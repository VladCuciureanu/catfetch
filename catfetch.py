import re
import os
import sys
import socket
import platform
from term_color_util import set_text_style, reset_text_style, Color, Style

# Get pc info
row_count, column_count = map(lambda x: int(x), os.popen('stty size', 'r').read().split())
username = os.popen('echo $USER').read().strip()
hostname = socket.gethostname().strip()
total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[1].split()[1:4])
terminal = os.popen('pstree -sA $$ | awk -F \"---\" \'{ print $2 }\'').read().strip()
de_wm = os.popen('wmctrl -m').readline()[6:].strip()
cpu_name = os.popen('cat /proc/cpuinfo').readlines()[4][13:].strip()
gpu_name = re.sub(r'\([^)]*\)', '', os.popen('glxinfo | grep \"Device\"').readline()[12:].strip()).replace("  ", " ")
uptime = os.popen('python -m uptime').readline().strip().replace("hours","h").replace("minutes", "m").replace("seconds","s")[:-1]

# Clear terminal
print("\033[H\033[J")

# Print user and hostname
set_text_style(7, 0, 0)
print(username, end="")
set_text_style(5, 0, 0)
print(" @ ", end="")
set_text_style(7, 0, 0)
print(hostname)

# Print separator
set_text_style(1, 0, 0)
for _ in range(column_count//2):
    print("~ ", end="")
print()
reset_text_style()

# Print actual data
# OS
set_text_style(2, 0, 0)
print(str.ljust("OS", 8),end="  >>  ")
set_text_style(3, 0, 0)
print(str.ljust(sys.platform, column_count-14)[0:column_count-14])
# Kernel
set_text_style(2, 0, 0)
print(str.ljust("Kernel", 8),end="  >>  ")
set_text_style(3, 0, 0)
print(str.ljust(platform.release(), column_count-14)[0:column_count-14])
# Terminal
set_text_style(2, 0, 0)
print(str.ljust("Terminal", 8),end="  >>  ")
set_text_style(3, 0, 0)
print(str.ljust(terminal, column_count-14)[0:column_count-14])
# DE / WM
set_text_style(2, 0, 0)
print(str.ljust("DE / WM", 8),end="  >>  ")
set_text_style(3, 0, 0)
print(str.ljust(de_wm, column_count-14)[0:column_count-14])
# Hardware
set_text_style(2, 0, 0)
print(str.ljust("Hardware", 8),end="  >>  ")
set_text_style(3, 0, 0)
print(str.ljust(platform.machine(), column_count-14)[0:column_count-14])
# CPU
set_text_style(2, 0, 0)
print(str.ljust("CPU", 8),end="  >>  ")
set_text_style(3, 0, 0)
print(str.ljust(cpu_name, column_count-14)[0:column_count-14])
# GPU
set_text_style(2, 0, 0)
print(str.ljust("GPU", 8),end="  >>  ")
set_text_style(3, 0, 0)
print(str.ljust(gpu_name, column_count-14)[0:column_count-14])
# Memory
set_text_style(2, 0, 0)
print(str.ljust("Memory", 8),end="  >>  ")
set_text_style(3, 0, 0)
print(str.ljust("{} MB / {} MB".format(used_memory, total_memory), column_count-14)[0:column_count-14])
# Uptime
set_text_style(2, 0, 0)
print(str.ljust("Uptime", 8),end="  >>  ")
set_text_style(3, 0, 0)
print(str.ljust(uptime, column_count-14)[0:column_count-14])

# New line for cleanliness
print()

symbol = "⚞^..^⚟"
offset = (column_count - len(symbol)*7)/7-1

# Print top boxes
for _ in range(offset//2):
        print(' ',end='')
for _ in range(1,8):
    set_text_style(_, 0 ,0)
    print('╔',end='')
    for i in range(len(symbol)):
        print('═',end='')
    print('╗',end='')
    if _ < 7:
        for _ in range(offset):
            print(' ',end='')
print()

# Print middle boxes
for _ in range(offset//2):
        print(' ',end='')
for _ in range(1,8):
    set_text_style(_, 0 ,0)
    print('║',end='')
    print(symbol,end='')
    print('║',end='')
    if _ < 7:
        for _ in range(offset):
            print(' ',end='')
print()

# Print bottom boxes
for _ in range(offset//2):
        print(' ',end='')
for _ in range(1,8):
    set_text_style(_, 0 ,0)
    print('╚',end='')
    for i in range(len(symbol)):
        print('═',end='')
    print('╝',end='')
    if _ < 7:
        for _ in range(offset):
            print(' ',end='')


# Some end newlines for cleanliness
print()