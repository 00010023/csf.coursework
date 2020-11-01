from .intro import intro
from .menu import menu

functions: list[any] = [
    intro, menu
]


def launcher():
    for function in functions:
        function()
    pass
