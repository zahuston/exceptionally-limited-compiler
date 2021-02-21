from .token import Token
from .position import Position
import pdb

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
STRING_DELINEATOR = "\""

class Lexer:
    def __init__(self, code):
        if len(code) <= 0:
            raise Exception("Gotta give me something to work with in this file")

        self.code = code
        self.token = Token('String', 'Hello')
        self.position = Position(0, 0, code[0])
        self.code_index = 0
        self.current_char = code[0]

    def tokenize(self):
        for self.code_index in range(len(self.code)):
            if self.current_char in DIGITS:
                tokens.append(self.parse_numeric())
            elif self.current_char in STRING_DELINEATOR:
                tokens.append(self.parse_string_literal())
            else:
                print(f"Nothing implemented yet for current character ({self.current_char})")

            self.advance()

        print(f"Tokenized file of length {char_count}")
        return []

    def advance(self):
        self.code_index += 1

        if (self.code_index > len(self.code)):
            print("Reached the end of the file, cannot advance")
            return

        self.position.advance_position(self.code[self.code_index])

    def parse_numeric(self):
        numeric_string = ''
        while(self.current_char in DIGITS):
            numeric_string += self.current_char
            self.advance()

    def parse_string_literal(self):
        string_literal = ""
        while(self.current_char != STRING_DELINEATOR):
            string_literal += current_char
