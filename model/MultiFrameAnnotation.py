import json
from dataclasses import dataclass, field
from typing import *

from model.PedestrianTag import PedestrianTag
from model.VehicleTag import VehicleTag
from model.SceneTag import SceneTag

@dataclass
class MultiFrameAnnotation:
    # timeStart: float
    # timeEnd: float
    frameStart: int
    frameEnd: int
    pedTags: Set[PedestrianTag] = field(default_factory = set)
    egoTags: Set[VehicleTag] = field(default_factory = set)
    sceneTags: Set[SceneTag] = field(default_factory = set)
    additionalNotes: str = ""

    def __eq__(self, other):
        return (other and self.frameStart == other.frameStart) and (self.frameEnd == other.frameEnd) 

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.frameStart, self.frameEnd))

    def __str__(self) -> str:
        # return f"MultiFrameAnnotations(timeStart={self.timeStart}, timeEnd={self.timeEnd}, frameStart={self.frameStart}, frameEnd={self.frameEnd}, pedTags={self.pedTags}, egoTags={self.egoTags}, sceneTags={self.sceneTags}, additionalNotes={self.additionalNotes})"
        return f"MultiFrameAnnotations(frameStart={self.frameStart}, frameEnd={self.frameEnd}, pedTags={self.pedTags}, egoTags={self.egoTags}, sceneTags={self.sceneTags}, additionalNotes={self.additionalNotes})"
    def toJSON(self) -> str:
        """A valid JSON representation of the object
        Returns:
            str: _description_
            """
        return self.__str__()