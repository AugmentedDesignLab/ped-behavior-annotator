from pytube import YouTube
import cv2
from controller.VideoController import VideoController


class YoutubeController(VideoController):
    def __init__(self, url: str) -> None:
        # Use pytube to download the video
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension='mp4').first()
        filepath = stream.download(filename='temp_video')

        # Create a capture object
        capture = cv2.VideoCapture(filepath)
        if not capture.isOpened():
            raise ValueError(f"Could not open video from URL: {url}")
        super().__init__(capture)

    def close(self):
        self.capture.release()
        import os
        os.remove('temp_video.mp4')