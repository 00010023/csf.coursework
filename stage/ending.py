from .decorator import separators, bye_text

welcome_time = True

text: str = "Thanks for using my application, hope we \n" \
            "will see each other soon again! 00010023 \n"

all_texts: [str] = [
    separators + bye_text + text + separators
]


def ending():
    global welcome_time
    if welcome_time is True:
        for texter in all_texts:
            print(texter)
        welcome_time = False
    else:
        pass
