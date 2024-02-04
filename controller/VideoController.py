from typing import List
import cv2
import queue
from managers.EventManager import EventManager
import logging
class VideoController:
    
    def __init__(self, capture: cv2.VideoCapture, eventManager: EventManager) -> None:
        self.capture = capture
        self.eventManager = eventManager

        self._readingFrames = False
        pass

    def getNFrames(self) -> int:
        #Total number of frames in the video
        return int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))

    def getFPS(self) -> int:
        #FPS of the video
        fps = int(self.capture.get(cv2.CAP_PROP_FPS))
        if fps is None or fps < 1:
            logging.warn(f"Unknown FPS, setting to 30")
            self.eventManager.publishExceptionMessage(f"Unknown FPS, setting to 30")
            fps = 30
        return fps

    def getDuration(self) -> float:
        #Duration of the video in seconds
        total_frames = self.getNFrames()
        fps = self.getFPS()
        if fps == 0:
            return 0
        return total_frames / fps

    def getFrameAfter(self, currentFrame: int, duration: float) -> int:
        #The frame number after the current frame or duration
        fps = self.getFPS()
        frame_diff = int(duration * fps)
        return currentFrame + frame_diff

    def getFrameBefore(self, currentFrame: int, duration: float) -> int:
        #Frame number before the current frame or duration
        fps = self.getFPS()
        frame_diff = int(duration * fps)
        return max(currentFrame - frame_diff, 0)
    

    def captureFrames(self, frameList: List[cv2.UMat]):
        self._readingFrames = True
        while True:
            if self._readingFrames is False:
                print(f"VideoController is shutting down early...")
                break # while capturing, external signal may want to stop it (for big videos)

            ret, frame = self.capture.read()
            if not ret:
                break
            # frameQueue.put(frame)
            frameList.append(frame)
        self.capture.release()
        self._readingFrames = False
        pass

    def stop(self):
        self._readingFrames = False
    
    @property
    def isDownloading(self):
        return self._readingFrames





