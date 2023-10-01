import pytest
import cv2
from pytube import YouTube
from controller.VideoController import VideoController

@pytest.fixture
def videoCapture() -> cv2.VideoCapture:
    video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"

    # Create a YouTube object
    yt = YouTube(video_url)
    # Get the best video stream available (usually the highest resolution)
    video_stream = yt.streams.filter(file_extension='mp4').first()
    # Get the frame rate of the video
    frame_rate = int(video_stream.fps)
    print(frame_rate)
    # Create a VideoCapture object to read video stream
    video_capture = cv2.VideoCapture(video_stream.url)

    return video_capture


def test_fps(videoCapture):
    videoController = VideoController(videoCapture)
    assert videoController.getFPS() == 30

def test_duration(videoCapture):
    videoController = VideoController(videoCapture)
    assert videoController.getDuration() > 60 and videoController.getDuration() < 300

def test_nframes(videoCapture):
    videoController = VideoController(videoCapture)
    nframes = videoController.getNFrames()
    assert nframes == 1800

def test_frame_after(videoCapture):
    videoController = VideoController(videoCapture)
    current_frame = 30
    duration = 10
    expected_frame = current_frame + videoController.getFPS() * duration
    
    assert videoController.getFrameAfter(current_frame, duration) == expected_frame

def test_frame_before(videoCapture):
    videoController = VideoController(videoCapture)
    current_frame = 300
    duration = 5
    expected_frame = current_frame - videoController.getFPS() * duration
    
    assert videoController.getFrameBefore(current_frame, duration) == expected_frame