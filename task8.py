"""
This is the application that was
created to fulfill WIUT's requirements

Copyright to 000010023 by WIUT student
"""

a = 5
b = 10


def exampleReturn(first_number, second_number):  # <- can take argument
    result = first_number + second_number  # <- has ability to initiate inline variable
    return result  # <- return a specific value, so it can be passed as argument on another function
    pass  # <- ending function here


def exampleVoid(first_number, second_number):  # <- can take argument
    result = first_number + second_number  # <- has ability to initiate inline variable
    print(result)  # <- does everything on inline mode and doesn't return something
    pass  # <- ending function here that does something without returning some value


if __name__ == '__main__':
    exampleVoid(exampleReturn(a, b), b)
    pass
