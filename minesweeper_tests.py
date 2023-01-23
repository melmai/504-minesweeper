import unittest
from minesweeper import minesweeper
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
        field = Minefield(1,1)
        field.add_row("*", 0)

        # checks that the field data of one mine reflects the single mine accurately
        self.assertEqual(field._data, [["*"]], "1 row, 1 col single mine field not printed correctly")

    def test_min_space(self):
        # adds a single row, single column minefield with only one .
        field = Minefield(1, 1)
        field.add_row(".", 0)

        # checks that the field data of one . reflects the single it accurately with a single 0
        self.assertEqual(field._data, [[0]], "1 row, 1 col single space field not printed correctly")

    def test_max_mines(self):
        # runs the minesweeper function for the test input file and writes to the test output file
        minesweeper("mines_input_test.txt", "mines_output_test.txt")

        # opens the output file and stores the output line range to read for testing, then closes the output file
        output_file = open("mines_output_test.txt", 'r')
        test_range = output_file.readlines()[0:101]
        output_file.close()

        # checks that the lines pulled from the output file in the testing range match a 100x100 all-mines minefield output
        self.assertEqual(test_range, ['Field #1:\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n', '****************************************************************************************************\n']
, 'Did not print max mines output for a 100x100 minefield correctly, all field char should be *')

    def test_max_spaces(self):
        # runs the minesweeper function for the test input file and writes to the test output file
        minesweeper("mines_input_test.txt", "mines_output_test.txt")

        # opens the output file and stores the output line range to read for testing, then closes the output file
        output_file = open("mines_output_test.txt", 'r')
        test_range = output_file.readlines()[102:203]
        output_file.close()

        # checks that the lines pulled from the output file in the testing range match a 100x100 all-0 minefield output
        self.assertEqual(test_range, ['Field #2:\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n']
, 'Did not print max spaces output for a 100x100 minefield correctly, all field char should be 0')

    def test_max_mines_horizontal(self):
        # runs the minesweeper function for the test input file and writes to the test output file
        minesweeper("mines_input_test.txt", "mines_output_test.txt")

        # opens the output file and stores the output line range to read for testing, then closes the output file
        output_file = open("mines_output_test.txt", 'r')
        test_range = output_file.readlines()[204:206]
        output_file.close()

        # checks that the lines pulled from the output file in the testing range match a 1x100 all-mine minefield output
        self.assertEqual(test_range, ['Field #3:\n', '****************************************************************************************************\n'], 'Did not correctly print all mines output for a 1x100 minefield')

    def test_max_mines_vertical(self):
        # runs the minesweeper function for the test input file and writes to the test output file
        minesweeper("mines_input_test.txt", "mines_output_test.txt")

        # opens the output file and stores the output line range to read for testing, then closes the output file
        output_file = open("mines_output_test.txt", 'r')
        test_range = output_file.readlines()[207:308]
        output_file.close()

        # checks that the lines pulled from the output file in the testing range match a 100x1 all-mine minefield output
        self.assertEqual(test_range, ['Field #4:\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n']
, 'Did not correctly print all mines output for a 100x1 minefield')

    def test_max_spaces_horizontal(self):
        # runs the minesweeper function for the test input file and writes to the test output file
        minesweeper("mines_input_test.txt", "mines_output_test.txt")

        # opens the output file and stores the output line range to read for testing, then closes the output file
        output_file = open("mines_output_test.txt", 'r')
        test_range = output_file.readlines()[309:311]
        output_file.close()

        # checks that the lines pulled from the output file in the testing range match a 1x100 all-0 minefield output
        self.assertEqual(test_range, ['Field #5:\n', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n'], 'Did not correctly print all 0 output for a 1x100 all . minefield')

    def test_max_spaces_vertical(self):
        # runs the minesweeper function for the test input file and writes to the test output file
        minesweeper("mines_input_test.txt", "mines_output_test.txt")

        # opens the output file and stores the output line range to read for testing, then closes the output file
        output_file = open("mines_output_test.txt", 'r')
        test_range = output_file.readlines()[312:413]
        output_file.close()

        # checks that the lines pulled from the output file in the testing range match a 100x1 all-0 minefield output
        self.assertEqual(test_range, ['Field #6:\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n']
, 'Did not correctly print all 0 output for a 100x1 all . minefield')


if __name__ == '__main__':
    unittest.main()
