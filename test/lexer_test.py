import unittest   # The test framework
from parser.lexer import Lexer
from parser.token import Token

class Test_Lexer(unittest.TestCase):
    def test_multiple_number_with_space_input_comes_out_as_1_token(self):
        # arrange
        code = '123 '
        # act
        lexer = Lexer(code)
        actual = lexer.tokenize()
        expected = [Token(type='Int', value = 123)]
        # assert
        self.assertEqual(actual, expected)

    '''
        get's stuck in infinite loop and breaks testing.
    '''
    def test_multiple_number_input_comes_out_as_1_token(self):
        # arrange
        code = '123\n'
        # act
        lexer = Lexer(code)
        actual = lexer.tokenize()
        expected = [Token(type='Int', value = 123)]
        # assert
        self.assertEqual(actual, expected)

    def lexer__no_new_line__raises_error(self):
        # arrange
        code = '123'
        # act
        lexer = Lexer(code)

        actual = lexer.tokenize()
        expected = [Token(type='Int', value = 123)]
        # assert
        self.assertRaises(Exception, lexer.tokenize())



if __name__ == '__main__':
    unittest.main()
