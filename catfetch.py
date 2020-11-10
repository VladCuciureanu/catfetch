import sys
from term_color_util import set_text_style, reset_text_style
from system_info_service import SystemInfoService

# Calculating terminal width
column_count = SystemInfoService.get_terminal_width()

# Clear terminal
print("\033[H\033[J")

# Print user and hostname
set_text_style(7)
print(SystemInfoService.get_username(), end="")
set_text_style(5)
print(" @ ", end="")
set_text_style(7)
print(SystemInfoService.get_hostname())

# Print separator
set_text_style(1)
for _ in range(column_count // 2):
    print("~ ", end="")
print("\n")
reset_text_style()

# Load ASCII file
ascii_file = list(map(lambda x: x.replace("\n", ""), open("cat.ascii", "r").readlines()))
max_line_length = -1
for line in ascii_file:
    max_line_length = max(len(line), max_line_length)

# Load info into string list
sys_header_list = ["OS", "Kernel", "Terminal", "DE / WM", "Hardware", "CPU", "GPU", "Memory", "Uptime"]
sys_value_list = [
    SystemInfoService.get_os(),
    SystemInfoService.get_kernel(),
    SystemInfoService.get_terminal(),
    SystemInfoService.get_de_wm(),
    SystemInfoService.get_hardware(),
    SystemInfoService.get_cpu(),
    SystemInfoService.get_gpu(),
    "{} MB / {} MB".format(SystemInfoService.get_used_memory(), SystemInfoService.get_total_memory()),
    SystemInfoService.get_uptime(),
]

# Calculate info offset
sys_offset = 0
if len(ascii_file) > len(sys_header_list):
    sys_offset = int((len(ascii_file) - len(sys_header_list)) // 2)

# Print drawing and info side by side
for _ in range(0, max(len(ascii_file), len(sys_header_list))):
    try:
        set_text_style(5)
        print(('{:' + str(max_line_length + 4) + 's}').format(ascii_file[_]), end="")
    except IndexError:
        print(str.ljust("", max_line_length + 4), end="")
    try:
        if _ - sys_offset >= 0:
            set_text_style(2)
            print(str.ljust(sys_header_list[_ - sys_offset], 8), end="  >>  ")
            set_text_style(3)
            print(str.ljust(sys_value_list[_ - sys_offset][0:column_count - max_line_length - 18],
                            column_count - max_line_length - 18))
        else:
            print()
    except IndexError:
        print()

# New line for cleanliness
print()

# Setting some variables
symbol = "⚞^..^⚟"
offset = (column_count - len(symbol) * 7) / 7 - 2

# Check if terminal supports unicode
try:
    '╔═╗║╚═╝'.encode(sys.stdout.encoding)
except UnicodeEncodeError:
    print("Notice: Current terminal doesn't support unicode so the color boxes won't be displayed.")
    exit()

# Print top boxes
for _ in range(int(offset // 2)):
    print(' ', end='')
for _ in range(1, 8):
    set_text_style(_)
    print('╔', end='')
    for i in range(len(symbol)):
        print('═', end='')
    print('╗', end='')
    if _ < 7:
        for _ in range(int(offset)):
            print(' ', end='')
print()

# Print middle boxes
for _ in range(int(offset // 2)):
    print(' ', end='')
for _ in range(1, 8):
    set_text_style(_)
    print('║', end='')
    print(symbol, end='')
    print('║', end='')
    if _ < 7:
        for _ in range(int(offset)):
            print(' ', end='')
print()

# Print bottom boxes
for _ in range(int(offset // 2)):
    print(' ', end='')
for _ in range(1, 8):
    set_text_style(_)
    print('╚', end='')
    for i in range(len(symbol)):
        print('═', end='')
    print('╝', end='')
    if _ < 7:
        for _ in range(int(offset)):
            print(' ', end='')

# Some end newlines for cleanliness
print()
