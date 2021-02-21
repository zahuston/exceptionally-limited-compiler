NEW_LINE_CHARACTERS = ['\n', '\r'] # Windows nonsense.. sorry friend

class Position:
    def __init__(self, row, col, char):
        self.row = row
        self.col = col
        self.char = char
        self.char_count = 0

    def is_end_of_file(self):
        self.char == None or self.char == ''

    def advance_position(self, new_char):
        if self.is_end_of_file():
            return False

        self.char_count += 1
        self.row += 1

        if self.char in NEW_LINE_CHARACTERS:
            self.row = 0
            self.col = 0
        self.char = new_char

        return True
