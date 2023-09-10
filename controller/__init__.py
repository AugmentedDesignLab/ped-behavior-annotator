from VideoController import VideoController
import cv2
from pytube import YouTube

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

def test_youtube_controller():
    url = "https://www.youtube.com/watch?v=DXPCyfVVbpw"
    
    yt_controller = YoutubeController(url)
    ret, frame = yt_controller.capture.read()
    
    if ret:
        print("Successfully read a frame from the video")
        cv2.imshow("Frame", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Failed to read a frame from the video")

    yt_controller.close()

if __name__ == "__main__":
    test_youtube_controller()
