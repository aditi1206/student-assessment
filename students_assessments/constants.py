"""CONSTANTS"""
import os

ROOT_DIR = os.getcwd()
CLASS_DATA_FILES_PATH = os.environ.get('FILES_PATH', r'/Users/aditipancholi/PycharmProjects/students-assessment/assets')
CSV_EXTENSION = '.csv'

OUTPUT_PATH = r'/Users/aditipancholi/PycharmProjects/students-assessment/output'
OUT_PUT_FILE_NAME = r'Automated Report.txt'
OUTPUT_FILE_NAME = os.environ.get('OUTPUT_FILES_PATH', os.path.join(OUTPUT_PATH, OUT_PUT_FILE_NAME))

APP_DIRS = [OUTPUT_PATH]

TEMPLATE_PATH = os.environ.get('OUTPUT_FILES_PATH', os.path.join(ROOT_DIR, 'students_data_template.txt'))
