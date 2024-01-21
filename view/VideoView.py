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
        self.frameNumberText = StringVar()
        self.currentFrame.trace('w', self.update_frame_number_text)

    def render(self, parent: TKMT.WidgetFrame, video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"):

        self.videoController = YoutubeController(url=video_url)
        self.currentFrame.set(0)

        text_label = parent.Label(text="This is our video", size=12)
        text_label.grid(row=0, column=0, padx=10, pady=10)

        video_label = parent.Label("Video view")
        video_label.grid(row=1, column=0, padx=10, pady=10)

        frame_number_label = parent.Label(textvariable=self.frameNumberText, size=12)
        frame_number_label.grid(row=4, column=0, padx=10, pady=10)

        # frame_queue = queue.Queue()
        frameList = []

        # video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"
        video_thread = threading.Thread(target=self.videoController.captureFrames, args=(frameList,))
        video_thread.start()

        # self.videoController.captureFrames(frame_queue)

        update_thread = threading.Thread(target=self.update_frame, args=(video_label, frameList))
        update_thread.start()

        # slider = parent.Scale(from_=0, to=100, orient=tk.HORIZONTAL, command=self.on_slider_move)
        # slider.grid(row=2, column=0, padx=20, pady=10)
        
        parent.Scale(0, self.videoController.getNFrames(), self.currentFrame, widgetkwargs={"command":self.on_slider_move})
        parent.Progressbar(self.currentFrame)

        annotate_button = parent.Button(text="Annotate", command=self.requestAnnotation)
        annotate_button.grid(row=3, column=0, padx=10, pady=10)

    def on_slider_move(self, value):
        print("Slider moved to frame:", value)

    def update_frame(self, video_label: ttk.Label, frameList):
    
        if len(frameList) - 1 > self.currentFrame.get(): # we have a new frame
            frame = frameList[self.currentFrame.get() + 1]
            frame = cv2.resize(frame, (960, 540))

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)

            photo = ImageTk.PhotoImage(image=pil_image)
            video_label.config(image=photo)
            video_label.image = photo

            self.currentFrame.set(self.currentFrame.get() + 1) # incrementing the current frame number.

        inteval = int(1000 / self.videoController.getFPS()) # ms
        video_label.after(inteval, self.update_frame, video_label, frameList)

    def update_frame_number_text(self, *args):
        self.frameNumberText.set(f"Current Frame: {self.currentFrame.get()}")

    def requestAnnotation(self):
        event = AppEvent(AppEventType.requestAnnotation, data={"timestamp": 0, "frame": self.currentFrame})
        # self.videoController.eventHandler(event)
        self.eventManager.onEvent(event)