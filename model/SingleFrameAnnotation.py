import json
from dataclasses import dataclass, field
from typing import *

from model.PedestrianTag import PedestrianTag
from model.VehicleTag import VehicleTag
from model.SceneTag import SceneTag

@dataclass
class SingleFrameAnnotation:
    time: float
    frame: int
    pedTags: List[PedestrianTag] = field(default_factory=list)
    egoTags: List[VehicleTag] = field(default_factory=list)
    sceneTags: List[SceneTag] = field(default_factory=list)

    def __str__(self) -> str:
        return f"SingleFrameAnnotation(time={self.time}, frame={self.frame}, pedTags={self.pedTags}, egoTags={self.egoTags}, sceneTags={self.sceneTags})"
    def toJSON(self) -> str:
        """A valid JSON representation of the object
        Returns:
            str: _description_
            """
        return self.__str__()