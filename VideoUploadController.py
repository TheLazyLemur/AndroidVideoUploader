import os
import adb_utils
import ffmpeg_utils
from shutil import copy
from tkinter import filedialog


def choose_video():
    video_file = filedialog.askopenfilename(
        filetypes=(
            ("mp4 files", "*.mp4"),
            ("mov files", "*.mov"),
            ("mkv files", "*.mkv"),
        ))
    video_file = copy(video_file, os.path.dirname(
        os.path.realpath(__file__)) + "_new")
    return video_file


def create_directory_on_device():
    # Variables
    android_root = "/mnt/sdcard/"
    specified_dir = "RepController/Library/Videos/"
    # Build make directory adb command
    final_dir = android_root + specified_dir
    create_dir_cmd = "mkdir -p " + final_dir
    # Send adb command
    adb_utils.create_dir_on_devices(create_dir_cmd)
    return final_dir


def validate_title(_title):
    if " " in _title:
        _newTitle = _title.replace(" ", '_')
        return _newTitle
    if _title.isspace():
        print('Title cannot be empty')
        quit()
    return _title


# Takes the title, description and video length and builds the metadata
def build_metadata(_title, _desc, _duration):
    txt_file = open(_title + ".txt", "x")
    txt_file.write(_title + ";" + _desc + ";" + _duration)
    txt_file.close()


def upload(video_file, title, description, time):
    directory = create_directory_on_device()
    build_metadata(title, description, time)
    os.rename(video_file, title + ".mp4")

    ffmpeg_utils.make_thumbnail(os.getcwd(), title)
    successful = adb_utils.push_files_to_devices(title, directory)

    if successful == True:
        clean_files(title)
        print("Files were successfully pushed")
    else:
        clean_files(title)
        print("Operation Failed as a result")


# Clean the files after creating them so duplicates are not left over
def clean_files(_title):
    os.remove(_title + ".txt")
    os.remove(_title + ".mp4")
    os.remove(_title + ".png")
