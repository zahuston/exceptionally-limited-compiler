'''
  lexer goal take syntax --> tokens
  if 5==4:
    print("hello")
  [if, num:5, comp_eql, num:4, func(print), quote_start, string:hello, quote_end]  
  todo
  - identify token types
  - write lexer function to convert
  ? 
'''

from enum import Enum

class TokenType(Enum):
  Num,
  Control,
  


class Token():
  def __init__(self, type, value):
    self.type = type
    self.value = value
  

# todo: expand to consume code text from a file
class Lexer():
  def __init__(self, code)
    self.code = code
  
  def tokenize(): 
    tokenList = []
    errors = []
    # evaluate code and create tokens list
    # ?is it at this point that the lexer pulls in other files?
    return tokenList, errors

