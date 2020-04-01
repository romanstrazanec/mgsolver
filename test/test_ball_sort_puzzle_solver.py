import unittest

from src.ball_sort_puzzle.solver import BallSortPuzzle
from src.ball_sort_puzzle.color import Color


class TestBallSortPuzzleSolver(unittest.TestCase):
    def test_all_levels(self):
        for i in levels.keys():
            print(f'\nTESTING LEVEL {i}\n')
            ball_sort_puzzle = BallSortPuzzle(levels[i])
            self.assertTrue(ball_sort_puzzle.solve())
            print('=' * 25)

    def test_level(self):
        ball_sort_puzzle = BallSortPuzzle(levels[3])
        self.assertTrue(ball_sort_puzzle.solve())


levels = {
    1: [
        [Color.orange],
        [Color.orange, Color.orange, Color.orange]
    ],
    2: [
        [Color.blue, Color.orange, Color.blue, Color.orange],
        [Color.orange, Color.blue, Color.orange, Color.blue],
        []
    ],
    3: [
        [Color.blue, Color.orange, Color.red, Color.blue],
        [Color.orange, Color.orange, Color.red, Color.blue],
        [Color.red, Color.blue, Color.orange, Color.red]
    ],
    103: [
        [Color.cyan, Color.orange, Color.yellow, Color.lightblue],
        [Color.green, Color.yellow, Color.lightgreen, Color.lightblue],
        [Color.blue, Color.red, Color.cyan, Color.purple],
        [Color.gray, Color.red, Color.lightblue, Color.yellow],
        [Color.yellow, Color.blue, Color.pink, Color.green],
        [Color.lightgreen, Color.brown, Color.green, Color.brown],
        [Color.red, Color.purple, Color.blue, Color.brown],
        [Color.brown, Color.blue, Color.pink, Color.purple],
        [Color.gray, Color.cyan, Color.pink, Color.gray],
        [Color.lightblue, Color.lightgreen, Color.cyan, Color.orange],
        [Color.red, Color.purple, Color.gray, Color.green],
        [Color.orange, Color.lightgreen, Color.orange, Color.pink],
        [],
        []
    ]
}
