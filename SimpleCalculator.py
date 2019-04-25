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

# TODO this function should take to parameters:
# TODO input_file_name - name of the file that contains operations
# TODO result_file_name - name_of_file where we want to save results of operations
# TODO if there is no result_file_name then it should create this new file with such name
# TODO this function can use calculate function or other functions you created before
# TODO this function has no return it only writes to file
def calculate_from_file(input_file_name, result_file_name):
    pass


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

def find_with_index(elems, value):
    try:
        elems.index(value)
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
    sentence = input("What do you want to calculate: ").split( )
    ret_list = []
    possible_operations = ['add', 'subtract', 'multiply', 'divide']
    operations_to_execute = []
    numbers = []

    for x in sentence:
        if find_with_index(possible_operations,x):
            operations_to_execute.append(x)
        if is_number(x):
            numbers.append(x)
    first_num = numbers[0]
    second_num = numbers[1]

    for y in operations_to_execute:
        operation = y
        score = calculate(operation,float(first_num),float(second_num))
        ret_list.append(score)

    return ret_list


def find_min_value(values):
    min_value = 0
    for x in values:
        if x < min_value:
            min_value = x
    return min_value


def find_max_value(values):
    max_value = 0
    for x in values:
        if x > max_value:
            max_value = x
    return max_value


#def calculate_from_file(input_file_name, result_file_name):
    f = open('input_data.txt', 'r')
    print(f)




def calculate_average(values):
    average = 0
    average = sum(values) / len(values)
    return average


# then returns sorted list in ascending(normal) or descending(reverse" order
def sort_values(values, order='normal'):
    if order == "normal":
        sort_values_normal(values)
    elif order == "reverse":
        sort_values_reverse(values)
    return values


def switch_values(left, right):
    temp = left
    left = right
    right = temp
    return left, right


# this function sorts in ascending order
def sort_values_normal(values):
    for x in range(len(values)):
        for i in range(len(values)-1):
            if values[i] > values[i+1]:
                values[i], values[i+1] = switch_values(values[i], values[i+1])


# this function sorts descending order
def sort_values_reverse(values):
    for x in range(len(values)):
        for i in range(len(values)-1):
            if values[i] < values[i+1]:
                values[i], values[i + 1] = switch_values(values[i], values[i + 1])


# above lines should only be used to write definitions of functions
# from here is main function where you can call your functions


if __name__ == '__main__':
    list_of_values = [1, 5, 2, 4, 6, 3]


