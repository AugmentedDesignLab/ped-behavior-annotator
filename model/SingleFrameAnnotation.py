from dataclasses import dataclass, field
from typing import *

from model.PedestrianTag import PedestrianTag

@dataclass
class SingleFrameAnnotataion:
    time: float
    frame: int
    tags: List[PedestrianTag] = field(default_factory=list)

    def __str__(self) -> str:
        return f"SingleFrameAnnotation(time={self.time}, frame={self.frame}, tags={self.tags})"

