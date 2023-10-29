from dataclasses import dataclass, field
from typing import *

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
            1. You can do it yourself
            2. or use python JSON library

        Returns:
            str: _description_
        """
        return f"{
            'name': self.name,
            'annotation_path': self.annotation_path,
            'video_path': self.video_path,
            'multiFrameAnnotations': self.multiFrameAnnotations, # this will not work, we need to convert this list to a string instead
            'singleFrameAnnotation': self.singleFrameAnnotation # this will not work, we need to convert this list to a string instead
        }"
    
    def fromJSON(self, json: str) -> 'Recording':
        # read the json string and convert it to a Recording object
        return None
