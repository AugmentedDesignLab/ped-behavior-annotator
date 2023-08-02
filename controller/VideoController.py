import cv2

class VideoController:

    def __init__(self, capture: cv2.VideoCapture) -> None:
        self.capture = capture
        pass

    def getNFrames(self) -> int:
        pass

    def getFPS(self) -> float:
        pass

    def getDuration(self) -> float:
        pass

    def getFrameAfter(self, currentFrame: int, duration: float) -> int:
        pass

    def getFrameBefore(self, currentFrame: int, duration: float) -> int:
        pass