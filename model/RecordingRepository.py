from model.Recording import Recording
from typing import *


class RecordingRepository:
    """A repository is a collection.
    """

    def __init__(self, dir: str) -> None:
        pass

    def save(self, recording: Recording) -> bool:
        # save meta
        # save annotations
        pass

    def load() -> None:
        # reads all from the directory
        pass

    def getById(recordingId: str) -> Optional[Recording]: # Ignore it for now
        return None
    
    def getByVideoPath(videoPath: str) -> Optional[Recording]:
        # search though all the recordings and return the object that has the same video path as the input parameter
        return None
    