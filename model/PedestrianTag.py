from enum import Enum

class PedestrianTag(Enum):
    Flinch = "Flinch"
    Crash = "Crash"
    Jaywalking = "Jaywalking"
    Distracted = "Distracted"
    NoLook = "No Looking"


# PedestrianTag.Flinch == this is an object
# PedestrianTag.Flinch.value == "Flinch" this is a string
# Add more pedestrian behavior