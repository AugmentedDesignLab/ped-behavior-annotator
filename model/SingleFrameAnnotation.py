from dataclasses import dataclass, field
from typing import *

@dataclass
class SingleFrameAnnotation:
    time: float
    frame: int
    tags: List[str] = field(default_factory=list)

#get time and frame from annotationEditView