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


# you need to implement this function,
# INPUT:    as parameter it should take list of list, see example_list below,
# OUTPUT:   it should return list of calculated values
#    This function should use calculate function on parameters stored in list os lists passed as parameter
def calculate_many_records(list_of_records):
    result_list= []
    for x in list_of_records:
        operation, firstnumb, secondnumb = x
        result_list.append(calculate(operation,firstnumb,secondnumb))
    # somewhere here you should create your implementation
    return result_list

# lines below are another way to look if your code, it is example how this code could be used
# you can also use it to check how it works
example_list = [["add", 0, 100],
                ["subtract", 10, 50],
                ["multiply", 10, 50],
                ["divide", 10, 50]]



print(calculate_many_records(example_list))
