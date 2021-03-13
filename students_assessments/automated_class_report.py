""" AUTOMATION OF CLASSES REPORT"""
import os
import math
import pandas as pd
import numpy as np

from utils.directory_management import create_dir, get_files
from constants import APP_DIRS, CLASS_DATA_FILES_PATH, CSV_EXTENSION, OUTPUT_FILE_NAME, TEMPLATE_PATH
from render_template import render_template, generate_output

"""
SETUP
"""

"""CREATE APP DIRECTORIES"""
# Create Output Folder
create_dir(dir_path=APP_DIRS)

"""
UTILITY FUNCTIONS
"""


def round_class_average(value, n_digits=1):
    rounded_class_avg = round(value, ndigits=n_digits)
    return rounded_class_avg


def truncate_students_score(scores):
    """
    Truncate Students Score
    :param scores: {float} Students Scores
    :return: {int} Truncated Score
    """
    truncated_scores = []
    try:
        for score in scores:
            score = math.trunc(float(score))  # CONVERTING TO FLOAT AND TRUNCATING
            truncated_scores.append(score)
    except Exception as e:
        print(e)
    return truncated_scores


"""READ CSV DATA"""


def get_average_class_score(scores):
    mean = np.nanmean(np.array(scores))
    return mean


def get_class_name(file):
    return file.split('.csv')[0]


def add_students_data_template(data):
    format_string = ''
    for k, v in data.items():
        format_string += '{:<21}'.format(k) + ': ' + str(v) + '\n'
    return format_string


def process_students_score(data, file):
    class_details = {}
    discarded_students = []
    cleaned_grades = []
    try:
        for k, v in data.items():
            # print(k, v)
            # print(type(k), type(v))
            if float(v) == 0.00:
                # APPEND DISCARDED STUDENTS
                discarded_students.append(k)
            else:
                # REMOVE ZERO VALUES
                cleaned_grades.append(v)
        truncate_scores = truncate_students_score(scores=cleaned_grades)
        class_average = round_class_average(value=get_average_class_score(scores=truncate_scores))
        class_details.update({
            'class_name': get_class_name(file=file),
            'students_count': len(data),
            'number_of_students_score': len(data) - len(discarded_students),
            'discarded_students': discarded_students,
            'truncated_scores': truncate_scores,
            'class_average': class_average,
            'highest_average_class': '',
            'additional_data': '',
            # 'data': add_students_data_template(data=data),  # Additional Data if we want to append
            'average_all_classes_students': '',
            'new_lines': '\n'})
    except Exception as e:
        print(e)
    return class_details


def process_student_progress(files_path, files):
    # df = pd.DataFrame()
    data_processed = []
    for file in files:
        file_path = os.path.join(files_path, file)  # MULTIPLE OPERATING SYSTEMS HANDLING EX: /, \, \\, //
        data = pd.read_csv(filepath_or_buffer=file_path, header=0, index_col=0, squeeze=True).to_dict()
        data_processed.append(process_students_score(data=data, file=file))
    # print(data_processed)
    return data_processed


def calculate_highest_average(data):
    class_averages = {}
    for d in data:
        class_averages.update({d.get('class_name'): d.get('class_average')})
    highest_average_class = max(class_averages, key=class_averages.get)
    average_all_classes_students = get_average_class_score(scores=list(class_averages.values()))
    for d in data:
        if d.get('class_name') == highest_average_class:
            d.update({'highest_average_class': '\n*** \n{class_name} Highest Class Average compared to others \n***\n'
                                               ''.format(class_name=d.get('class_name'))})
        d.update({'average_all_classes_students': average_all_classes_students})
    return data


def execute():
    """
    Execute
    :return: {str} Success
    """
    response = False
    try:

        # GET FILES

        get_csv_files = get_files(current_working_directory=CLASS_DATA_FILES_PATH,
                                  extension=CSV_EXTENSION)
        # PROCESS STUDENTS INFORMATION
        class_details_list = process_student_progress(files_path=CLASS_DATA_FILES_PATH, files=get_csv_files)
        # CALCULATE HIGHEST CLASS AVERAGE
        data = calculate_highest_average(data=class_details_list)
        from pprint import pprint
        pprint(data)
        # RENDER TEMPLATE
        rendered_data = render_template(class_details=data, template_path=TEMPLATE_PATH)
        generate_output(data=rendered_data, file_path=OUTPUT_FILE_NAME)
        response = True
    except Exception as e:
        print(e)
    return response


if __name__ == '__main__':
    execute()
