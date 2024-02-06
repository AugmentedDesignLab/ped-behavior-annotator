from enum import Enum

class PedestrianTag(Enum):
    FlinchIn = "Flinch in"
    Collision = "Collision"
    Jaywalking = "Jaywalking"
    Distracted = "Distracted"
    NotLooking = "Not looking"

# PedestrianTag.Flinch == this is an object
# PedestrianTag.Flinch.value == "Flinch" this is a string
# Add more pedestrian behavior