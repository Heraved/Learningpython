def calculate(operation, first_num, second_num):
    result = 0
    if operation == "add":
        result = first_num + second_num

    elif operation == "subtract":
        result = first_num - second_num

    elif operation == "multiply":
        result = first_num * second_num

    elif operation == "divide":
        if second_num != 0:
            result = first_num / second_num

    return result


def calculate_many_records(list_of_records):
    result_list = []
    for x in list_of_records:
        operation, first_numb, second_numb = x
        result_list.append(calculate(operation, first_numb, second_numb))
    return result_list


def calculate_with_input():
    operation = input('Choose operation:\nadd\nsubtract\nmultiply\ndivide\n')
    first_numb = int(input('First number:\n'))
    second_numb = int(input('Second number:\n'))
    result = calculate(operation, first_numb, second_numb)
    
    print("The result is:", result)

    return result


# TODO this function should take list of values, then return value with smallest value
def find_min_value(values):
    min_value = 0
    # TODO  here should be your implementation
    return min_value


# TODO this function should take list of values, then return value with biggest value
def find_max_value(values):
    max_value = 0
    # TODO  here should be your implementation
    return max_value


# TODO this function should take list of values, then return average of those values
def calculate_average(values):
    average = 0
    # TODO  here should be your implementation
    return average


# TODO this function should take list of values,
# then returns sorted list in ascending(normal) or descending(reverse" order
def sort_values(values, order="normal"):
    # TODO  here should be your implementation
    return values


# above lines should only be used to write definitions of functions
# from here is main function where you can call your functions
if __name__ == '__main__':
    values = [1, 3, 5, 2, 10]
    sort_values(values)
    print(values)
