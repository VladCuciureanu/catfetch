import os
import re
import sys
import socket
import platform
import datetime

from utils.timedelta_format import timedelta_format
from system_info_service.system_info_service_interface import SystemInfoServiceInterface


class LinuxSystemInfoService(SystemInfoServiceInterface):
    @staticmethod
    def get_terminal_width():
        return list(map(lambda x: int(x), os.popen('stty size', 'r').read().split()))[1]

    @staticmethod
    def get_username():
        return os.popen('echo $USER').read().strip()

    @staticmethod
    def get_hostname():
        return socket.gethostname().strip()

    @staticmethod
    def get_os():
        return sys.platform

    @staticmethod
    def get_kernel():
        return platform.release()

    @staticmethod
    def get_terminal():
        return os.popen('pstree -sA $$ | awk -F \"---\" \'{ print $2 }\'').read().strip()

    @staticmethod
    def get_dewm():
        # TODO: Make it so you dont use wmctrl
        return os.popen('wmctrl -m').readline()[6:].strip()

    @staticmethod
    def get_hardware():
        return platform.machine()

    @staticmethod
    def get_cpu():
        return os.popen('cat /proc/cpuinfo').readlines()[4][13:].strip()

    @staticmethod
    def get_gpu():
        # TODO: Make it so you dont use glxinfo
        return re.sub(r'\([^)]*\)', '', os.popen('glxinfo | grep \"Device\"').readline()[12:].strip()).replace("  ",
                                                                                                               " ")

    @staticmethod
    def get_used_memory():
        return list(map(int, os.popen('free -t -m').readlines()[1].split()[1:4]))[1]

    @staticmethod
    def get_total_memory():
        return list(map(int, os.popen('free -t -m').readlines()[1].split()[1:4]))[0]

    @staticmethod
    def get_uptime():
        uptime = datetime.timedelta(seconds=get_linux_uptime())
        return timedelta_format(uptime)


def get_linux_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds
