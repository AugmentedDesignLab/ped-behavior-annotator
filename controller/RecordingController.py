
from typing import *
from model import MultiFrameAnnotation, SingleFrameAnnotation
from model.Recording import Recording
from model.RecordingRepository import RecordingRepository

# A controller sits between the repositories and views.

class RecordingController:
    def __init__(self, repository: RecordingRepository, recording: Recording = None):
        self.repository = repository
        self._recording = recording


    @property
    def recording(self) -> Recording:
        return self._recording

    def initNewRecording(self, name: str, annotationPath: str, videopath: str) -> Recording:
        self._recording = Recording(
            name=name,
            annotation_path=annotationPath,
            video_path=videopath
        ) 
    

    def loadRecording(self, recording: Recording):
        self._recording = recording


    def addSingleFrameAnnotation(self, singleAnnotation: SingleFrameAnnotation):
        print(f"Saving frame {singleAnnotation}")
        self._recording.singleFrameAnnotation.append(singleAnnotation) # this is still in memory
        self.repository.save(self._recording)
        # TODO:
        # call the repository to persist changes to the recording.
        pass


    def addMultiFrameAnnotation(self, multiFrameAnnotation: MultiFrameAnnotation):
        self._recording.multiFrameAnnotations.append(multiFrameAnnotation)
        self.repository.save(self._recording)
        pass


    def getRecordingByVideoPath(self, videoPath: str):
        self._recording = self.repository.getByVideoPath(videoPath)
        pass