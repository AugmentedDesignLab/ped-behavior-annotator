from enum import Enum

class VehicleTag(Enum):
    SpeedUp = "Speed-up"
    SlowDown = "Slow-down"
    GradualSpeedUp = "Gradual speed-up"
    GradualSlowDown = "Gradual slow-down"
    SlowReverse = "Slow-reverse"
    QuickReverse = "Quick-reverse"
    LaneChange = "Lane change"
    Speeding = "Speeding"
    Halt = "Halt"
    InducedCollision = "Induced collision"
    RunStop = "Run-stop"
    Swerve = "Swerve"
    MakeGo = "Make go"
    Sidewalk = "Sidewalk"

# speed-up, slow-down, gradual speed-up, gradual slow-down
# slow-reverse, quick-reverse, lane change, speeding, halt
# induced collision, run-stop, swerve, make go, sidewalk