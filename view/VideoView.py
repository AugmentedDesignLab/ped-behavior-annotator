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

# class VideoView(View):

#     def __init__(self, eventManager: EventManager) -> None:
#         self.eventManager = eventManager
#         self.currentFrame = tk.IntVar(value=0)
#         self.fps = 0

#     def render(self, parent: TKMT.WidgetFrame, video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"):

#         self.videoController = YoutubeController(url=video_url)
#         self.currentFrame.set(0)

#         video_label = parent.Label("Video view")
#         video_label.grid(row=0, column=0, padx=10, pady=10)

#         # frame_queue = queue.Queue()
#         frameList = []

#         # video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"
#         video_thread = threading.Thread(target=self.videoController.captureFrames, args=(frameList,))
#         video_thread.start()

#         # self.videoController.captureFrames(frame_queue)

#         update_thread = threading.Thread(target=self.update_frame, args=(video_label, frameList))
#         update_thread.start()

#         # slider = parent.Scale(from_=0, to=100, orient=tk.HORIZONTAL, command=self.on_slider_move)
#         # slider.grid(row=2, column=0, padx=20, pady=10)
        
#         parent.Scale(0, self.videoController.getNFrames(), self.currentFrame, widgetkwargs={"command":self.on_slider_move})
#         parent.Progressbar(self.currentFrame)

#         annotate_button = parent.Button(text="Annotate", command=self.requestAnnotation)
#         annotate_button.grid(row=3, column=0, padx=10, pady=10)

#     def on_slider_move(self, value):
#         print("Slider moved to frame:", value)

#     def update_frame(self, video_label: ttk.Label, frameList):
    
#         if len(frameList) - 1 > self.currentFrame.get(): # we have a new frame
#             frame = frameList[self.currentFrame.get() + 1]
#             frame = cv2.resize(frame, (480, 270))

#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             pil_image = Image.fromarray(frame_rgb)

#             photo = ImageTk.PhotoImage(image=pil_image)
#             video_label.config(image=photo)
#             video_label.image = photo

#             self.currentFrame.set(self.currentFrame.get() + 1) # incrementing the current frame number.

#         if self.fps == 0:
#             self.fps = self.videoController.getFPS()
#         interval = int(1000 / self.fps) # ms
#         video_label.after(interval, self.update_frame, video_label, frameList)

#     def requestAnnotation(self):
#         event = AppEvent(AppEventType.requestAnnotation, data={"timestamp": 0, "frame": self.currentFrame})
#         # self.videoController.eventHandler(event)
#         self.eventManager.onEvent(event)

class VideoView:

    def __init__(self, eventManager: EventManager) -> None:
        self.eventManager = eventManager
        self.current_frame = tk.IntVar(value=0)
        self.start_frame = tk.IntVar(value=0)
        self.end_frame = tk.IntVar(value=0)
        self.fps = 0
        self.playing = tk.BooleanVar(value=True)

    def render(self, parent: TKMT.WidgetFrame, video_url="https://www.youtube.com/watch?v=eu4QqwsfXFE"):
        self.videoController = YoutubeController(url=video_url)
        self.current_frame.set(0)

        video_label = parent.Label(text="Video view")
        video_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        frame_list = []

        video_thread = threading.Thread(target=self.videoController.captureFrames, args=(frame_list,))
        video_thread.start()

        video_label.after(0, lambda: self.update_frame(video_label, frame_list))

        parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.current_frame,
                  widgetkwargs={"command":self.on_slider_move}).grid(row=1, column=0, columnspan=3, padx=20, pady=10)
        
        parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.start_frame,
                  widgetkwargs={"command":self.on_slider_move}).grid(row=2, column=0, columnspan=3, padx=20, pady=10)
        
        parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.end_frame,
                  widgetkwargs={"command":self.on_slider_move}).grid(row=3, column=0, columnspan=3, padx=20, pady=10)
        self.end_frame.set(self.videoController.getNFrames())

        parent.Button(text="<<", command=self.skip_left).grid(
            row=4, column=0, padx=10, pady=10)
        parent.Button(text="Pause" if self.playing.get() else "Play", command=self.toggle_play_pause).grid(
            row=4, column=1, padx=10, pady=10)
        parent.Button(text=">>", command=self.skip_right).grid(
            row=4, column=2, padx=10, pady=10)

        parent.Button(text="Match Frame", command=self.match_frame).grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    def on_slider_move(self, value):
        print("Slider moved to frame:", value)

    def update_frame(self, video_label, frame_list):
        def update():
            # if self.playing.get() and len(frame_list) - 1 > self.current_frame.get():
            if self.current_frame.get() < self.start_frame.get():
                self.current_frame.set(self.start_frame.get())
            if self.current_frame.get() > self.end_frame.get():
                self.current_frame.set(self.start_frame.get())

            frame = frame_list[self.current_frame.get()]
            frame = cv2.resize(frame, (480, 270))

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)

            photo = ImageTk.PhotoImage(image=pil_image)
            video_label.config(image=photo)
            video_label.image = photo

            if self.playing.get():
                self.current_frame.set(self.current_frame.get() + 1)

                if self.fps == 0:
                    self.fps = self.videoController.getFPS()
                interval = int(1000 / self.fps)  # ms
                # Use 'after' to schedule the next update
                video_label.after(interval, update)
            else:
                video_label.after(1000, update)

        # Start the first update
        video_label.after(0, update)
        
    def toggle_play_pause(self):
        self.playing.set(not self.playing.get())
        print("Paused" if not self.playing.get() else "Playing")

    def skip_left(self):
        self.current_frame.set(self.current_frame.get()-30)

    def skip_right(self):
        self.current_frame.set(self.current_frame.get()+30)
        if self.current_frame.get() > self.end_frame.get():
            self.current_frame.set(self.end_frame.get())

    def match_frame(self):
        matching_frame = self.start_frame.get()
        self.end_frame.set(matching_frame)
        self.current_frame.set(matching_frame)
        self.playing.set(True)