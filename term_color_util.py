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

def set_text_style(foreground_color: Color, background_color: Color, textstyle: Style):
    print("\033[{};3{};4{}m".format(textstyle,foreground_color,background_color), end="")

def get_text_style(foreground_color: Color, background_color: Color, textstyle: Style):
    return "\033[{};3{};4{}m".format(textstyle,foreground_color,background_color)

def reset_text_style():
    print("\033[0m")