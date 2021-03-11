from parser.token_jz import Token, OperatorToken, ControlToken
from .position import Position
import pdb

STRING_DELINEATORS = ['"']

class Lexer:
    def __init__(self, code):
        if len(code) <= 0:
            raise Exception("Gotta give me something to work with in this file")

        if code[len(code) - 1] != '\n':
            raise Exception("File must end on a new line")

        self.position = Position(0, 0, code[0])
        self.code = code
        self.code_index = 0

    def tokenize(self):
        tokens = []

        # Each parse method responsible for returning position at the next character to be processed
        while (self.code_index < len(self.code)):
            if self.position.char.isnumeric():
                tokens.append(self.parse_numeric())
            elif self.position.char in STRING_DELINEATORS:
                tokens.append(self.parse_string_literal())
            elif self.position.char.isalpha():
                tokens.append(self.parse_variable())
            elif OperatorToken.is_operator_char(self.position.char):
                tokens.append(self.parse_operator())
            elif self.position.char.isspace():
                self.advance()
            else:
                self.advance()
                print(f"Nothing implemented yet for current character ({self.position.char})")

        return tokens

    # Advances forward. Returns true if able to make progress, false otherwise
    def advance(self):
        self.code_index += 1

        if (self.code_index >= len(self.code)):
            print(f"Reached the end of the file (code_index: {self.code_index}), cannot advance (file length: {len(self.code)})")
            return False

        self.position.advance_position(self.code[self.code_index])
        return True

    def parse_numeric(self):
        numeric_string = ''
        while(self.position.char.isnumeric()):
            numeric_string += self.position.char
            self.advance()
        return Token("Int", int(numeric_string))

    def parse_string_literal(self):
        string_literal = ""
        self.advance() # Advance beyond the initial double quote


        # TODO - Handle escaping quotes if we're feeling it
        while(self.position.char not in STRING_DELINEATORS):
            string_literal += self.position.char

            if not self.advance():
                raise Exception("Reached end of file error while looking for terminating string delineator")

        # Advance beyond the last double quote, don't want to start interepeting another string literal
        self.advance()
        return Token("String", string_literal)

    def parse_variable(self):
        variable_literal = ""
        while self.position.char.isalnum():
            variable_literal += self.position.char
            self.advance()

        if ControlToken.is_valid_control_token(variable_literal):
            return Token('Control', variable_literal)
        else:
            return Token('Variable', variable_literal)

    def parse_operator(self):
        string_literal = ''

        while(OperatorToken.is_operator_char(self.position.char)):
            string_literal += self.position.char
            self.advance()

        return Token("Operator", string_literal)
