import sys

if sys.platform.startswith('linux'):
    from system_info_service.linux_system_info_service import LinuxSystemInfoService as SystemInfoService
elif sys.platform in ['win32', 'cygwin']:
    from system_info_service.windows_system_info_service import WindowsSystemInfoService as SystemInfoService
else:
    raise Exception("Could not determine OS or OS is not compatible!")
