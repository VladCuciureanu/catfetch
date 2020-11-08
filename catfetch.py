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
print()
reset_text_style()

# Print actual data
# OS
set_text_style(2)
print(str.ljust("OS", 8), end="  >>  ")
set_text_style(3)
print(str.ljust(SystemInfoService.get_os(), column_count - 14)[0:column_count - 14])
# Kernel
set_text_style(2)
print(str.ljust("Kernel", 8), end="  >>  ")
set_text_style(3)
print(str.ljust(SystemInfoService.get_kernel(), column_count - 14)[0:column_count - 14])
# Terminal
set_text_style(2)
print(str.ljust("Terminal", 8), end="  >>  ")
set_text_style(3)
print(str.ljust(SystemInfoService.get_terminal(), column_count - 14)[0:column_count - 14])
# DE / WM
set_text_style(2)
print(str.ljust("DE / WM", 8), end="  >>  ")
set_text_style(3)
print(str.ljust(SystemInfoService.get_de_wm(), column_count - 14)[0:column_count - 14])
# Hardware
set_text_style(2)
print(str.ljust("Hardware", 8), end="  >>  ")
set_text_style(3)
print(str.ljust(SystemInfoService.get_hardware(), column_count - 14)[0:column_count - 14])
# CPU
set_text_style(2)
print(str.ljust("CPU", 8), end="  >>  ")
set_text_style(3)
print(str.ljust(SystemInfoService.get_cpu(), column_count - 14)[0:column_count - 14])
# GPU
set_text_style(2)
print(str.ljust("GPU", 8), end="  >>  ")
set_text_style(3)
print(str.ljust(SystemInfoService.get_gpu(), column_count - 14)[0:column_count - 14])
# Memory
set_text_style(2)
print(str.ljust("Memory", 8), end="  >>  ")
set_text_style(3)
print(str.ljust("{} MB / {} MB".format(SystemInfoService.get_used_memory(), SystemInfoService.get_total_memory()),
                column_count - 14)[0:column_count - 14])
# Uptime
set_text_style(2)
print(str.ljust("Uptime", 8), end="  >>  ")
set_text_style(3)
print(str.ljust(SystemInfoService.get_uptime(), column_count - 14)[0:column_count - 14])

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
