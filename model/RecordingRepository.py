from model.Recording import Recording
from typing import *


class RecordingRepository:
    """A repository is a collection.
    """

    def __init__(self, dir: str) -> None:
        self._recordings: Dict[str, Recording] = {} # recording001 -> recording object for 001
        pass

    def save(self, recording: Recording) -> bool:
        # save meta
        # save annotations
        pass

    def load() -> None:
        # reads all from the directory and saves to it's local cache
        pass

    def getById(recordingId: str) -> Optional[Recording]: # Ignore it for now
        """searches for recording by recordingId in the local cache

        Args:
            recordingId (str): _description_

        Returns:
            Optional[Recording]: _description_
        """
        return None
    

    
    def getByVideoPath(videoPath: str) -> Optional[Recording]:
        # search though all the recordings and return the object that has the same video path as the input parameter
        return None
    