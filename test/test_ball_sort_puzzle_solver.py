import unittest

from src.ball_sort_puzzle.solver import BallSortPuzzle
from src.ball_sort_puzzle.color import Color


class Levels:
    l1 = [
        [Color.orange],
        [Color.orange, Color.orange, Color.orange]
    ]

    l2 = [
        [Color.blue, Color.orange, Color.blue, Color.orange],
        [Color.orange, Color.blue, Color.orange, Color.blue],
        []
    ]

    l3 = [
        [Color.blue, Color.orange, Color.red, Color.blue],
        [Color.orange, Color.orange, Color.red, Color.blue],
        [Color.red, Color.blue, Color.orange, Color.red]
    ]

    l103 = [
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


class TestBallSortPuzzleSolver(unittest.TestCase):

    # def setUp(self) -> None:
    #     self.solver = Ball

    def test_level1(self):
        solver = BallSortPuzzle(Levels.l1)
        self.assertTrue(solver.solve())

    def test_level2(self):
        solver = BallSortPuzzle(Levels.l2)
        self.assertTrue(solver.solve())
