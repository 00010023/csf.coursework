separators: str = "=" * 44 + "\n"

welcome_big_text: str = \
    """ _       __     __
| |     / /__  / /________  ____ ___  ___
| | /| / / _ \\/ / ___/ __ \\/ __ `__ \\/ _ \\
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/
|__/|__/\\___/_/\\___/\\____/_/ /_/ /_/\\___/
"""

intro_text: str = "Welcome to my tutorial application by 10023 \n" \
                  "In this application I'll be introducing \n" \
                  "basic concepts of lists, tuples, dictionary \n" \
                  "and some functions as ... \n"

all_text: list[str] = [
    separators + welcome_big_text + separators,
    separators + intro_text + separators
]


def intro():
    for texter in all_text:
        print(texter)
