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

class VideoView:

    def __init__(self, eventManager: EventManager) -> None:
        self.eventManager = eventManager
        self.currentFrame = tk.IntVar(value=0)
        self.frameNumberText = tk.StringVar()
        self.currentFrame.trace_add('write', self.update_frame_number_text)
        self.startFrame = tk.IntVar(value=0)
        self.endFrame = tk.IntVar(value=0)
        self.fps = 0
        self.playing = tk.BooleanVar(value=True)

    def render(self, parent: TKMT.WidgetFrame, video_url="https://www.youtube.com/watch?v=eu4QqwsfXFE"):
        self.videoController = YoutubeController(url=video_url)
        self.currentFrame.set(0)

        video_label = parent.Label(text="Video view")
        video_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        frameList = []

        # video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"
        video_thread = threading.Thread(target=self.videoController.captureFrames, args=(frameList,))
        video_thread.start()

        video_label.after(0, lambda: self.update_frame(video_label, frameList))

        parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.currentFrame,
                  widgetkwargs={"command":self.on_slider_move}).grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.startFrame,
                  widgetkwargs={"command":self.on_slider_move}).grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
        parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.endFrame,
                  widgetkwargs={"command":self.on_slider_move}).grid(row=3, column=0, columnspan=3, padx=10, pady=10)
        self.endFrame.set(self.videoController.getNFrames())

        parent.Button(text="<<", command=self.skip_left).grid(
            row=4, column=0, padx=10, pady=10)
        parent.Button(text="Pause" if self.playing.get() else "Play", command=self.toggle_play_pause).grid(
            row=4, column=1, padx=10, pady=10)
        parent.Button(text=">>", command=self.skip_right).grid(
            row=4, column=2, padx=10, pady=10)
        
        parent.Button(text="Match Frame", command=self.match_frame).grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        parent.Button(text="Replay Segment", command=self.replay_segment).grid(row=5, column=2, columnspan=1, padx=10, pady=10)

        frame_number_label = parent.Label(text=self.frameNumberText.get(), size=12, widgetkwargs={"textvariable":self.frameNumberText})
        frame_number_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

    def on_slider_move(self, value):
        print("Slider moved to frame:", value)

    def update_frame(self, video_label, frameList):
        def update():
            # if self.playing.get() and len(frameList) - 1 > self.currentFrame.get():
            if self.currentFrame.get() < self.startFrame.get():
                self.currentFrame.set(self.startFrame.get())
            if self.currentFrame.get() > self.endFrame.get():
                self.currentFrame.set(self.endFrame.get())

            frame = frameList[self.currentFrame.get()]
            frame = cv2.resize(frame, (480, 270))

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)

            photo = ImageTk.PhotoImage(image=pil_image)
            video_label.config(image=photo)
            video_label.image = photo

            if self.playing.get():
                self.currentFrame.set(self.currentFrame.get() + 1)

                if self.fps == 0:
                    self.fps = self.videoController.getFPS()
                interval = int(1000 / self.fps)  # ms
                # Use 'after' to schedule the next update
                video_label.after(interval, update)
            else:
                video_label.after(1000, update)

    def update_frame_number_text(self, *args):
        self.frameNumberText.set(f"Current Frame: {self.currentFrame.get()}")

    def requestAnnotation(self):
        event = AppEvent(AppEventType.requestAnnotation, data={"timestamp": 0, "frame": self.currentFrame})
        # self.videoController.eventHandler(event)
        self.eventManager.onEvent(event)
        # Start the first update
#        video_label.after(0, update)
        
    def toggle_play_pause(self):
        self.playing.set(not self.playing.get())
        print("Paused" if not self.playing.get() else "Playing")

    def skip_left(self):
        self.currentFrame.set(self.currentFrame.get()-30)

    def skip_right(self):
        self.currentFrame.set(self.currentFrame.get()+30)

    def match_frame(self):
        matching_frame = self.startFrame.get()
        self.endFrame.set(matching_frame)
        self.currentFrame.set(matching_frame)
        self.playing.set(True)
    
    def replay_segment(self):
        self.currentFrame.set(self.startFrame.get())
