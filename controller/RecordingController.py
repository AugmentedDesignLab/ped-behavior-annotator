
from model import MultiFrameAnnotation, SingleFrameAnnotation
from model.Recording import Recording

# A controller sits between the repositories and views.

class RecordingController:
    def __init__(self, recording: Recording = None):
        self.recording = Recording() if recording is None else recording

    def addSingleFrameAnnotation(self, singleAnnotation: SingleFrameAnnotation):
        self.recording.singleFrameAnnotation.append(singleAnnotation) # this is still in memory
        # TODO:
        # call the repository to persist changes to the recording.
        pass

    def addMultiFrameAnnotation(self, multiFrameAnnotation: MultiFrameAnnotation):
        self.recording.multiFrameAnnotations.append(multiFrameAnnotation)
        pass