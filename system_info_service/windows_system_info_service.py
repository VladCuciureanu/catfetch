import os
import datetime

from utils.timedelta_format import timedelta_format
from system_info_service.system_info_service_interface import SystemInfoServiceInterface


class WindowsSystemInfoService(SystemInfoServiceInterface):
    @staticmethod
    def get_terminal_width():
        return int(os.popen('mode con').readlines()[4].strip()[8:].strip())

    @staticmethod
    def get_username():
        return os.popen('echo %USERNAME%').read().strip()

    @staticmethod
    def get_hostname():
        return os.popen('hostname').read().strip()

    @staticmethod
    def get_os():
        return os.popen('wmic os get Caption /value').read().split('=')[1].strip()

    @staticmethod
    def get_kernel():
        return os.popen('ver').read().replace("]", "[").split("[")[1]

    @staticmethod
    def get_terminal():
        return os.popen('(dir 2>&1 *`|echo CMD);&<# rem #>echo PowerShell').read().strip()

    @staticmethod
    def get_de_wm():
        return 'Windows Shell'  # Could find a way to add more shell replacements but not worth my time ATM.

    @staticmethod
    def get_hardware():
        return os.popen('set processor').readlines()[0].split('=')[1].strip()

    @staticmethod
    def get_cpu():
        return os.popen('wmic cpu get name').readlines()[2].strip()

    @staticmethod
    def get_gpu():
        return os.popen('wmic path win32_VideoController get name').readlines()[2].strip()

    @staticmethod
    def get_used_memory():
        total_memory = int(os.popen('wmic OS get TotalVisibleMemorySize /Value').read().split('=')[1].strip())
        free_memory = int(os.popen('wmic OS get FreePhysicalMemory /Value').read().split('=')[1].strip())
        return int((total_memory - free_memory) * (10 ** -3))

    @staticmethod
    def get_total_memory():
        total_memory = int(os.popen('wmic OS get TotalVisibleMemorySize /Value').read().split('=')[1].strip())
        return int(total_memory * (10 ** -3))

    @staticmethod
    def get_uptime():
        raw_info_string = \
            os.popen('wmic path Win32_OperatingSystem get LastBootUpTime').readlines()[2].strip().split('.')[0]
        year = int(raw_info_string[0:4])
        month = int(raw_info_string[4:6])
        day = int(raw_info_string[6:8])
        hour = int(raw_info_string[8:10])
        minute = int(raw_info_string[10:12])
        second = int(raw_info_string[12:14])
        uptime = datetime.datetime.now() - datetime.datetime.now().replace(year=year, month=month, day=day, hour=hour,
                                                                           minute=minute, second=second)
        return timedelta_format(uptime)
