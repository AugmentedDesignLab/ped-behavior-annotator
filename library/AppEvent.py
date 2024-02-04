from dataclasses import dataclass
from enum import IntEnum, auto

class AppEventType(IntEnum):
    requestAnnotation = auto()
    newProject = auto()
    saveProject = auto()
    updateRecordingView = auto()
    exceptions = auto()
    recording = auto()

@dataclass
class AppEvent():
    type: AppEventType
    data: any = None
    