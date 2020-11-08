from enum import Enum


class Color(Enum):
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    PURPLE = 5
    CYAN = 6
    WHITE = 7


class Style(Enum):
    NONE = 0
    BOLD = 1
    UNDERLINE = 2
    NEGATIVE1 = 3
    NEGATIVE2 = 4


def set_text_style(foreground_color: Color = None, background_color: Color = None, text_style: Style = None):
    if foreground_color is not None:
        print("\033[3{}m".format(foreground_color), end="")
    if background_color is not None:
        print("\033[4{}m".format(background_color), end="")
    if text_style is not None:
        print("\033[{}m".format(text_style), end="")


def reset_text_style():
    print("\033[0m", end="")
