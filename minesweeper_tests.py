import unittest
from minesweeper import Minesweeper


class MinesweeperTests(unittest.TestCase):
    def test_output(self):
        Minesweeper("max_input_test.txt", "new_output_test.txt")
        with open("max_output_test.txt", 'r') as file:
            original_test_output = file.read(8)
        with open("new_output_test.txt", 'r') as file2:
            new_test_output = file2.read(8)
        self.assertEqual(original_test_output, new_test_output)

    def test_max_mines(self):
        """
        This method tests the ability of the Minesweeper class to create an accurate
        minefield of the maximum size (100x100) composed of all mines
        """
        # runs the minesweeper function for the test input file and writes
        # to the test output file
        Minesweeper("max_input_test.txt", "max_output_test.txt")

        # opens the output file and stores the output line range to read for
        # testing, then closes the output file
        output_file = open("max_output_test.txt", 'r')
        test_range = output_file.readlines()[0:101]
        output_file.close()

        # checks that the lines pulled from the output file in the testing
        # range match a 100x100 all-mines minefield output
        self.assertEqual(test_range, ['Field #1:\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n',
                                      '****************************************************************************************************\n']
                         ,
                         'Did not print max mines output for a 100x100 '
                         'minefield correctly, all field char should be *')

    def test_max_spaces(self):
        """
        This method tests the ability of the Minesweeper class to create an accurate
        minefield of the maximum size (100x100) composed of all '.', aka spaces
        """
        # runs the minesweeper function for the test input file and writes
        # to the test output file
        Minesweeper("max_input_test.txt", "max_output_test.txt")

        # opens the output file and stores the output line range to read for
        # testing, then closes the output file
        output_file = open("max_output_test.txt", 'r')
        test_range = output_file.readlines()[102:203]
        output_file.close()

        # checks that the lines pulled from the output file in the testing
        # range match a 100x100 all-0 minefield output
        self.assertEqual(test_range, ['Field #2:\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n']
                         ,
                         'Did not print max spaces output for a 100x100 '
                         'minefield correctly, all field char should be 0')

    def test_max_mines_horizontal(self):
        """
        This method tests the ability of the Minesweeper class to create an accurate
        minefield of the maximum rows and minimum columns (1x100) composed of all mines
        """
        # runs the minesweeper function for the test input file and writes
        # to the test output file
        Minesweeper("max_input_test.txt", "max_output_test.txt")

        # opens the output file and stores the output line range to read for
        # testing, then closes the output file
        output_file = open("max_output_test.txt", 'r')
        test_range = output_file.readlines()[204:206]
        output_file.close()

        # checks that the lines pulled from the output file in the testing
        # range match a 1x100 all-mine minefield output
        self.assertEqual(test_range, ['Field #3:\n',
                                      '****************************************************************************************************\n'],
                         'Did not correctly print all mines output for a '
                         '1x100 minefield')

    def test_max_mines_vertical(self):
        """
        This method tests the ability of the Minesweeper class to create an accurate
        minefield of the minimum rows and maximum columns (100x1) composed of all mines
        """
        # runs the minesweeper function for the test input file and writes
        # to the test output file
        Minesweeper("max_input_test.txt", "max_output_test.txt")

        # opens the output file and stores the output line range to read for
        # testing, then closes the output file
        output_file = open("max_output_test.txt", 'r')
        test_range = output_file.readlines()[207:308]
        output_file.close()

        # checks that the lines pulled from the output file in the testing
        # range match a 100x1 all-mine minefield output
        self.assertEqual(test_range,
                         ['Field #4:\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n', '*\n', '*\n', '*\n',
                          '*\n', '*\n', '*\n', '*\n']
                         ,
                         'Did not correctly print all mines output for a '
                         '100x1 minefield')

    def test_max_spaces_horizontal(self):
        """
        This method tests the ability of the Minesweeper class to create an accurate
        minefield of the maximum rows and minimum columns (1x100) composed of all '.'
        """
        # runs the minesweeper function for the test input file and writes
        # to the test output file
        Minesweeper("max_input_test.txt", "max_output_test.txt")

        # opens the output file and stores the output line range to read for
        # testing, then closes the output file
        output_file = open("max_output_test.txt", 'r')
        test_range = output_file.readlines()[309:311]
        output_file.close()

        # checks that the lines pulled from the output file in the testing
        # range match a 1x100 all-0 minefield output
        self.assertEqual(test_range, ['Field #5:\n',
                                      '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n'],
                         'Did not correctly print all 0 output for a 1x100 '
                         'all . minefield')

    def test_max_spaces_vertical(self):
        """
        This method tests the ability of the Minesweeper class to create an accurate
        minefield of the minimum rows and maximum columns (100x1) composed of all '.'
        """
        # runs the minesweeper function for the test input file and writes
        # to the test output file
        Minesweeper("max_input_test.txt", "max_output_test.txt")

        # opens the output file and stores the output line range to read for
        # testing, then closes the output file
        output_file = open("max_output_test.txt", 'r')
        test_range = output_file.readlines()[312:413]
        output_file.close()

        # checks that the lines pulled from the output file in the testing
        # range match a 100x1 all-0 minefield output
        self.assertEqual(test_range,
                         ['Field #6:\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n',
                          '0\n', '0\n', '0\n', '0\n']
                         ,
                         'Did not correctly print all 0 output for a 100x1 '
                         'all . minefield')


if __name__ == '__main__':
    unittest.main()
