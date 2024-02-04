
from typing import *
from model import MultiFrameAnnotation, SingleFrameAnnotation
from model.Recording import Recording
from model.RecordingRepository import RecordingRepository
from managers.EventManager import EventManager 
from library import AppEvent, AppEventType


# A controller sits between the repositories and views.

class RecordingController:
    def __init__(self, repository: RecordingRepository, eventManager: EventManager, recording: Recording = None):
        self.repository = repository
        self.eventManager = eventManager
        self._recording = recording
        # self.initNewRecording("Test Recording", self.repository.location, "https://www.youtube.com/watch?v=eu4QqwsfXFE")

        self.eventManager.subscribe(AppEventType.recording, self.handleRecordingEvents)

    @property
    def recording(self) -> Recording:
        return self._recording

    def initNewRecording(self, name: str, fps: Optional[float], annotationPath: str, videoPath: str) -> Recording:
        self.saveProject() # saves the current project if not None

        self._recording = Recording(
            name=name,
            fps=fps,
            annotation_path=annotationPath,
            video_path=videoPath
        ) 
    

    def loadRecording(self, recording: Recording):
        self._recording = recording


    def addSingleFrameAnnotation(self, singleFrameAnnotation: SingleFrameAnnotation):
        print(f"Saving frame {singleFrameAnnotation}")
        self._recording.singleFrameAnnotation.append(singleFrameAnnotation) # this is still in memory
        # self.repository.save(self._recording)
        # TODO:
        # call the repository to persist changes to the recording.
        pass


    def addMultiFrameAnnotation(self, multiFrameAnnotation: MultiFrameAnnotation):
        print(f"Saving frame {multiFrameAnnotation}")
        self._recording.multiFrameAnnotations.append(multiFrameAnnotation)
        # self.repository.save(self._recording)
        pass

    def saveProject(self) -> Tuple[bool, str]:

        if self._recording is None:
            return False, "No recording to save"
        return self.repository.save(self._recording)

    def getRecordingByVideoPath(self, videoPath: str):
        self._recording = self.repository.getByVideoPath(videoPath)
        pass

    def handleRecordingEvents(self, event: AppEvent):
        # print("RecordingController received event", event)
        if "updateFPS" in event.data:
            self._recording.fps = event.data["updateFPS"]
        pass