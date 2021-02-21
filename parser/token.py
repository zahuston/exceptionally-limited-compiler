from .errors.invalid_token_error import InvalidTokenError
from enum import Enum


CONTROL_TOKENS = ['if', 'elif', 'else', 'for', 'while', 'in', 'or', 'and']
OPERATOR_CHARACTERS = ['=', '>', '<', '+', '-' '(', ')']

TOKEN_TYPES = ['String', 'Int', 'Float', 'Variable', 'Operator', 'Control']

class Token:
    def __init__(self, type, value = None):
        if type not in TOKEN_TYPES:
            raise InvalidTokenError(f"Invalid token type ({type}), must be one of {TOKEN_TYPES}")

        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token(type={self.type}, value = {self.value})'


class ControlToken(Token):
    @staticmethod
    def is_valid_control_token(token_value):
        return token_value in CONTROL_TOKENS

class OperatorToken(Token):
    @staticmethod
    def is_valid_operator_token(token_value):
        return token_value in OPERATOR_CHARACTERS
