import unittest
from main import minesweeper
from minefield import Minefield


# output validation test and hint validation test

class minetest(unittest.TestCase):
    def test_hint_homogenous(self):
        field = Minefield(3, 3)
        field.add_row("...", 0)
        field.add_row("...", 1)
        field.add_row("...", 2)
        self.assertEqual(field._data, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        field = Minefield(3, 3)
        field.add_row("***", 0)
        field.add_row("***", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data, [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']])
        field = Minefield(6, 6)
        field.add_row("******", 0)
        field.add_row("******", 1)
        field.add_row("******", 2)
        field.add_row("******", 3)
        field.add_row("******", 4)
        field.add_row("******", 5)
        self. assertEqual(field._data, [['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*']])

    def test_hint_mt(self):
        field = Minefield(0, 0)
        self.assertEqual(field._data, [])

    def test_just_one(self):
        field = Minefield(3, 3)
        field.add_row("...", 0)
        field.add_row(".*.", 1)
        field.add_row("...", 2)
        self.assertEqual(field._data, [[1, 1, 1], [1, '*', 1], [1, 1, 1]])
        field = Minefield(3, 3)
        field.add_row("***", 0)
        field.add_row("*.*", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data, [['*', '*', '*'], ['*', 8, '*'], ['*', '*', '*']])
        field = Minefield(3, 3)
        field.add_row(".**", 0)
        field.add_row("*.*", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data,[[2, '*', '*'], ['*', 7, '*'], ['*', '*', '*']])
        field = Minefield(3, 3)
        field.add_row("**.", 0)
        field.add_row("*.*", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data, [['*', '*', 2], ['*', 7, '*'], ['*', '*', '*']])

    def test_random(self):
        field = Minefield(3, 3)
        field.add_row(".**", 0)
        field.add_row("*.*", 1)
        field.add_row("*..", 2)
        self.assertEqual(field._data, [[2, '*', '*'], ['*', 5, '*'], ['*', 3, 1]])
        field = Minefield(3, 12)
        field.add_row(".**..*...*..", 0)
        field.add_row("*.*..*..**..", 1)
        field.add_row("*....*..**..", 2)
        self.assertEqual(field._data, [[2, '*', '*', 2, 2, '*', 2, 1, 3, '*', 2, 0],
 ['*', 5, '*', 2, 3, '*', 3, 2, '*', '*', 3, 0],
 ['*', 3, 1, 1, 2, '*', 2, 2, '*', '*', 2, 0]])


if __name__ == '__main__':
    unittest.main()
