"""CONSTANTS"""
import os
from datetime import datetime

ROOT_DIR = os.getcwd()
DATE_TIME_FORMAT = '%m-%d-%YT%H:%M:%S'
DATE_TIME = datetime.now().strftime(DATE_TIME_FORMAT)

CLASS_DATA_FILES_PATH = os.environ.get('FILES_PATH', r'assets')
CSV_EXTENSION = '.csv'

OUTPUT_PATH = os.path.join(ROOT_DIR, '..', r'output')
OUT_PUT_FILE_NAME = r'Automated Report_{date_time}.txt'.format(date_time=DATE_TIME)
OUTPUT_FILE_NAME = os.environ.get('OUTPUT_FILES_PATH', os.path.join(OUTPUT_PATH, OUT_PUT_FILE_NAME))

APP_DIRS = [OUTPUT_PATH]

TEMPLATE_PATH = os.environ.get('OUTPUT_FILES_PATH', os.path.join(ROOT_DIR, 'students_data_template.txt'))
