from enum import Enum

class PedestrianTag(Enum):
    Trip = "Trip"
    AloneLane = "Alone lane"
    BriskWalk = "Brisk-walk"
    GroupWalk = "Group-walk"
    GroupDisperse = "Group-disperse"
    DogWalk = "Dog-walk"
    Retreat = "Retreat"
    SpeedUp = "Speed-up"
    SlowDown = "Slow-down"
    Wander = "Wander"
    PauseStart = "Pause-start"
    Jaywalking = "Jaywalking"
    CrossOnRed = "Cross-on-red"
    Swerve = "Swerve"
    Break = "Break"
    FlinchOut = "Flinch out"
    FlinchIn = "Flinch in"
    Frozen = "Frozen"
    Collision = "Collision"
    NearMiss = "Near-miss"
    RunIntoTraffic = "Run into traffic"
    ThrownBack = "Thrown back"
    MakeStop = "Make stop"
    MakeGo = "Make go"
    Aggression = "Aggression"
    Observing = "Observing"
    Looking = "Looking"
    Glancing = "Glancing"
    NotLookingGlancing = "Not looking/glancing"
    Distracted = "Distracted"
    Agitated = "Agitated"
    Cautious = "Cautious"
    Indecisive = "Indecisive"
    Cross = "Cross"
    NotCross = "Not-cross"
    NotSureCross = "Not-sure-cross"

# trip, alone lane, brisk-walk, group-walk, group-disperse, dog-walk, retreat, speed-up, slow-down
# wander, pause-start, jaywalking, cross-on-red, swerve
# break, flinch out, flinch in, frozen, collision, near-miss
# near-miss, run into traffic, thrown back, make stop, make go, aggression, observing
# looking, glancing, not looking/glancing, distracted, agitated, cautious, indecisive
# Cross, not-cross, not-sure-cross

# PedestrianTag.Flinch == this is an object
# PedestrianTag.Flinch.value == "Flinch" this is a string