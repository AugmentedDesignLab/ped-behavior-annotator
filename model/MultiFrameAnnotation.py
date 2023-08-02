from dataclasses import dataclass, field
from typing import *

@dataclass
class MultiFrameAnnotation:
    timeStart: float
    timeEnd: float
    frameStart: int
    frameEnd: int
    tags: List[str] = field(default_factory=list)

