"""
Copyright to 000010023 by WIUT student
"""


class Colorly:
    HEADER: str = '\033[95m'
    OKBLUE: str = '\033[94m'
    OKCYAN: str = '\033[96m'
    OKGREEN: str = '\033[92m'
    WARNING: str = '\033[93m'
    FAIL: str = '\033[91m'
    ENDC: str = '\033[0m'
    BOLD: str = '\033[1m'
    UNDERLINE: str = '\033[4m'


def error(text: str):
    return Colorly.FAIL + text + Colorly.ENDC


def success(text: str):
    return Colorly.OKGREEN + text + Colorly.ENDC


def warning(text: str):
    return Colorly.WARNING + text + Colorly.ENDC
