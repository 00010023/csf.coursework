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

    def error(self: str):
        return Colorly.FAIL + self + Colorly.ENDC

    def success(self: str):
        return Colorly.OKGREEN + self + Colorly.ENDC

    def warning(self: str):
        return Colorly.WARNING + self + Colorly.ENDC
