import unittest
from minefield import Minefield


class MinefieldTests(unittest.TestCase):
    def test_init(self):
        """This method tests the instantiation of a minefield"""
        minefield = Minefield(5, 7)

        # check rows, cols, and dataset upon creation of minefield object
        self.assertEqual(5, minefield.rows, "Minefield should have 5 rows.")
        self.assertEqual(7, minefield.cols, "Minefield should have 7 rows.")
        self.assertEqual([], minefield.data,
                         'Minefield should have empty data array.')

    def test_create_row(self):
        """
        This method tests the creation of a single row from a list of chars
        """
        minefield = Minefield(3, 5)

        # test creation of row with all bombs
        all_bombs = minefield.create_row(["*", "*", "*", "*", "*"])
        self.assertEqual(["*", "*", "*", "*", "*"], all_bombs,
                         "Minefield row should be all bombs.")

        # test creation of row with no bombs
        no_bombs = minefield.create_row([".", ".", ".", ".", "."])
        self.assertEqual([0, 0, 0, 0, 0], no_bombs,
                         'Minefield row should have 0-0-0-0-0')

        # test creation of row with some bombs
        some_bombs = minefield.create_row(["*", "*", "*", ".", "."])
        self.assertEqual(["*", "*", "*", 1, 0], some_bombs,
                         'Minefield not incrementing properly')


if __name__ == '__main__':
    unittest.main()
