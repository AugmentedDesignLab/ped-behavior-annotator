from dataclasses import dataclass, field
from typing import *

from model.MultiFrameAnnotation import MultiFrameAnnotation
from model.SingleFrameAnnotation import SingleFrameAnnotation

@dataclass
class Recording:
    name: str
    annotation_path: str
    video_path: str
    
    multiFrameAnnotations: List[MultiFrameAnnotation] = field(default_factory=list)
    singleFrameAnnotation: List[SingleFrameAnnotation] = field(default_factory=list)