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
    result_list=  []
    for x in list_of_records :
        operation, firstnumb, secondnumb = x
        result_list.append(calculate(operation, firstnumb,secondnumb))
    # somewhere here you should create your implementation
    return result_list


def calculate_with_input() :
    operation = input('Choose operation:\nadd\nsubtract\nmultiply\ndivide\n')
    first_numb = int(input('First number:\n'))
    second_numb = int(input('Second number:\n'))
    result = calculate(operation,first_numb,second_numb)
    
    print ("The result is:",result)

    return result


# above lines should only be used to write definitions of functions
# from here is main function where you can call your functions
if __name__ == '__main__':
    calculate_with_input()
