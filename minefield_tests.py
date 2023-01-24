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

    def test_min_mine(self):
        # adds a single row, single column minefield with only one mine
        field = Minefield(1, 1)
        field.add_row("*", 0)

        # checks that the field data of one mine reflects the single mine
        # accurately
        self.assertEqual(field._data, [["*"]],
                         "1 row, 1 col single mine field not printed "
                         "correctly")

    def test_min_space(self):
        # adds a single row, single column minefield with only one .
        field = Minefield(1, 1)
        field.add_row(".", 0)

        # checks that the field data of one . reflects the single it
        # accurately with a single 0
        self.assertEqual(field._data, [[0]],
                         "1 row, 1 col single space field not printed "
                         "correctly")

    def test_size(self):
        """
        Tests to make sure that the field and columns are equal to what they are set to
        """
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
        """
        Tests to make sure that the hints are correct at specific spots.
        """

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
        """
        Tests to make sure if minefield is set to 0, 0 that it is actually empty

        """
        field = Minefield(0, 0)
        self.assertEqual(field._data, [])

    def test_all_numbers(self):
        """
        Tests to make sure that hints are generated correctly. Testing that it produces numbers 1-8

        """
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
        """
        Tests that verify that a whole hint field is generated correctly.

        """
        field = Minefield(3, 3)
        field.add_row(".**", 0)
        field.add_row("*.*", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data,
                         [[2, '*', '*'], ['*', 7, '*'], ['*', '*', '*']])
        field = Minefield(3, 3)
        field.add_row("**.", 0)
        field.add_row("*.*", 1)
        field.add_row("***", 2)
        self.assertEqual(field._data,
                         [['*', '*', 2], ['*', 7, '*'], ['*', '*', '*']])
        field = Minefield(3, 3)
        field.add_row(".**", 0)
        field.add_row("*.*", 1)
        field.add_row("*..", 2)
        self.assertEqual(field._data,
                         [[2, '*', '*'], ['*', 5, '*'], ['*', 3, 1]])
        field = Minefield(3, 12)
        field.add_row(".**..*...*..", 0)
        field.add_row("*.*..*..**..", 1)
        field.add_row("*....*..**..", 2)
        self.assertEqual(field._data,
                         [[2, '*', '*', 2, 2, '*', 2, 1, 3, '*', 2, 0],
                          ['*', 5, '*', 2, 3, '*', 3, 2, '*', '*', 3, 0],
                          ['*', 3, 1, 1, 2, '*', 2, 2, '*', '*', 2, 0]])


if __name__ == '__main__':
    unittest.main()
