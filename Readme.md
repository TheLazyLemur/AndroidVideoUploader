# Android Video uploader

### Description

This project is for a bigger Unity project. The tool picks a video, generates the meta data for the video based on parameters
and generates a thumbnail from the video. Once the data is generated it pushes the files to the connected android devices.

The Unity project looks to the directory this program uploads the content to, so the goal of this is to automate the process of manually adding files
, taking screenshots and writing titles, descriptions and timestamps multiple times.

##### NB : This only runs on windows as is.

### Dependencies

- Python 3
- ADB
- FFMPEG

### Setup

- Create directories FFMPEG and ADB
- Drop FFMPEG and ADB binaries into their respective folders
- Alternatively install ADB and FFMPEG on your system and add them to path.
- Run the app with ```python3 App.py```

### Road Map

- Linux Support
- MacOS Support
