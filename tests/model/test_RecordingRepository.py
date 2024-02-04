import pytest
import cv2
from model.RecordingRepository import RecordingRepository
from model.Recording import Recording
from model.SingleFrameAnnotation import SingleFrameAnnotation
from model.PedestrianTag import PedestrianTag
from model.VehicleTag import VehicleTag
from model.SceneTag import SceneTag

def test_Save():

    repository = RecordingRepository("tests")
    recording = Recording(name="Test Recording", annotation_path="recording", video_path="test_recording")
    
    sAnnotation1 = SingleFrameAnnotation(
            frame=100
        )
    sAnnotation1.pedTags.append(PedestrianTag.Flinch)
    sAnnotation1.pedTags.append(PedestrianTag.Crash)

    sAnnotation2 = SingleFrameAnnotation(
            frame=101
        )
    sAnnotation2.egoTags.append(VehicleTag.Brake)
    sAnnotation2.sceneTags.append(SceneTag.RedLight)
    sAnnotation2.additionalNotes = "This is a note"

    recording.singleFrameAnnotation.extend([sAnnotation1, sAnnotation2])

    status, message = repository.save(recording)
    print(message)
    assert status == True