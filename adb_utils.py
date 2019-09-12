import subprocess
import os
from adb.client import Client as AdbClient


def init_adb_daemon(app_root):
    global approot
    approot = app_root
    os.chdir(app_root + "/platform-tools/")
    subprocess.call("adb.exe start-server")
    os.chdir(app_root)


def get_devices():
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    return devices


def kill_adb_daemon(app_root):
    os.chdir(app_root + "/platform-tools/")
    subprocess.call("adb.exe kill-server")
    os.chdir(app_root)


def create_dir_on_devices(dir_cmd):
    devices = get_devices()
    devices_present = check_if_devices_present(devices)
    if devices_present:
        for device in devices:
            device.shell(dir_cmd)
    else:
        print("No android devices are connected")
        return


def push_files_to_devices(title, directory):
    devices = get_devices()
    devices_present = check_if_devices_present(devices)
    if devices_present:
        for device in devices:
            device.push(title + ".mp4", directory + "/" + title + ".mp4")
            device.push(title + ".txt", directory + "/" + title + ".txt")
            device.push(title + ".png", directory + "/" + title + ".png")
        return True
    else:
        print("No android devices are connected")
        return False


def check_if_devices_present(devices):
    if len(devices) <= 0:
        return False
    else:
        return True
