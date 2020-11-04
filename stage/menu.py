"""
Copyright to 000010023 by WIUT student
"""

import list
import tuple
import dictionary

from .decorator import separators
from colorly import Colorly
from .ending import ending

menus: dict[int: dict] = {
    1: {
        "name": "1. List Case",
        "func": list.launcher
    },
    2: {
        "name": "2. Tuple Case",
        "func": tuple.launcher
    },
    3: {
        "name": "3. Dictionary Case",
        "func": dictionary.launcher
    },
    4: {
        "name": "4. Exit Application",
        "func": ending
    }
}


def input_choice():
    selection = input("Choose your option from menu below: ")
    try:
        select(int(float(selection)))
    except ValueError:
        errored()
    except Exception:
        errored()


def select(number: int):
    if 0 < number < 5:
        menus[number]["func"]()
    else:
        errored()


def errored(isFailed=True):
    if isFailed:
        print("Invalid option, try again!")
        input_choice()
    else:
        input_choice()


def menu():
    print(separators)
    for choice in menus.values():
        print(choice["name"])
    print(Colorly.warning("\n" + "=" * 44))
    errored(False)
