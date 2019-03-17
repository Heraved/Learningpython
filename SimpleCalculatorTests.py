import io
import unittest
from unittest.mock import patch

from SimpleCalculator import *


class TestAddOperation(unittest.TestCase):

    def test_add_two_zeros(self):
        self.assertEqual(0, calculate("add", 0, 0))

    def test_add_zero_to_value(self):
        self.assertEqual(100, calculate("add", 100, 0))

    def test_add_two_ints(self):
        self.assertEqual(101, calculate("add", 100, 1))

    def test_add_minus_int(self):
        self.assertEqual(-1, calculate("add", 100, -101))

    def test_add_two_floats(self):
        self.assertEqual(7.1, calculate("add", 3.5, 3.6))

    def test_add_float_to_int(self):
        self.assertEqual(10.5, calculate("add", 7, 3.5))


class TestSubtractOperation(unittest.TestCase):

    def test_subtract_two_zeros(self):
        self.assertEqual(0, calculate("subtract", 0, 0))

    def test_subtract_smaller_value(self):
        self.assertEqual(99, calculate("subtract", 100, 1))

    def test_subtract_bigger_value(self):
        self.assertEqual(-99, calculate("subtract", 1, 100))

    def test_subtract_minus_value(self):
        self.assertEqual(201, calculate("subtract", 100, -101))

    def test_subtract_from_minus_value(self):
        self.assertEqual(-60, calculate("subtract", -10, 50))

    def test_subtract_float_from_int(self):
        self.assertEqual(3.5, calculate("subtract", 7, 3.5))


class TestMultiplyOperation(unittest.TestCase):

    def test_multiply_two_zeros(self):
        self.assertEqual(0, calculate("multiply", 0, 0))

    def test_multiply_plus_values(self):
        self.assertEqual(100, calculate("multiply", 100, 1))

    def test_multiply_one_minus_value(self):
        self.assertEqual(-100, calculate("multiply", 1, -100))

    def test_multiply_two_minus_value(self):
        self.assertEqual(200, calculate("multiply", -100, -2))

    def test_multiply_float_with_int(self):
        self.assertAlmostEqual(24.5, calculate("multiply", 7, 3.5))

    def test_multiply_two_floats(self):
        self.assertAlmostEqual(14.7, calculate("multiply", 4.2, 3.5))


class TestDivideOperation(unittest.TestCase):

    def test_divide_by_zeros(self):
        self.assertEqual(0, calculate("divide", 100, 0))

    def test_divide_two_zeros(self):
        self.assertEqual(0, calculate("divide", 0, 0))

    def test_divide_plus_values(self):
        self.assertEqual(50, calculate("divide", 100, 2))

    def test_divide_one_minus_value(self):
        self.assertEqual(-2, calculate("divide", 100, -50))

    def test_divide_two_minus_value(self):
        self.assertEqual(50, calculate("divide", -100, -2))

    def test_divide_float_with_int(self):
        self.assertAlmostEqual(2, calculate("divide", 7, 3.5))

    def test_divide_two_floats(self):
        self.assertAlmostEqual(1.2, calculate("divide", 4.2, 3.5))


class TestCalculateManyRecords(unittest.TestCase):

    def test_calculate_many_records(self):
        input_list = [["add", 0, 101],
                      ["add", 2, 101],
                      ["subtract", 10, 50],
                      ["subtract", 20, 10],
                      ["multiply", 10, 5],
                      ["multiply", 3, 0],
                      ["divide", 10, 50],
                      ["divide", 10, 0]]

        output_list = [101, 103, -40, 10, 50, 0, 0.2, 0]

        self.assertEqual(output_list, calculate_many_records(input_list))


class TestInput(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["add", 5, 6])
    def test_input_add_operation(self, input, mock_stdout):
        calculate_with_input()
        self.assertEqual("The result is: 11\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["subtract", 5, 6])
    def test_input_subtract_operation(self, input, mock_stdout):
        calculate_with_input()
        self.assertEqual("The result is: -1\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["multiply", 5, 6])
    def test_input_multiply_operation(self, input, mock_stdout):
        calculate_with_input()
        self.assertEqual("The result is: 30\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["divide", 12, 6])
    def test_input_divide_operation(self, input, mock_stdout):
        calculate_with_input()
        self.assertEqual("The result is: 2.0\n", mock_stdout.getvalue())


class TestFindMinMaxValue(unittest.TestCase):
    def __init__(self, unit_test):
        super().__init__(unit_test)
        self.values = [100, -2, 33, -400, 1000]

    def test_find_min_value(self):
        self.assertEqual(-400, find_min_value(self.values))

    def test_find_max_value(self):
        self.assertEqual(1000, find_max_value(self.values))


class TestAverageValue(unittest.TestCase):

    def test_average(self):
        values = [100, 50, 200, 50]
        self.assertEqual(100, calculate_average(values))


class TestSortingFunction(unittest.TestCase):

    def test_sorting_ascending(self):
        values = [2, 1, 3, 7, 10, 5, 4]
        copy_of_values = values.copy()
        self.assertEqual(sorted(copy_of_values), sort_values(values))

    def test_sorting_descending(self):
        values = [2, 1, 3, 7, 10, 5, 4]
        copy_of_values = values.copy()
        self.assertEqual(sorted(copy_of_values, reverse=True), sort_values(values, "reverse"))

    def test_sorting_incorrect_order(self):
        values = [2, 1, 3, 7, 10, 5, 4]
        copy_of_values = values.copy()
        self.assertEqual(copy_of_values, sort_values(values, "fast"))


class TestStringInput(unittest.TestCase):

    @patch('builtins.input', side_effect=["add 7 to 9"])
    def test_input_one_operation(self, input):
        expected_list = [16.0]
        self.assertEqual(expected_list, calculate_with_string_input())

    @patch('builtins.input', side_effect=["add multiply subtract divide 20 -2.5"])
    def test_input_many_operations(self, input):
        expected_list = [17.5, -50.0, 22.5, -8.0]
        self.assertEqual(expected_list, calculate_with_string_input())

    @patch('builtins.input', side_effect=["20 -2.5"])
    def test_input_no_operations(self, input):
        expected_list = []
        self.assertEqual(expected_list, calculate_with_string_input())


if __name__ == '__main__':
    unittest.main()
