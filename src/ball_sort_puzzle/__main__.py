from solver import BallSortPuzzleSolver
from levels import Levels

b = BallSortPuzzleSolver(Levels.l2)
b.solve()
print(b.cells)
