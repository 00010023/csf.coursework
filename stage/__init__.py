from .intro import intro
from .menu import menu
from .ending import ending

functions: list[any] = [
    intro, menu, ending
]


def launcher():
    for function in functions:
        function()
    pass
