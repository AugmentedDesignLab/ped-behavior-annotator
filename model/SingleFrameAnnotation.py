import json
from dataclasses import dataclass, field
from typing import *

from model.PedestrianTag import PedestrianTag
from model.VehicleTag import VehicleTag
from model.SceneTag import SceneTag

@dataclass
class SingleFrameAnnotation:
    # time: float
    frame: int
    pedTags: Set[PedestrianTag] = field(default_factory = set)
    egoTags: Set[VehicleTag] = field(default_factory = set)
    sceneTags: Set[SceneTag] = field(default_factory = set)
    additionalNotes: str = ""

    def __eq__(self, other):
        return (other and self.frame == other.frame)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.frame)

    def __str__(self) -> str:
        # return f"SingleFrameAnnotation(time={self.time}, frame={self.frame}, pedTags={self.pedTags}, egoTags={self.egoTags}, sceneTags={self.sceneTags}, additionalNotes={self.additionalNotes})"
        return f"SingleFrameAnnotation(frame={self.frame}, pedTags={self.pedTags}, egoTags={self.egoTags}, sceneTags={self.sceneTags}, additionalNotes={self.additionalNotes})"
    def toJSON(self) -> str:
        """A valid JSON representation of the object
        Returns:
            str: _description_
            """
        return self.__str__()