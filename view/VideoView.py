import tkinter as tk
from tkinter import ttk
from typing import Callable
import TKinterModernThemes as TKMT
import cv2
from PIL import Image, ImageTk
from pytube import YouTube
import threading
import logging
import queue
from controller.VideoController import VideoController
from controller.YoutubeController import YoutubeController
from library.AppEvent import AppEvent, AppEventType
from managers.EventManager import EventManager
from managers.ViewEventManager import ViewEventManager

from view.View import View
import time

class VideoView:

    def __init__(self, eventManager: EventManager, viewEventManager: ViewEventManager) -> None:
        self.name = f"VideoView"
        self.eventManager = eventManager
        self.viewEventManager = viewEventManager

        self.videoScreenSize = (480, 270)
        
        self.currentFrame = tk.IntVar(value=0)
        self.currentFrameText = tk.StringVar()
        self.currentFrame.trace_add('write', self.updateCurrentFrameFromSlider)

        self.startFrame = tk.IntVar(value=0)
        self.startFrameText = tk.StringVar()
        self.startFrameText.set("Start Frame: 0")
        self.startFrame.trace_add('write', self.updateStartFrameFromSlider)

        self.endFrame = tk.IntVar(value=0)
        self.endFrameText = tk.StringVar()
        self.endFrame.trace_add('write', self.updateEndFrameFromSlider)

        self.segmentProgress = tk.IntVar(value=0)

        self.fps = 0
        self.playing = tk.BooleanVar(value=True)
        self.needReset = False

    def handleEvent(self, appEvent: AppEvent):
        raise Exception("handleEvent not implemented")

    def render(self, parent: TKMT.WidgetFrame, videoURL):
        self.videoController = YoutubeController(url=videoURL, eventManager=self.eventManager)
        # TODO rest of the code should ran after a while.
        self.currentFrame.set(0)

        self.videoLabel = parent.Label(text="Video", row=0, col=0, rowspan=6, colspan=3, padx=10, pady=10)

        self.frameList = []

        # videoURL = "https://www.youtube.com/watch?v=eu4QqwsfXFE"
        self.videoThread = threading.Thread(target=self.videoController.captureFrames, args=(self.frameList,))
        self.videoThread.start()


        self.currentSlider = parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.currentFrame,
                  widgetkwargs={"command":self.updateCurrentFrameFromSlider},
                  row=0, col=3, colspan=3, padx=10, pady=10)
        
        self.startSlider = parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.startFrame,
                  widgetkwargs={"command":self.updateStartFrameFromSlider},
                  row=1, col=3, colspan=3, padx=10, pady=10)
        
        self.endSlider = parent.Scale(lower=0, upper=self.videoController.getNFrames(), variable=self.endFrame,
                  widgetkwargs={"command":self.updateEndFrameFromSlider},
                  row=2, col=3, colspan=3, padx=10, pady=10)

        self.endFrame.set(self.videoController.getNFrames())
        

        parent.Button(text="<<", command=self.skip_left, row=3, col=3, padx=10, pady=10)
        self.playBtn = parent.Button(text="Pause" if self.playing.get() else "Pause", command=self.toggle_play_pause, row=3, col=4, padx=10, pady=10)
        parent.Button(text=">>", command=self.skip_right, row=3, col=5, padx=10, pady=10)
        
        parent.Button(text="Snap Start", command=self.snapStart, row=4, col=3, padx=10, pady=10)
        parent.Button(text="Snap End", command=self.snapEnd, row=4, col=4, padx=10, pady=10)
        parent.Button(text="Replay", command=self.replaysegment, row=4, col=5, padx=10, pady=10)

        parent.Progressbar(variable=self.segmentProgress, mode="determinate", lower=0, upper=100, row=5, col=3, colspan=3)

        currentFrameLabel = parent.Text(text=self.currentFrameText.get(), widgetkwargs={"textvariable":self.currentFrameText}, row=0, col=6, padx=10, pady=10, sticky=tk.N+tk.S+tk.W)

        startFrameLabel = parent.Text(text=self.startFrameText.get(), widgetkwargs={"textvariable":self.startFrameText}, row=1, col=6, padx=10, pady=10, sticky=tk.N+tk.S+tk.W)

        endFrameLabel = parent.Text(text=self.endFrameText.get(), widgetkwargs={"textvariable":self.endFrameText}, row=2, col=6, padx=10, pady=10, sticky=tk.N+tk.S+tk.W)


        
        self.videoLabel.after(0, self.update_frame)
        

    def updateVideo(self, videoURL: str):
        logging.info(f"{self.name}: Loading new video from {videoURL}")

        self.videoURL = videoURL
        self.destroy()
        self.videoLabel.after(2000, self.updateAfterDestroy)

    
    def updateAfterDestroy(self):
        self.videoController = YoutubeController(url=self.videoURL, eventManager=self.eventManager)
        # TODO rest of the code should run after a while.
        time.sleep(1)
        # self.currentFrame.set(0)
        self.frameList.clear()
        self.videoThread = threading.Thread(target=self.videoController.captureFrames, args=(self.frameList,))
        self.videoThread.start()

        print("update video slider", self.currentSlider)
        
        self.currentSlider.configure(to=self.videoController.getNFrames())
        self.startSlider.configure(to=self.videoController.getNFrames())
        self.endSlider.configure(to=self.videoController.getNFrames())
        print(f"the upper for current slider should be {self.videoController.getNFrames()}")
        
                  
        self.currentFrame.set(0)
        self.startFrame.set(0)
        self.endFrame.set(self.videoController.getNFrames())
        
        self.fps = self.videoController.getFPS()
        self.eventManager.onEvent(AppEvent(type=AppEventType.recording, data={"updateFPS": self.fps}))

        self.needReset = False
        self.videoLabel.after(0, self.update_frame)



    def destroy(self):
        # 1. Clean up old update loop

        if hasattr(self, "videoController") and self.videoController is not None:
            self.videoController.stop()
        self.needReset = True
        self.currentFrame.set(0)
        self.frameList.clear()

        # TODO loading later
        # loadingImage = cv2.imread("assets/images/video_loading.png")
        # loadingImage = cv2.resize(loadingImage, self.videoScreenSize)
        # loadingImage = cv2.cvtColor(loadingImage, cv2.COLOR_BGR2RGB)
        # loadingImage = Image.fromarray(loadingImage)
        # photo = ImageTk.PhotoImage(image=loadingImage)
        # self.videoLabel.config(image=photo)
        # self.videoLabel.image = photo

        # self.loadingBar = self.videoLabel.Progressbar(tk.IntVar(value=0), mode = 'indeterminate',row=2, col=3)
        # self.loadingBar.start()
        # time.sleep(2)

        while self.videoThread.is_alive():
            print(f"waiting for video thread to die...")
            time.sleep(1)
        # self.videoThread.term
        # 2. load the new one


    def update_frame(self):

        if self.needReset:
            print("Cleaning up the old video loop")
            return
        if len(self.frameList) == 0:
            print("waiting 1 second for the frames.")
            # self.videoLabel.after(100, self.loadingBar.start)
            self.videoLabel.after(1000, self.update_frame)
        else:
            # self.fps = self.videoController.getFPS() # TODO this is dangerous
            # if self.playing.get() and len(self.frameList) - 1 > self.currentFrame.get():
            if self.currentFrame.get() < self.startFrame.get():
                self.currentFrame.set(self.startFrame.get())
            if self.currentFrame.get() > self.endFrame.get():
                self.currentFrame.set(self.endFrame.get())

            self.segmentProgress.set(int((self.currentFrame.get()-self.startFrame.get())/(self.endFrame.get()-self.startFrame.get()) * 100))

            frame = self.frameList[self.currentFrame.get()]
            frame = cv2.resize(frame, self.videoScreenSize)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)

            photo = ImageTk.PhotoImage(image=pil_image)
            self.videoLabel.config(image=photo)
            self.videoLabel.image = photo

            if self.playing.get():
                self.currentFrame.set(self.currentFrame.get() + 1)
                if self.fps == 0:
                    self.fps = self.videoController.getFPS()
                    if self.fps > 0:
                        self.eventManager.onEvent(AppEvent(type=AppEventType.recording, data={"updateFPS": self.fps}))
                if self.fps == 0:
                    interval = 1000
                else:
                    interval = int(1000 / self.fps)  # ms
                # Use 'after' to schedule the next update
                self.videoLabel.after(interval, self.update_frame)
            else:
                self.videoLabel.after(1000, self.update_frame)
    
        # Start the first update

    def updateCurrentFrameFromSlider(self, *args):
        # self.currentFrame.set(newVal)
        self.currentFrameText.set(f"Current Frame: {self.currentFrame.get()}")
        if self.currentFrame.get() == self.endFrame.get():
            self.pause()

        self.viewEventManager.publishCurrentFrameChange(self.currentFrame.get())

    def updateStartFrameFromSlider(self, *args):
        # self.startFrame.set(newVal)
        self.startFrameText.set(f"Start Frame: {self.startFrame.get()}")
        self.viewEventManager.publishStartFrameChange(self.startFrame.get())
    
    def updateEndFrameFromSlider(self, *args):
        # self.endFrame.set(newVal)
        self.endFrameText.set(f"End Frame: {self.endFrame.get()}")
        self.viewEventManager.publishEndFrameChange(self.endFrame.get())

    def pause(self):
        if hasattr(self, 'playBtn'):
            self.playing.set(False)
            self.playBtn.config(text="Play")
    
    def play(self):
        if hasattr(self, 'playBtn'):
            self.playing.set(True)
            self.playBtn.config(text="Pause")


    def toggle_play_pause(self):
        self.playing.set(not self.playing.get())
        if self.playing.get():
            self.playBtn.config(text="Pause")
        else:
            self.playBtn.config(text="Play")

    def skip_left(self):
        self.currentFrame.set(self.currentFrame.get()-30)

    def skip_right(self):
        self.currentFrame.set(self.currentFrame.get()+30)


    def snapStart(self):
        self.startFrame.set(self.currentFrame.get())

    def snapEnd(self):
        self.endFrame.set(self.currentFrame.get())

    
    def replaysegment(self):
        self.currentFrame.set(self.startFrame.get())
        self.play()
