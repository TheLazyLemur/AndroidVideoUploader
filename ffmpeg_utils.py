import subprocess
import os


def make_thumbnail(cur_dir, video_title):
    subprocess.call(f"./ffmpeg/bin/ffmpeg.exe -i {video_title}.mp4 -ss 00:00:01.000 -vframes 1 {video_title}.png")
    print(os.listdir(cur_dir))
