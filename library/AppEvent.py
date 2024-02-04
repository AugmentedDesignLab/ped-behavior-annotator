from dataclasses import dataclass
from enum import IntEnum, auto

class AppEventType(IntEnum):
    requestAnnotation = auto()
    newProject = auto()
    saveProject = auto()
    updateRecordingView = auto()
    exceptions = auto()
    recording = auto()
    videoView = auto()
    annotationEditView = auto()
    titleView = auto()
    

@dataclass
class AppEvent():
    type: AppEventType
    data: any = None
    