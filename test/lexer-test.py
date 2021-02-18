import unittest
from main.py import Lexer

# https://docs.python.org/3/library/unittest.html
'''
    individual token tests
    - entire number
    - entire string
    combined token tests
    - 5==4
    - print("hello") --> 
    spacing is removed
'''
class TestLexer(unittest.TestCase):
  def multiple_number_input_comes_out_as_1_token(self):
      # arrange
      code = '123'
      # act 
      lexer = Lexer(code)
      actual = lexer.tokenize()
      expected = [Token(TokenType.Num, 123)]
      # assert
      self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()