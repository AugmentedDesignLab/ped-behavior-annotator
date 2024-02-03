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
    pedTags: List[PedestrianTag] = field(default_factory=list)
    egoTags: List[VehicleTag] = field(default_factory=list)
    sceneTags: List[SceneTag] = field(default_factory=list)
    additionalNotes: str = ""

    def __str__(self) -> str:
        # return f"MultiFrameAnnotations(timeStart={self.timeStart}, timeEnd={self.timeEnd}, frameStart={self.frameStart}, frameEnd={self.frameEnd}, pedTags={self.pedTags}, egoTags={self.egoTags}, sceneTags={self.sceneTags}, additionalNotes={self.additionalNotes})"
        return f"MultiFrameAnnotations(frameStart={self.frameStart}, frameEnd={self.frameEnd}, pedTags={self.pedTags}, egoTags={self.egoTags}, sceneTags={self.sceneTags}, additionalNotes={self.additionalNotes})"
    def toJSON(self) -> str:
        """A valid JSON representation of the object
        Returns:
            str: _description_
            """
        return self.__str__()