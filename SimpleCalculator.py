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
        if second_num == 0:
            result = 0







    return result


calculate("add", 100, 0)


print(calculate("add", 100, 0))
