from minefield import Minefield


def minesweeper(input_file="mines.txt", output_file="minesweeper_output.txt"):
    # set up i/o files
    input_file = open(input_file, 'r')
    output_file = open(output_file, 'w')

    # get dimensions and initialize field numbers
    dimensions = input_file.readline().strip()
    field_number = 0

    while dimensions != "0 0":

        # process row/col values and increment field number
        rows, cols = dimensions.split()
        field_number += 1

        # the row/col values are strings that should be ints
        rows = int(rows)
        cols = int(cols)

        # create minefield
        field = Minefield(rows, cols)

        # write field labels
        output_file.write(f"Field #{field_number}:\n")

        # read lines of minefield
        for n in range(rows):
            line = input_file.readline().strip('\n')
            field.add_row(line, n)

        # write data to file
        output = str(field)
        output_file.write(output + "\n")

        # process new row/col values
        dimensions = input_file.readline().strip()

    # close i/o files
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    # test
    minesweeper("mines_input_test.txt", "mines_output_test.txt")

    # real
    minesweeper()

