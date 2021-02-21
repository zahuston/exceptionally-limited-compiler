NEW_LINE_CHARACTERS = ['\n', '\r'] # Windows nonsense.. sorry friend

class Position:
    def __init__(self, row, col, char_at_position):
        self.row = row
        self.col = col
        self.char_at_position = char_at_position
        self.char_count = 0

    def is_end_of_file(self):
        self.char_at_position == None or self.char_at_position == ''

    def advance_position(self, new_char):
        if self.is_end_of_file():
            return False

        self.char_count += 1
        self.row += 1

        if self.char_at_position in NEW_LINE_CHARACTERS:
            self.row = 0
            self.col = 0
        self.char_at_position = new_char

        return True
