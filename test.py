import unittest
from minesweeper import minesweeper
from minefield import Minefield


# output validation test and hint validation test

class minetest(unittest.TestCase):
    def test_output(self):
        minesweeper("mines_input_test.txt", "new_output_test.txt")
        with open("mines_output_test.txt", 'r') as file:
            original_test_output = file.read(8)
        with open("new_output_test.txt", 'r') as file2:
            new_test_output = file2.read(8)
        self.assertEqual(original_test_output, new_test_output)

    def test_size(self):
        field = Minefield(4, 4)
        self.assertEqual(field.rows, 4)
        self.assertEqual(field.cols, 4)
        field = Minefield(100, 100)
        self.assertEqual(field.rows, 100)
        self.assertEqual(field.cols, 100)
        field = Minefield(0, 0)
        self.assertEqual(field.rows, 0)
        self.assertEqual(field.cols, 0)

    def test_hint_homogenous(self):
        field = Minefield(3, 3)
        field.add_row("...", 0)
        field.add_row("...", 1)
        field.add_row("...", 2)
        self.assertEqual(field._data[0][0], 0)
        field = Minefield(3, 3)
        field.add_row("***", 0)
        field.add_row("***", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data[1][1], "*")
        field = Minefield(6, 6)
        field.add_row("******", 0)
        field.add_row("******", 1)
        field.add_row("******", 2)
        field.add_row("******", 3)
        field.add_row("******", 4)
        field.add_row("******", 5)
        self.assertEqual(field._data[3][4], '*')

    def test_hint_mt(self):
        field = Minefield(0, 0)
        self.assertEqual(field._data, [])

    def test_all_numbers(self):
        field = Minefield(3, 3)
        field.add_row("...", 0)
        field.add_row(".*.", 1)
        field.add_row("...", 2)
        self.assertEqual(field._data[0][1], 1)
        field = Minefield(3, 3)
        field.add_row(".*.", 0)
        field.add_row(".*.", 1)
        field.add_row("...", 2)
        self.assertEqual(field._data[0][0], 2)
        field = Minefield(3, 3)
        field.add_row(".*.", 0)
        field.add_row("**.", 1)
        field.add_row("...", 2)
        self.assertEqual(field._data[0][0], 3)
        field = Minefield(3, 3)
        field.add_row("...", 0)
        field.add_row("..*", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data[1][1], 4)
        field = Minefield(3, 3)
        field.add_row("...", 0)
        field.add_row("*.*", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data[1][1], 5)
        field = Minefield(3, 3)
        field.add_row("..*", 0)
        field.add_row("*.*", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data[1][1], 6)
        field = Minefield(3, 3)
        field.add_row("***", 0)
        field.add_row("*..", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data[1][1], 7)
        field = Minefield(3, 3)
        field.add_row("***", 0)
        field.add_row("*.*", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data[1][1], 8)

    def test_whole_field(self):
        field = Minefield(3, 3)
        field.add_row(".**", 0)
        field.add_row("*.*", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data, [[2, '*', '*'], ['*', 7, '*'], ['*', '*', '*']])
        field = Minefield(3, 3)
        field.add_row("**.", 0)
        field.add_row("*.*", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data, [['*', '*', 2], ['*', 7, '*'], ['*', '*', '*']])
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
