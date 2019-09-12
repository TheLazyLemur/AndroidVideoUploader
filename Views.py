import tkinter as tk
import VideoUploadController
import sys

LARGE_FONT = ("Verdana", 12)


class UploadPage(tk.Frame):
    video_file = ""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Heading label
        label = tk.Label(self, text="Upload New Video", font=LARGE_FONT)
        label.pack(pady=25, padx=10)

        # Button to select the video to upload
        btn_select_video = tk.Button(
            self, text="Choose Video", command=lambda: self.choose_video())
        btn_select_video.pack(pady=50, padx=10)

        # Text fields for title, description and duration
        title_field = tk.Text(self, width=25, height=1)
        title_field.pack(pady=10, padx=10)
        title_field.insert('end-1c', "Title...")

        desc_field = tk.Text(self, width=25, height=10)
        desc_field.pack(pady=10, padx=10)
        desc_field.insert('end-1c', "Video Description...")

        duration_field = tk.Text(self, width=25, height=1)
        duration_field.pack(pady=10, padx=10)
        duration_field.insert('end-1c', "Duration(s)")

        # Button to finalise the upload
        btn_upload_video = tk.Button(self, text="Upload",
                                     command=lambda: self.upload(title_field, desc_field, duration_field))
        btn_upload_video.pack(pady=50, padx=10)

        # Close button
        btn_upload_video = tk.Button(self, text="Quit",
                                     command=lambda: self.close_app())
        btn_upload_video.pack(pady=50, padx=10)

    def choose_video(self):
        self.video_file = VideoUploadController.choose_video()

    def upload(self, title_field, desc_field, duration_field):
        VideoUploadController.upload(self.video_file,
                                     VideoUploadController.validate_title(title_field.get("1.0", 'end-1c')),
                                     desc_field.get(
                                         "1.0", 'end-1c'),
                                     duration_field.get("1.0", 'end-1c'))

    def close_app(self):
        sys.exit()