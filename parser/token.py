from .errors import invalid_token_error

TOKEN_TYPES = ['String', 'Int', 'Float', 'Variable', 'Operator']

class Token:
    def __init__(self, type, value):
        if type not in TOKEN_TYPES:
            raise InvalidTokenError(f"Invalid token type ({type}), must be one of {TOKEN_TYPES}")

        self.type = type
        self.value = value
