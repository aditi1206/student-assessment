""" AUTOMATION OF CLASSES REPORT"""
import os
import math
import pandas as pd
import numpy as np
import statistics
from utils.directory_management import create_dir, get_files
from constants import APP_DIRS,  CLASS_DATA_FILES_PATH, CSV_EXTENSION

"""
SETUP
"""
"""CREATE APP DIRECTORIES"""
# Create Output Folder
create_dir(dir_path=APP_DIRS)

"""GET FILES"""

get_csv_files = get_files(current_working_directory=CLASS_DATA_FILES_PATH,
                          extension=CSV_EXTENSION)

"""
UTILITY FUNCTIONS
"""


def round_class_average(value, n_digits=1):
    rounded_class_avg = round(value, ndigits=n_digits)
    return rounded_class_avg


def truncate_students_score(score=0):
    """
    Truncate Students Score
    :param score: {float} Students Score
    :return: {int} Truncated Score
    """
    try:
        score = math.trunc(float(score))  # CONVERTING TO FLOAT AND TRUNCATING
    except Exception as e:
        print(e)
    return score


"""READ CSV DATA"""

def get_average_class_score(scores):
    # data = np.array(scores, dtype=float)
    # data[data == 0] = np.nan
    # print(data)
    # print(type(data))
    # print("Shape of array is", data.shape)
    #
    # mean = np.nanmean(np.array(data))
    return scores


def process_student_progress(files_path, files):
    for file in files:
        data = pd.read_csv(filepath_or_buffer=os.path.join(files_path, file))
        # DATA FRAME
        df = pd.DataFrame(data)
        # print(df)
        # print(df)
        # print(df.values)

        students_scores = []
        for i in df.values:
            # print(i[1])
            students_scores.append(truncate_students_score(score=i[1]))

        students_scores = get_average_class_score(scores=students_scores)
        print('Students Scores: {}'.format(students_scores))
        rounded_class_average = round_class_average(value=students_scores)
        print('CLASS AVERAGE: {}'.format(rounded_class_average))

        print('\n')
        return '{}{}'.format(students_scores, rounded_class_average)
    class_details = {
        'class_name': file,
        'students_count': 10,
        'number_of_students_score': '9',
        'discarded_students': ['Edith Adkins'],
        'new_lines': '\n\n'}
    return class_details


data_frame = process_student_progress(files_path=CLASS_DATA_FILES_PATH, files=get_csv_files)


