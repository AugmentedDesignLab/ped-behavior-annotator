from dataclasses import dataclass, field
from typing import *
import json

from model.MultiFrameAnnotation import MultiFrameAnnotation
from model.SingleFrameAnnotation import SingleFrameAnnotation

@dataclass
class Recording:
    name: str
    annotation_path: str # ./annotations/recording0001.json
    video_path: str # https://www.youtube.com/watch?v=kljhas3
    
    multiFrameAnnotations: List[MultiFrameAnnotation] = field(default_factory=list)
    singleFrameAnnotation: List[SingleFrameAnnotation] = field(default_factory=list)

    def toJSON(self) -> str:
        """A valid JSON representation of the object
        Returns:
            str: _description_
        """
        return (f"Recording(name: {self.name},'annotation_path': {self.annotation_path}, 'video_path': {self.video_path}, 'multiFrameAnnotations': {self.multiFrameAnnotations},'singleFrameAnnotation':{self.singleFrameAnnotation}")

    def fromJSON(self, json: str) -> 'Recording':
        # read the json string and convert it to a Recording object
        return None
