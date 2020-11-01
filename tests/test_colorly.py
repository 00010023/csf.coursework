import colorly


def test_colorly():
    for color in vars(colorly.Colorly):
        assert type(color) == str
