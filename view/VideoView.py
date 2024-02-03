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
import time

class VideoView:

    def __init__(self, eventManager: EventManager) -> None:
        self.eventManager = eventManager
        
        self.currentFrame = tk.IntVar(value=0)
        self.currentFrameText = tk.StringVar()
        self.currentFrame.trace_add('write', self.updateCurrentFrameText)

        self.startFrame = tk.IntVar(value=0)
        self.startFrameText = tk.StringVar()
        self.startFrameText.set("Start Frame: 0")
        self.startFrame.trace_add('write', self.updateStartFrameText)

        self.endFrame = tk.IntVar(value=0)
        self.endFrameText = tk.StringVar()
        self.endFrame.trace_add('write', self.updateEndFrameText)

        self.segmentProgress = tk.IntVar(value=0)

        self.fps = 0
        self.playing = tk.BooleanVar(value=True)
        self.needReset = False

    def render(self, parent: TKMT.WidgetFrame, videoURL):
        self.videoController = YoutubeController(url=videoURL)
        self.currentFrame.set(0)

        self.videoLabel = parent.Label(text="Video")
        self.videoLabel.grid(row=0, column=0, rowspan=6, columnspan=3, padx=10, pady=10)

        self.frameList = []

        # videoURL = "https://www.youtube.com/watch?v=eu4QqwsfXFE"
        self.videoThread = threading.Thread(target=self.videoController.captureFrames, args=(self.frameList,))
        self.videoThread.start()


        self.currentSlider = parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.currentFrame,
                  widgetkwargs={"command":self.on_slider_move})
        self.currentSlider.grid(row=0, column=3, columnspan=3, padx=10, pady=10)
        
        self.startSlider = parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.startFrame,
                  widgetkwargs={"command":self.on_slider_move})
        self.startSlider.grid(row=1, column=3, columnspan=3, padx=10, pady=10)
        
        self.endSlider = parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.endFrame,
                  widgetkwargs={"command":self.on_slider_move})
        self.endSlider.grid(row=2, column=3, columnspan=3, padx=10, pady=10)

        self.endFrame.set(self.videoController.getNFrames())
        

        parent.Button(text="<<", command=self.skip_left).grid(
            row=3, column=3, padx=10, pady=10)
        parent.Button(text="Pause" if self.playing.get() else "Play", command=self.toggle_play_pause).grid(
            row=3, column=4, padx=10, pady=10)
        parent.Button(text=">>", command=self.skip_right).grid(
            row=3, column=5, padx=10, pady=10)
        
        parent.Button(text="Match Frame", command=self.match_frame).grid(row=4, column=3, columnspan=2, padx=10, pady=10)
        parent.Button(text="Replay Segment", command=self.replay_segment).grid(row=4, column=5, columnspan=1, padx=10, pady=10)

        parent.Progressbar(variable=self.segmentProgress, mode="determinate", lower=0, upper=100, row=5, col=3, colspan=3)

        currentFrameLabel = parent.Label(text=self.currentFrameText.get(), size=12, widgetkwargs={"textvariable":self.currentFrameText})
        currentFrameLabel.grid(row=0, column=6, columnspan=1, padx=10, pady=10)

        startFrameLabel = parent.Label(text=self.startFrameText.get(), size=12, widgetkwargs={"textvariable":self.startFrameText})
        startFrameLabel.grid(row=1, column=6, columnspan=1, padx=10, pady=10)

        endFrameLabel = parent.Label(text=self.endFrameText.get(), size=12, widgetkwargs={"textvariable":self.endFrameText})
        endFrameLabel.grid(row=2, column=6, columnspan=1, padx=10, pady=10)
        
        self.videoLabel.after(0, self.update_frame)
        

    def updateVideo(self, videoURL: str):

        self.videoURL = videoURL
        self.destroy()
        self.videoLabel.after(2000, self.updateAfterDestroy)

    
    def updateAfterDestroy(self):
        self.videoController = YoutubeController(url=self.videoURL)
        self.currentFrame.set(0)
        self.frameList.clear()
        self.videoThread = threading.Thread(target=self.videoController.captureFrames, args=(self.frameList,))
        self.videoThread.start()

        print("update video slider", self.currentSlider)
        
        self.currentSlider.upper = self.videoController.getNFrames()
        self.startSlider.upper = self.videoController.getNFrames()
        self.endSlider.upper = self.videoController.getNFrames()
        print(f"the upper for current slider should be {self.videoController.getNFrames()}")
        
        # self.startSlider = parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.startFrame,
        #           widgetkwargs={"command":self.on_slider_move}).grid(row=1, column=3, columnspan=3, padx=10, pady=10)
        
        # self.endSlider = parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.endFrame,
        #           widgetkwargs={"command":self.on_slider_move}).grid(row=2, column=3, columnspan=3, padx=10, pady=10)
                  
        self.endFrame.set(self.videoController.getNFrames())

        self.needReset = False
        self.videoLabel.after(0, self.update_frame)



    def destroy(self):
        # 1. Clean up old update loop
        self.needReset = True
        self.currentFrame.set(0)
        self.frameList.clear()
        time.sleep(2)

        assert self.videoThread.is_alive() == False
        # self.videoThread.term
        # 2. load the new one


    

    def on_slider_move(self, value):
        print("Slider moved to frame:", value)

    def update_frame(self):
        if self.needReset:
            print("Cleaning up the old video loop")
            return
        if len(self.frameList) == 0:
            print("waiting 1 second for the frames.")
            self.videoLabel.after(1000, self.update_frame)
        else:
            # if self.playing.get() and len(self.frameList) - 1 > self.currentFrame.get():
            if self.currentFrame.get() < self.startFrame.get():
                self.currentFrame.set(self.startFrame.get())
            if self.currentFrame.get() > self.endFrame.get():
                self.currentFrame.set(self.endFrame.get())

            self.segmentProgress.set(int((self.currentFrame.get()-self.startFrame.get())/(self.endFrame.get()-self.startFrame.get()) * 100))

            frame = self.frameList[self.currentFrame.get()]
            frame = cv2.resize(frame, (480, 270))

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)

            photo = ImageTk.PhotoImage(image=pil_image)
            self.videoLabel.config(image=photo)
            self.videoLabel.image = photo

            if self.playing.get():
                self.currentFrame.set(self.currentFrame.get() + 1)

                if self.fps == 0:
                    self.fps = self.videoController.getFPS()
                interval = int(1000 / self.fps)  # ms
                # Use 'after' to schedule the next update
                self.videoLabel.after(interval, self.update_frame)
            else:
                self.videoLabel.after(1000, self.update_frame)
    
        # Start the first update

    def updateCurrentFrameText(self, *args):
        self.currentFrameText.set(f"Current Frame: {self.currentFrame.get()}")

    def updateStartFrameText(self, *args):
        self.startFrameText.set(f"Start Frame: {self.startFrame.get()}")
    
    def updateEndFrameText(self, *args):
        self.endFrameText.set(f"End Frame: {self.endFrame.get()}")

# Annotations aren't requested in VideoView
#     def requestAnnotation(self):
#         event = AppEvent(AppEventType.requestAnnotation, data={"timestamp": 0, "frame": self.currentFrame})
#         # self.videoController.eventHandler(event)
#         self.eventManager.onEvent(event)
#         # Start the first update
# #        self.videoLabel.after(0, update)
        
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
