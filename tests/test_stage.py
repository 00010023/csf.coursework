from stage.intro import all_text
from stage.menu import menus, condition, select


def test_intro_stage():
    for text in all_text:
        assert type(text) == str


def test_menu_stage():
    for objects in [menus, condition]:
        assert type(objects) == dict
        for key in objects.keys():
            assert type(key) == int
    assert select(1) == print()
