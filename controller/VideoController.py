from typing import List
import cv2
import queue
class VideoController:
    
    def __init__(self, capture: cv2.VideoCapture) -> None:
        self.capture = capture
        pass

    def getNFrames(self) -> int:
        #Total number of frames in the video
        return int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))

    def getFPS(self) -> float:
        #FPS of the video
        return self.capture.get(cv2.CAP_PROP_FPS)

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
        while True:
            ret, frame = self.capture.read()
            if not ret:
                break
            # frameQueue.put(frame)
            frameList.append(frame)
        self.capture.release()
        pass

