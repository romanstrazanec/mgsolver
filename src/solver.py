from src.data_resolver import DataResolver


class Solver:
    def __init__(self):
        self.left = DataResolver.get_left_data()
        self.top = DataResolver.get_top_data()

    @property
    def size(self):
        return len(self.left), len(self.top)
