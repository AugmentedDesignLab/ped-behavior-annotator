from enum import Enum

class SceneTag(Enum):
    Day = "Day"
    Night = "Night"
    Sunny = "Sunny"
    Foggy = "Foggy"
    Cloudy = "Cloudy"
    Snowy = "Snowy"
    NoTrafficLight = "No traffic light"
    GreenTrafficLight = "Green traffic light"
    YellowTrafficLight = "Yellow traffic light"
    BlinkingYellowTrafficLight = "Blinking yellow traffic light"
    RedTrafficLight = "Red traffic light"
    StopSign = "Stop sign"
    Crosswalk = "Crosswalk"
    NoCrosswalk = "No crosswalk"
    Roundabout = "Roundabout"
    LightTraffic = "Light traffic"
    ModerateTraffic = "Moderate traffic"
    HeavyTraffic = "Heavy traffic"
    OneWayTraffic = "One-way traffic"
    TwoWayTraffic = "Two-way traffic"
    OccludedPedestrian = "Occluded pedestrian"
    GlareOnWindshield = "Glare on windshield"

# day, night, sunny, foggy, cloudy, snowy
# no traffic light, green traffic light, yellow traffic light, blinking yellow traffic light, red traffic light
# stop sign
# crosswalk, no crosswalk, roundabout
# light traffic, moderate traffic, heavy traffic, one-way traffic, two-way traffic
# occluded pedestrian, glare on windshield