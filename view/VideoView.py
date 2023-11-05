import tkinter as tk
from tkinter import ttk
from typing import Callable
import TKinterModernThemes as TKMT
import cv2
from PIL import Image, ImageTk
from pytube import YouTube
import threading
import queue
from controller.VideoController import VideoController
from library.AppEvent import AppEvent, AppEventType

from view.View import View

class VideoView(View):

    def __init__(self, videoController: VideoController) -> None:
        self.videoController = videoController

    def render(self, parent: TKMT.WidgetFrame):
        text_label = parent.Label(text="This is our video", size=12)
        text_label.grid(row=0, column=0, padx=10, pady=10)

        video_label = parent.Label(master=parent)
        video_label.grid(row=1, column=0, padx=10, pady=10)

        frame_queue = queue.Queue()

        video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"
        video_thread = threading.Thread(target=self.start_video_stream, args=(video_url, frame_queue))
        video_thread.start()

        update_thread = threading.Thread(target=self.update_frame, args=(video_label, frame_queue))
        update_thread.start()

        slider = parent.Scale(from_=0, to=100, orient=tk.HORIZONTAL, command=self.on_slider_move)
        slider.grid(row=2, column=0, padx=20, pady=10)

        annotate_button = parent.Button(text="Annotate", command=self.requestAnnotation)
        annotate_button.grid(row=3, column=0, padx=10, pady=10)

    def on_slider_move(self, value):
        print("Slider moved to:", value)

    def start_video_stream(self, video_url, frame_queue):
        yt = YouTube(video_url)
        stream = yt.streams.filter(file_extension='mp4').first()

        cap = cv2.VideoCapture(stream.url)

        while True:
            ret, frame = cap.read()
            
            if not ret:
                break
            frame_queue.put(frame)
        cap.release()

    def update_frame(self, video_label, frame_queue):
        try:
            frame = frame_queue.get_nowait()

            frame = cv2.resize(frame, (960, 540))  # Change the size here as needed

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)

            photo = ImageTk.PhotoImage(image=pil_image)
            video_label.config(image=photo)
            video_label.image = photo

        except queue.Empty:
            pass

        video_label.after(10, self.update_frame, video_label, frame_queue)

    def requestAnnotation(self):
        event = AppEvent(AppEventType.requestAnnotation, data={"timestamp": 0, "frame": None})
        self.videoController.eventHandler(event)