
from model import MultiFrameAnnotation, SingleFrameAnnotation
from model.Recording import Recording


class RecordingController:
    def __init__(self, recording: Recording = None):
        self.recording = Recording() if recording is None else recording

    def addSingleFrameAnnotation(self, singleAnnotation: SingleFrameAnnotation):
        self.recording.singleFrameAnnotation.append(singleAnnotation)
        pass
    
    def addMultiFrameAnnotation(self, multiFrameAnnotation: MultiFrameAnnotation):
        self.recording.multiFrameAnnotations.append(multiFrameAnnotation)
        pass