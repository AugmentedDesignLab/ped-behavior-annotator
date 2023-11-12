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
from controller.YoutubeController import YoutubeController
from library.AppEvent import AppEvent, AppEventType
from managers.EventManager import EventManager

from view.View import View

class VideoView(View):

    def __init__(self, eventManager: EventManager) -> None:
        self.eventManager = eventManager
        self.currentFrame = tk.IntVar(value=0)

    def render(self, parent: TKMT.WidgetFrame, video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"):

        self.videoController = YoutubeController(url=video_url)

        text_label = parent.Label(text="This is our video", size=12)
        text_label.grid(row=0, column=0, padx=10, pady=10)

        video_label = parent.Label("Video view")
        video_label.grid(row=1, column=0, padx=10, pady=10)

        frame_queue = queue.Queue()

        # video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"
        video_thread = threading.Thread(target=self.videoController.captureFrames, args=(frame_queue,))
        video_thread.start()

        # self.videoController.captureFrames(frame_queue)

        update_thread = threading.Thread(target=self.update_frame, args=(video_label, frame_queue))
        update_thread.start()

        # slider = parent.Scale(from_=0, to=100, orient=tk.HORIZONTAL, command=self.on_slider_move)
        # slider.grid(row=2, column=0, padx=20, pady=10)
        
        self.currentFrame.set(0)
        parent.Scale(0, self.videoController.getNFrames(), self.currentFrame, widgetkwargs={"command":self.on_slider_move})
        parent.Progressbar(self.currentFrame)

        annotate_button = parent.Button(text="Annotate", command=self.requestAnnotation)
        annotate_button.grid(row=3, column=0, padx=10, pady=10)

    def on_slider_move(self, value):
        print("Slider moved to frame:", value)

    def update_frame(self, video_label, frame_queue):
    
        try:
            frame = frame_queue.get_nowait()

            frame = cv2.resize(frame, (960, 540))  # Change the size here as needed

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)

            photo = ImageTk.PhotoImage(image=pil_image)
            video_label.config(image=photo)
            video_label.image = photo

            self.currentFrame.set(self.currentFrame.get() + 1) # incrementing the current frame number.

        except queue.Empty:
            pass

        video_label.after(10, self.update_frame, video_label, frame_queue)

    def requestAnnotation(self):
        event = AppEvent(AppEventType.requestAnnotation, data={"timestamp": 0, "frame": self.currentFrame})
        # self.videoController.eventHandler(event)
        self.eventManager.onEvent(event)