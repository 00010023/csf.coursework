separators = "=" * 44 + "\n"

welcome_big_text = \
    """ _       __     __
| |     / /__  / /________  ____ ___  ___
| | /| / / _ \\/ / ___/ __ \\/ __ `__ \\/ _ \\
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/
|__/|__/\\___/_/\\___/\\____/_/ /_/ /_/\\___/
"""

intro_text = "Welcome to my tutorial application by 00010023 \n" \
             "In this application I'll be introducing \n" \
             "basic concepts of lists, tuples, dictionary \n" \
             "and some functions as ..."

all_text = [
    separators + welcome_big_text + separators,
    intro_text
]


def launcher():
    for texter in all_text:
        print(texter)
    pass
