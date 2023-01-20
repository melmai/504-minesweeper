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
        incrementing properly based on the row before/after a given row
        position.
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

    def test_add_row(self):
        """
        This method tests the add_row() method, which accepts a string of
        characters, generates a list containing "*" for a bomb or ints that
        represent the number of bombs surrounding that position, and appends
        the list to the object's data property.
        """
        minefield = Minefield(5, 5)

        # add row of all bombs
        minefield.add_row("*****", 0)
        self.assertEqual([["*", "*", "*", "*", "*"]], minefield.data,
                         'Row of chars not being processed accurately.')

        # add row of no bombs
        minefield.add_row(".....", 1)
        self.assertEqual([["*", "*", "*", "*", "*"],
                          [2, 3, 3, 3, 2]], minefield.data,
                         'Row of chars not being processed accurately.')

        # add row of some bombs
        minefield.add_row("..*.*", 2)
        self.assertEqual([["*", "*", "*", "*", "*"],
                          [2, 4, 4, 5, 3],
                          [0, 1, "*", 2, "*"]], minefield.data,
                         'Row of chars not being processed accurately.')

    def test_bomb_found(self):
        """
        This method tests the helper method that identifies if a given row
        contains a bomb.
        """
        minefield = Minefield(5, 5)

        # create a test row with a bomb, should return True
        minefield.data = [["*", 1, 0, 0, 0]]
        bomb_found = minefield.bomb_found(0)
        self.assertEqual(True, bomb_found, "bomb_found() should return True")

        # replace test row with no bombs, should return False
        minefield.data = [[0, 0, 0, 0, 0]]
        bomb_found = minefield.bomb_found(0)
        self.assertEqual(False, bomb_found, "bomb_found() should return False")

    def test_is_bomb(self):
        """
        This method tests the helper method that identifies a cell as
        having a bomb.
        """
        # * values should return True
        self.assertEqual(True, Minefield.is_bomb("*"),
                         "is_bomb() should return True for '*'")

        # . values should return False
        self.assertEqual(False, Minefield.is_bomb("."),
                         "is_bomb() should return False for '.'")

if __name__ == '__main__':
    unittest.main()
