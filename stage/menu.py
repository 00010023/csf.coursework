import list
import tuple
import dictionary

from .decorator import separators

menus: dict[int: str] = {
    1: "1. List Case",
    2: "2. Tuple Case",
    3: "3. Dictionary Case",
    4: "4. Exit Application"
}

condition: dict[int: str] = {
    1: list.launcher,
    2: tuple.launcher,
    3: dictionary.launcher,
    4: exit
}


def input_choice():
    selection = input("Choose your option from menu below: ")
    select(int(selection))


def select(number: int):
    if 0 < number < 5:
        condition[number]()
    else:
        print("Invalid option, try again!")
        input_choice()


def menu():
    print(separators)
    for choice in menus.values():
        print(choice)
    print("\n" + "=" * 44)
    input_choice()
