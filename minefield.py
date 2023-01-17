class Minefield:
    """This class creates a minefield represented as a 2D array"""

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._data = []

    def add_row(self, line, row):
        """
        This method adds a new row for the minefield grid, checks the rows
        above and below, and increments the values if needed.
        :param line: string of data
        :param row: the row number
        :return: None
        """

        # create row from line and add to 2d list
        chars = [*line]
        grid_row = self.create_row(chars)
        self._data.append(grid_row)

        # if bombs in previous row, update current row
        if row != 0 and self.bomb_found(row - 1):
            self._data[row] = self.update_row(row, "prev")

        # if bombs in current row, update previous row
        if (row - 1) >= 0 and self.bomb_found(row):
            self._data[row - 1] = self.update_row(row - 1)

    def update_row(self, row_to_update, reference="next"):
        """
        This method increments the bomb tracking values of a given row based on
        another referenced row (above or below the row to update)
        :param int row_to_update: the row of values to update
        :param string reference: row to reference when updating
        row_to_update. Values are "prev" or "next", default is "next"
        :return: list: updated row of values
        """
        row = self._data[row_to_update]

        # row to base updated values on based on previous/next row
        if reference == "prev":
            ref_row = self._data[row_to_update - 1]
        elif reference == "next":
            ref_row = self._data[row_to_update + 1]
        else:
            raise Exception("Not a valid reference argument.")

        for m in range(self._cols):
            is_first = True if m == 0 else False
            is_last = True if m == self._cols - 1 else False

            # if there's a bomb in the reference row, adjust the updated row
            if self.is_bomb(ref_row[m]):
                # increment value at same index, if not also a bomb
                if not self.is_bomb(row[m]):
                    row[m] += 1

                # increment value after, if not the last col
                if not is_last and not self.is_bomb(row[m + 1]):
                    row[m + 1] += 1

                # increment value before, if not the first col
                if not is_first and not self.is_bomb(row[m - 1]):
                    row[m - 1] += 1

        return row

    def create_row(self, chars):
        """
        This method creates a row based on a string of text and updates the
        bomb count value based on the character before and after.
        :param list chars: characters of the provided file line
        :return: list of bomb count within the same row
        """
        row = []
        for m in range(self._cols):

            # it's a bomb - add it
            if self.is_bomb(chars[m]):
                row.append(chars[m])

                # increment previous col, if exists and is not a bomb
                if (m - 1) >= 0 and not self.is_bomb(row[m - 1]):
                    row[m - 1] = row[m - 1] + 1

            # it's not a bomb, but there's one right before it
            elif (m - 1) >= 0 and self.is_bomb(chars[m - 1]):
                row.append(1)

            # no bomb
            else:
                row.append(0)
        return row

    def bomb_found(self, row):
        """
        This method checks the row to see if a bomb is present
        :param int row: row to check
        :return: boolean
        """
        return "*" in self._data[row]

    @staticmethod
    def is_bomb(value):
        """
        This method checks the current value to see if it is a bomb
        :param value: string or int
        :return: boolean
        """
        return value == "*"

    def __str__(self):
        data = ''
        for row in self._data:
            for char in row:
                data += str(char)
            data += "\n"
        return data
