import unittest

from stringkata.stringcalculator import StringCalculator, IllegalArgumentError


class StringCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = StringCalculator()

    def test_hello_world(self):
        self.assertEqual("hello", "hello", "message not equal")

    def test_given_empty_string_should_return_0(self):
        actual = self.calculator.add("")
        expected = 0
        self.assertEqual(actual, expected)

    def test_given_single_number_should_return_number(self):
        actual = self.calculator.add("1")
        expected = 1
        self.assertEqual(actual, expected)

    def test_given_two_numbers_should_return_sum(self):
        actual = self.calculator.add("1,2")
        expected = 3
        self.assertEqual(actual, expected)

    def test_given_multiple_numbers_should_return_sum(self):
        actual = self.calculator.add("1,2,3,4")
        expected = 10
        self.assertEqual(actual, expected)

    def test_given_numbers_separated_by_comma_or_newline_should_return_sum(self):
        actual = self.calculator.add("1,2\n3,4")
        expected = 10
        self.assertEqual(actual, expected)

    def test_given_numbers_separated_by_custom_delimiter_should_return_sum(self):
        actual = self.calculator.add("//;\n1;2")
        expected = 3
        self.assertEqual(actual, expected)

    def test_given_negative_number_should_throw_exception(self):
        self.assertRaises(IllegalArgumentError, self.calculator.add, "1,2,3,-4")
