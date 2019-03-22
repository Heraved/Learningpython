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


# this function was created by me, it will return True if it is number, otherwise False
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# TODO implement this function, it should take as input string about, what you want to do, something like:
# TODO "add 7 to 9", and then it should parse string that was passed to console, and call on it function calculate
# TODO it should only work for 2 numbers, 3 or more numbers shouldn't be possible with this function,
# TODO it should be possible to pass many operations ex. "add subtract 7 9", and it should calculate all required
# TODO operations for this input. Results should always be returned as list, for one operation it would be 1 element
# TODO list, but if there are more operations then list will be longer
# TODO to solve it you might want to use function is_member(value) that I already implemented for you, it should
# TODO return True if value is number and return False otherwise
# TODO Also check split function, it is function for strings, it is possible to you this function to split sentence into
# TODO many words
def calculate_with_string_input():
    sentence = input("What do you want to calculate: ")
    # TODO here should be implementation
    ret_list = []
    return ret_list


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
    average = sum(values) / len(values)
    # TODO  here should be your implementation
    return average



# TODO this function should take list of values,
# then returns sorted list in ascending(normal) or descending(reverse" order
def sort_values(values, order="normal"):
     # TODO  here should be your implementation
    return values


# above lines should only be used to write definitions of functions
# from here is main function where you can call your functions


list_of_values = [1,5,2,4]

if __name__ == '__main__':
    print(calculate_average(list_of_values))
