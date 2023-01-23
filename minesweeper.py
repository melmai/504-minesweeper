from minefield import Minefield


class Minesweeper:
    def __init__(self,
                 input_file="mines.txt",
                 output_file="minesweeper_output.txt"):

        self._input_file = open(input_file, 'r')
        self._output_file = open(output_file, 'w')
        self.process_file()

    def process_file(self):
        """
        This method reads the provided input file and prints hints to the
        provided output file.
        """
        # get dimensions and initialize field numbers
        dimensions = self._input_file.readline().strip()
        field_number = 0

        # until the EOF, create and process the minefields of the input
        while dimensions != "0 0":
            dimensions, field_number = \
                self.generate_minefield_hints(
                    dimensions, field_number)

        # close i/o files
        self._input_file.close()
        self._output_file.close()

    def generate_minefield_hints(self, dimensions, field_number):
        """
        This method creates a minefield from the input data and prints the
        hints of the minefield to the output file.
        :param dimensions: string representing the rows and columns of the
        minefield
        :param field_number: int of the current minefield
        :return: dimensions of the next minefield and the current field number
        """
        # process row/col values and increment field number
        rows, cols = dimensions.split()
        field_number += 1

        # the row/col values are strings that should be ints
        # the row/col values are strings that should be ints
        rows = int(rows)
        cols = int(cols)

        # create minefield
        field = Minefield(rows, cols)

        # write field labels
        self._output_file.write(f"Field #{field_number}:\n")

        # read lines of minefield
        for n in range(rows):
            line = self._input_file.readline().strip('\n')
            field.add_row(line, n)

        # write data to file
        output = str(field)
        self._output_file.write(output + "\n")

        # process new row/col values
        dimensions = self._input_file.readline().strip()

        return dimensions, field_number


if __name__ == '__main__':
    Minesweeper()
