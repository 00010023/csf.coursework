from .decorator import separators, welcome_text



intro_text: str = "Welcome to my tutorial application by 10023 \n" \
                  "In this application I'll be introducing \n" \
                  "basic concepts of lists, tuples, dictionary \n" \
                  "and some functions as ... \n"

all_text: list[str] = [
    separators + welcome_text + separators,
    separators + intro_text + separators
]


def intro():
    for texter in all_text:
        print(texter)
