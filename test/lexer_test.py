import unittest   # The test framework
import sys

sys.path.append('../src')

from parser.lexer import Lexer
from parser.token_jz import Token
'''
    individual token tests
    - entire number
    - entire string
    combined token tests
    - 5==4
    - print("hello") -->
    spacing is removed
'''
class Test_Lexer(unittest.TestCase):
    # Basic String Tests
    def test_single_character_string_comes_out_as_1_token(self):
        actual = Lexer(""""a"\n""").tokenize()
        expected = [Token(type="String", value = "a")]
        self.assertListEqual(actual, expected)

    def test_multiple_character_string_comes_out_as_1_token(self):
        actual = Lexer(""""abc"\n""").tokenize()
        expected = [Token(type="String", value = "abc")]
        self.assertListEqual(actual, expected)

    def test_space_within_string_comes_out_as_1_token(self):
        actual = Lexer(""""abc xyz"\n""").tokenize()
        expected = [Token(type="String", value = "abc xyz")]
        self.assertListEqual(actual, expected)

    def test_multiple_string_inputs_comes_out_as_2_token(self):
        actual = Lexer(""""abc" "xyz"\n""").tokenize()
        expected = [Token(type="String", value = "abc"), Token(type="String", value = "xyz")]
        self.assertListEqual(actual, expected)

    # Basic Int Tests
    def test_single_int_comes_out_as_1_token(self):
        actual = Lexer("""1\n""").tokenize()
        expected = [Token(type="Int", value = 1)]
        self.assertListEqual(actual, expected)

    def test_multiple_int_comes_out_as_2_token(self):
        actual = Lexer("""1 2\n""").tokenize()
        expected = [Token(type="Int", value = 1), Token(type="Int", value = 2)]
        self.assertListEqual(actual, expected)

    # Basic Float Tests
    def test_single_float_comes_out_as_1_token(self):
        actual = Lexer("""1.9\n""").tokenize()
        expected = [Token(type="Float", value = 1.9)]
        self.assertListEqual(actual, expected)

    def test_multiple_float_comes_out_as_2_token(self):
        actual = Lexer("""1.9 2.5\n""").tokenize()
        expected = [Token(type="Float", value = 1.9), Token(type="Float", value = 2.5)]
        self.assertListEqual(actual, expected)

    def test_no_infinite_floating_on(self):
        with self.assertRaises(Exception):
            Lexer("""1.9.1.3\n""").tokenize()

    # Basic Variable Tests
    def test_single_variable_comes_out_as_1_token(self):
        actual = Lexer("""testVariable\n""").tokenize()
        expected = [Token(type="Variable", value = "testVariable")]
        self.assertListEqual(actual, expected)

    def test_multiple_variable_comes_out_as_2_token(self):
        actual = Lexer("""testVariableA testVariableB\n""").tokenize()
        expected = [Token(type="Variable", value = "testVariableA"), Token(type="Variable", value = "testVariableB")]
        self.assertListEqual(actual, expected)

    # variables
    def test_single_alphanumeric_variables(self):
        actual = Lexer("""testVariable1\n""").tokenize()
        expected = [Token(type="Variable", value = "testVariable1")]
        self.assertListEqual(actual, expected)

    # Basic Operator Tests
    def test_single_operator_comes_out_as_1_token(self):
        actual = Lexer("""+\n""").tokenize()
        expected = [Token(type="Operator", value = "+")]
        self.assertListEqual(actual, expected)

    def test_multiple_operator_comes_out_as_2_token(self):
        actual = Lexer("""+ -\n""").tokenize()
        expected = [Token(type="Operator", value = "+"), Token(type="Operator", value = "-")]
        self.assertListEqual(actual, expected)

    # Basic Operator Tests
    def test_single_control_comes_out_as_1_token(self):
        actual = Lexer("""if\n""").tokenize()
        expected = [Token(type="Control", value = "if")]
        self.assertListEqual(actual, expected)

    def test_multiple_control_comes_out_as_2_token(self):
        actual = Lexer("""if else\n""").tokenize()
        expected = [Token(type="Control", value = "if"), Token(type="Control", value = "else")]
        self.assertListEqual(actual, expected)

    def test_all_possible_controls(self):
        actual = Lexer("""if elif else for while in or and\n""").tokenize()
        expected = [Token(type="Control", value="if"),
                    Token(type="Control", value="elif"),
                    Token(type="Control", value="else"),
                    Token(type="Control", value="for"),
                    Token(type="Control", value="while"),
                    Token(type="Control", value="in"),
                    Token(type="Control", value="or"),
                    Token(type="Control", value="and")]
        self.assertListEqual(actual, expected)

    # Invalid Characters
    def test_invalid_characters_create_errors(self):
        actual = Lexer("""&$#\n""").tokenize()
        expected = [Token(type="Operator", value = "+"), Token(type="Operator", value = "-")]
        # Todo: consider how we'd handle a non-alphanumeric non-keyword character
        self.assertEqual(True, False)

    # WhiteSpace
    def test_multiple_spaces_between_tokens_are_removed(self):
        actual = Lexer("""1    3\n""").tokenize()
        expected = [Token(type="Int", value = 1), Token(type="Int", value = 3)]
        self.assertEqual(actual, expected)

    def test_tabs_between_tokens_are_removed(self):
        actual = Lexer("""1\t\t3\n""").tokenize()
        expected = [Token(type="Int", value = 1), Token(type="Int", value = 3)]
        self.assertEqual(actual, expected)

    def test_newlines_between_tokens_are_removed(self): #???
        actual = Lexer("""1
        3\n""").tokenize()
        expected = [Token(type="Int", value = 1), Token(type="Int", value = 3)]
        self.assertEqual(actual, expected)

    def test_assorted_space_characters_between_tokens_are_removed(self):
        actual = Lexer("""  1
        3\t5
        \n""").tokenize()
        expected = [Token(type="Int", value = 1), Token(type="Int", value = 3), Token(type="Int", value = 5)]
        self.assertEqual(actual, expected)

    # Happy Path Common Cases
    def test_arithmetic_expression(self):
        actual = Lexer("""5+7\n""").tokenize()
        expected = [Token(type="Int", value = 5), Token(type="Operator", value = "+"), Token(type="Int", value = 7)]
        self.assertEqual(actual, expected)

    def test_arithmetic_assignment_expression(self):
        actual = Lexer("""testVar = 5 + 7\n""").tokenize()
        expected = [Token(type="Variable", value = "testVar"),
                    Token(type="Operator", value = "="),
                    Token(type="Int", value = 5),
                    Token(type="Operator", value = "+"),
                    Token(type="Int", value = 7)]
        self.assertEqual(actual, expected)

    def test_method_call(self):
        actual = Lexer("""print("hello world")\n""").tokenize()
        expected = [Token(type="Variable", value = "print"),
                    Token(type="Operator", value = "("),
                    Token(type="string", value = "hello world"),
                    Token(type="Operator", value = ")")]
        self.assertEqual(actual, expected)

    def test_conditional_expression(self):
        actual = Lexer("""
        if 5==5:
            v = 5\n""").tokenize()
        expected = [Token(type="Control", value = "if"),
                    Token(type="Int", value = 5),
                    Token(type="Operator", value = "=="),
                    Token(type="Int", value = 5),
                    Token(type="Operator", value = ":"),
                    Token(type="Variable", value = "v"),
                    Token(type="Operator", value = "="),
                    Token(type="Int", value = 5)]
        self.assertEqual(actual, expected)

    def test_conditional_expression(self):
        # Todo: should this throw an error?
        actual = Lexer("""
        if5==5:
            v = 5\n""").tokenize()
        expected = [Token(type="Control", value = "if"),
                    Token(type="Int", value = 5),
                    Token(type="Operator", value = "=="),
                    Token(type="Int", value = 5),
                    Token(type="Operator", value = ":"),
                    Token(type="Variable", value = "v"),
                    Token(type="Operator", value = "="),
                    Token(type="Int", value = 5)]
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
