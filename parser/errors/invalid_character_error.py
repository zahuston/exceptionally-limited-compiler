class InvalidCharacterError(Exception):
    def __init__(self, message, position = None):
        self.message = message
        self.position = position
