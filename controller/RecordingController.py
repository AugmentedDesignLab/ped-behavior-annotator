
from model import MultiFrameAnnotation, SingleFrameAnnotation
from model.Recording import Recording

# A controller sits between the repositories and views.

class RecordingController:
    def __init__(self, recording: Recording = None):
        self.recording = Recording(
            name="Test Recording",
            annotation_path="test_annotation_path",
            video_path="test_video_path"
        ) if recording is None else recording

    def addSingleFrameAnnotation(self, singleAnnotation: SingleFrameAnnotation):
        print(f"Saving frame {singleAnnotation}")
        self.recording.singleFrameAnnotation.append(singleAnnotation) # this is still in memory
        # TODO:
        # call the repository to persist changes to the recording.
        pass

    def addMultiFrameAnnotation(self, multiFrameAnnotation: MultiFrameAnnotation):
        self.recording.multiFrameAnnotations.append(multiFrameAnnotation)
        pass