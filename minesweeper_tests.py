import unittest
from minefield import Minefield


class MinefieldTests(unittest.TestCase):
    def test_init(self):
        """This method tests the instantiation of a minefield"""
        minefield = Minefield(5, 7)
        self.assertEqual(5, minefield.rows, "Minefield should have 5 rows.")
        self.assertEqual(7, minefield.cols, "Minefield should have 7 rows.")
        self.assertEqual([], minefield.data,
                         'Minefield should have empty data array.')

    def test_create_row(self):
        minefield = Minefield(3, 5)
        all_bombs = minefield.create_row(["*", "*", "*", "*", "*"])
        self.assertEqual(["*", "*", "*", "*", "*"], all_bombs,
                         "Minefield row should be all bombs.")
        no_bombs = minefield.create_row([".", ".", ".", ".", "."])
        self.assertEqual([0, 0, 0, 0, 0], no_bombs,
                         'Minefield row should have 0-0-0-0-0')
        some_bombs = minefield.create_row(["*", "*", "*", ".", "."])
        self.assertEqual(["*", "*", "*", 1, 0], some_bombs,
                         'Minefield not incrementing properly')


if __name__ == '__main__':
    unittest.main()
