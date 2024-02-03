import json
from dataclasses import dataclass, field
from typing import *

@dataclass
class MultiFrameAnnotation:
    timeStart: float
    timeEnd: float
    frameStart: int
    frameEnd: int
    tags: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        return f"MultiFrameAnnotations(timeStart={self.timeStart}, timeEnd={self.timeEnd}, frameStart={self.frameStart}, frameEnd={self.frameEnd}, tags={self.tags})"

    def toJSON(self) -> str:
        """A valid JSON representation of the object
        Returns:
            str: _description_
            """
        return self.__str__()