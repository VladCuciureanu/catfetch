import os
import sys

if sys.platform in ['win32', 'cygwin']:
    os.system("color")

from term_color_util.term_color_util import set_text_style, reset_text_style
