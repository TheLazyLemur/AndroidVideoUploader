import os
import tkinter as tk
import adb_utils as functions
from Views import UploadPage


class VideoUploadApp(tk.Tk):
    APP_ROOT = os.getcwd()

    def __init__(self, *args, **kwargs):
        functions.init_adb_daemon(self.APP_ROOT)

        # Configure layout
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Load frames
        self.frames = {}
        frame = UploadPage(container, self)
        self.frames[UploadPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(UploadPage)

    def show_frame(self, cont):
        # Display frame
        frame = self.frames[cont]
        frame.tkraise()


upload_app = VideoUploadApp()
upload_app.minsize(600, 600)
upload_app.maxsize(1920, 1080)
upload_app.mainloop()
