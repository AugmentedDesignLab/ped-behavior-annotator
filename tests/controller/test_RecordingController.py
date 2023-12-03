from asyncio.windows_events import NULL
from tokenize import Single
from model.MultiFrameAnnotation import MultiFrameAnnotation
from model.SingleFrameAnnotation import SingleFrameAnnotation
from model.Recording import Recording
from model.RecordingRepository import RecordingRepository
from controller.RecordingController import RecordingController
import pytest


@pytest.fixture
def singleAnnotation() -> SingleFrameAnnotation:
    singleFrame = SingleFrameAnnotation()
    return singleFrame

@pytest.fixture
def multiAnnotation() -> MultiFrameAnnotation:
    multiFrame = MultiFrameAnnotation()
    return multiFrame

def test_addSingleFrameAnnotation(singleAnnotation):
    # Create a Repository object and Recording Object. 
    recording = Recording(name="", annotation_path="", video_path="")
    video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"
    repository = RecordingRepository(video_url)
    recordingController = RecordingController(repository, recording)
    recordingController.addSingleFrameAnnotation(singleAnnotation)

    # Assert for not null value. 
    assert recordingController.getRecordingByVideoPath(video_url) != None

def test_addMultiFrameAnnotation():
    
    recording = Recording(name="", annotation_path="", video_path="")
    
    video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"
    repository = RecordingRepository(video_url)
    recordingController = RecordingController(repository, recording)
    recordingController.addMultiFrameAnnotation(multiAnnotation)

    assert recordingController.getRecordingByVideoPath(video_url) != None