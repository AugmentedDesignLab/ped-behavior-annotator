from enum import Enum

class SceneTag(str, Enum):
    RedLight = "Red Light"
    ChangingLight = "Changing Light"
    NoSigns = "No stop signs"
    NoLight = "No traffic lights"

