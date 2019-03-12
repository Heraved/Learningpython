import unittest

# Input:
#    - operation - string value specifying operation, e.g.: add, subtract, divide, multiply
#    - first_num - value of first number
#    - second_num - value of second number
# Output:
#    - function should return result of operation

def calculate(operation, first_num, second_num):
    if operation == "add":
        result = first_num + second_num

    elif operation == "subtract":
        result = first_num - second_num

    elif operation == "multiply":
        result = first_num * second_num

    elif operation == "divide":
        result = first_num  / second_num

    else :
        result = 0


    return









class TestAddOperation(unittest.TestCase):

    def test_add_two_zeros(self):
        self.assertEqual(calculate("add", 0, 0), 0)

    def test_add_two_ints(self):
        self.assertEqual(calculate("add", 100, 1), 101)

    def test_add_minus_int(self):
        self.assertEqual(calculate("add", 100, -101), -1)

    def test_add_two_floats(self):
        self.assertEqual(calculate("add", 3.5, 3.6), 7.1)

    def test_add_float_to_int(self):
        self.assertEqual(calculate("add", 7, 3.5), 10.5)


class TestSubtractOperation(unittest.TestCase):

    def test_subtract_two_zeros(self):
        self.assertEqual(calculate("subtract", 0, 0), 0)

    def test_subtract_smaller_value(self):
        self.assertEqual(calculate("subtract", 100, 1), 99)

    def test_subtract_bigger_value(self):
        self.assertEqual(calculate("subtract", 1, 100), -99)

    def test_subtract_minus_value(self):
        self.assertEqual(calculate("subtract", 100, -101), 201)

    def test_subtract_from_minus_value(self):
        self.assertEqual(calculate("subtract", -10, 50), -60)

    def test_subtract_float_from_int(self):
        self.assertEqual(calculate("subtract", 7, 3.5), 3.5)


class TestMultiplyOperation(unittest.TestCase):

    def test_multiply_two_zeros(self):
        self.assertEqual(calculate("multiply", 0, 0), 0)

    def test_multiply_plus_values(self):
        self.assertEqual(calculate("multiply", 100, 1), 100)

    def test_multiply_one_minus_value(self):
        self.assertEqual(calculate("multiply", 1, -100), -100)

    def test_multiply_two_minus_value(self):
        self.assertEqual(calculate("multiply", -100, -2), 200)

    def test_multiply_float_with_int(self):
        self.assertAlmostEqual(calculate("multiply", 7, 3.5), 24.5)

    def test_multiply_two_floats(self):
        self.assertAlmostEqual(calculate("multiply", 4.2, 3.5), 14.7)


class TestDivideOperation(unittest.TestCase):

    def test_divide_by_zeros(self):
        self.assertEqual(calculate("divide", 100, 0), 0)

    def test_divide_two_zeros(self):
        self.assertEqual(calculate("divide", 0, 0), 0)

    def test_divide_plus_values(self):
        self.assertEqual(calculate("divide", 100, 2), 50)

    def test_divide_one_minus_value(self):
        self.assertEqual(calculate("divide", 100, -50), -2)

    def test_divide_two_minus_value(self):
        self.assertEqual(calculate("divide", -100, -2), 50)

    def test_divide_float_with_int(self):
        self.assertAlmostEqual(calculate("divide", 7, 3.5), 2)

    def test_divide_two_floats(self):
        self.assertAlmostEqual(calculate("divide", 4.2, 3.5), 1.2)


if __name__ == '__main__':
    unittest.main()

