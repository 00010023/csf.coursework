"""
This is the application that was
created to fulfill WIUT's requirements

Copyright to 000010023 by WIUT student
"""

a = 5
b = 10


def calculator(first_number, second_number, operator):
    if operator == "+" or operator == "add":
        print(f"{first_number} + {second_number} is", first_number + second_number)
    elif operator == "-" or operator == "subtract":
        print(f"{first_number} - {second_number} is", first_number - second_number)
    elif operator == "*" or operator == "multiply":
        print(f"{first_number} * {second_number} is", first_number * second_number)
    elif operator == "/" or operator == "divide":
        print(f"{first_number} / {second_number} is", first_number / second_number)
    else:
        print("Invalid operator!")
    pass


class Calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def addition(self):
        print(f"The addition of {self.first_number} and {self.second_number} is:",
              self.first_number + self.second_number)

    def subtraction(self):
        print(f"The addition of {self.first_number} and {self.second_number} is:",
              self.first_number - self.second_number)

    def multiplication(self):
        print(f"The addition of {self.first_number} and {self.second_number} is:",
              self.first_number * self.second_number)

    def division(self):
        print(f"The addition of {self.first_number} and {self.second_number} is:",
              self.first_number / self.second_number)

    def is_greater_or_not(self):
        if self.first_number > self.second_number:
            print(f"The number {self.first_number} is greater than {self.second_number}")
        elif self.first_number < self.second_number:
            print(f"The number {self.first_number} is less than {self.second_number}")
        elif self.first_number == self.second_number:
            print(f"The number {self.first_number} is equal to {self.second_number}")


if __name__ == '__main__':
    try:

        # Class usage
        process = Calculator(a, b)
        process.addition()
        process.subtraction()
        process.multiplication()
        process.is_greater_or_not()

        # Function usage
        calculator(a, b, "+")

    except Exception as error:
        print(f"Error occurred: {error}")
    pass
