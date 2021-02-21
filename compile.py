import argparse # https://docs.python.org/3/library/argparse.html
import pdb
import sys

from parser.lexer import Lexer

print('Parsing command line arguments')
parser = argparse.ArgumentParser(description='Compile source starting at the input file into TBD output')
parser.add_argument('source_file', help='the source file in the J&Z limited liability language')
parsed_args = parser.parse_args()

print(parsed_args)

with open(parsed_args.source_file, 'r') as source_file:
    source_code = source_file.read()
    lexer = Lexer(source_code)

    tokens = lexer.tokenize()

    print(f"Look at all of our tokens: {tokens}")
