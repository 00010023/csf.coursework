import list
import tuple
import dictionary

from .intro import separators

menus: dict[int: str] = {
    1: "1. List Case",
    2: "2. Tuple Case",
    3: "3. Dictionary Case",
}

condition: dict[int: str] = {
    1: list.launcher,
    2: tuple.launcher,
    3: dictionary.launcher
}


def select(number: int):
    condition[number]()


def menu():
    print(separators)
    for choice in menus.values():
        print(choice)
    print("\n" + "=" * 44)
    selection = input("Choose your option from menu below: ")
    select(int(selection))
