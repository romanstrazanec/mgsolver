from csv import reader as csv_reader
from os.path import join as path_join

from src.messages import DR_INCORRECT_FN


class DataResolver:
    RES_DIR_PATH = path_join('..', 'res')
    LEFT_CSV_FN = 'left.csv'
    TOP_CSV_FN = 'top.csv'

    @staticmethod
    def get_left_data():
        return DataResolver._get_data(DataResolver.LEFT_CSV_FN)

    @staticmethod
    def get_top_data():
        return DataResolver._get_data(DataResolver.TOP_CSV_FN)

    @staticmethod
    def _get_data(file_name: str):
        DataResolver._validate_file_name(file_name)
        with open(path_join(DataResolver.RES_DIR_PATH, file_name)) as f:
            reader = csv_reader(f)
            return [[int(elem) for elem in line] for line in reader]

    @staticmethod
    def _validate_file_name(fn: str):
        if fn not in [DataResolver.LEFT_CSV_FN, DataResolver.TOP_CSV_FN]:
            raise Exception(DR_INCORRECT_FN % (DataResolver.LEFT_CSV_FN, DataResolver.TOP_CSV_FN))
