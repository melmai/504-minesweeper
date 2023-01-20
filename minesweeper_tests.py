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

    def test_update_row(self):
        """
        This method tests the update_row() method to make sure the values are
        incrementing properly
        """
        minefield = Minefield(5, 5)

        # set test data
        minefield.data = [[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          ["*", 1, 0, 1, "*"]]

        # update the second row based on the third row (next)
        minefield.update_row(1)
        expected_data = [[0, 0, 0, 0, 0],
                          [1, 1, 0, 1, 1],
                          ["*", 1, 0, 1, "*"]]
        self.assertEqual(expected_data, minefield.data,
                         "Row not updating based on next row.")

        # update the minefield data
        minefield.data = [[0, 0, 0, 0, 0],
                          [1, 1, 0, 1, 1],
                          ["*", 1, 0, 1, "*"],
                          ["*", 1, 0, 1, "*"]]

        # update the third and fourth rows based on new data
        minefield.update_row(2)
        minefield.update_row(3, "prev")
        expected_data = [[0, 0, 0, 0, 0],
                         [1, 1, 0, 1, 1],
                         ["*", 2, 0, 2, "*"],
                         ["*", 2, 0, 2, "*"]]
        self.assertEqual(expected_data, minefield.data,
                         "Row not updating based on previous row.")


if __name__ == '__main__':
    unittest.main()
