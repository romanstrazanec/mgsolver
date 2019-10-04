from src.data_resolver import DataResolver
from src.messages import EMPTY_RES_FILE
from src.nonogram_marks import value_to_mark
from src.size import Size


class Solver:
    def __init__(self):
        self.left = DataResolver.get_left_data()
        self.top = DataResolver.get_top_data()
        try:
            self.size = Size(width=len(self.top), height=len(self.left))
        except ValueError:
            raise Exception(EMPTY_RES_FILE)

        self.solution = [[0 for _ in range(self.size.width)] for _ in range(self.size.height)]

    def __str__(self) -> str:
        return '\n'.join('|'.join(value_to_mark(elem) for elem in line) for line in self.solution)
