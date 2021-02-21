# exceptionally-limited-compiler

## Executing the Compiler
Entry point to the project at the moment is compile.py at the top level project directory. The script file itself includes more details, but this lets you read in a specified file, and convert it into tokens. To be extended to parse the tokens, and then translate these to an output language.

## Executing the tests


## Debugging
1. Import `pdb`
2. Add a breakpoint() method call wherever you want to pause execution

## Running Questions
**Q**: Should the Lexer store whitespace? Would think this is the last place you interact with the original file, so it may have to be?
**A**:
