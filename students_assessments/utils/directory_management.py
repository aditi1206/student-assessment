"""DIRECTORY MANAGEMENT"""
import os
from students_assessments.constants import CSV_EXTENSION, APP_DIRS, CLASS_DATA_FILES_PATH

# TODO: Convert Functions to a Class


def get_files(current_working_directory, extension=CSV_EXTENSION):
    """
    GET FILES IN A DIRECTORY
    :param current_working_directory: {str} Path of File(s)
    :param extension: {str} File Extension
    :return: {list} List of Files with extension
    """
    print('WORKING DIRECTORY: {}'.format(current_working_directory))
    files_list = []
    try:
        for root, dirs, files in os.walk(current_working_directory):
            for file in files:
                # print(file)
                try:
                    if file.lower().endswith(extension):
                        files_list.append(file)
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)
    print('FILES LIST WITH EXTENSION: {}'.format(files_list))
    return files_list


def create_dir(dir_path):
    """
    CREATE DIR
    :param dir_path: {List} List of Directories
    :return: {Bool} True if Successfully created else False
    """
    paths_lst = list()
    directory_created = False
    try:
        if not isinstance(dir_path, list):
            paths_lst.append(dir_path)
            dir_path = paths_lst
        for d in dir_path:
            if not os.path.exists(d):
                os.makedirs(d)
                print('DIRECTORY {directory} WAS CREATED'.format(directory=d))
                directory_created = True
    except Exception as e:
        print('EXCEPTION IN CREATING DIRECTORY: {}'.format(e))
        return False
    return directory_created


if __name__ == '__main__':
    files_list = get_files(current_working_directory=CLASS_DATA_FILES_PATH, extension=CSV_EXTENSION)
    create_dir(dir_path=APP_DIRS)
