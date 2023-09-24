from dataclasses import dataclass, field
from typing import *

from model.PedestrianTag import PedestrianTag
from model.VehicleTag import VehicleTag

@dataclass
class SingleFrameAnnotation:
    time: float
    frame: int
    pedTags: List[PedestrianTag] = field(default_factory=list)
    egoTags: List[VehicleTag] = field(default_factory=list)

    def __str__(self) -> str:
        return f"SingleFrameAnnotation(time={self.time}, frame={self.frame}, pedTags={self.pedTags}, egoTags={self.egoTags})"

