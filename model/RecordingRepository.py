from model.Recording import Recording, RecordingEncoder
from typing import *
import json
import os

class RecordingRepository:
    """A repository is a collection.
    """

    def __init__(self, dir: str) -> None:
        self.dir = dir
        self._recordings: Dict[str, Recording] = {} # recording001 -> recording object for 001

        pass

    def save(self, recording: Recording) -> bool:
        # save meta
        # save annotations
        # save the JSON format.

        path = recording.annotation_path
        if not path.endswith('.json') and not path.endswith('.JSON'):
            path += '.json'
        if not os.path.isabs(path):
            path = os.path.join(self.dir, path)
        
        print(f"saving recording to {path}")
        with open(path, 'w') as f:
            # f.write(recording.toJSON())
            json.dump(recording, f, default=RecordingEncoder, indent=4)
            return True
        
        return False


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
    