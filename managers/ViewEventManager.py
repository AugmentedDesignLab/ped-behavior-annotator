from library.AppEvent import *
from managers.EventManager import *

class ViewEventManager:
    def __init__(self, eventManager: EventManager):
        self.eventManager = eventManager

    def publishStartFrameChange(self, startFrame: int):
        event = AppEvent(AppEventType.annotationEditView, data={"updateStartFrame": startFrame})
        self.eventManager.onEvent(event)

    def publishEndFrameChange(self, startFrame: int):
        event = AppEvent(AppEventType.annotationEditView, data={"updateEndFrame": startFrame})
        self.eventManager.onEvent(event)

    def publishCurrentFrameChange(self, startFrame: int):
        event = AppEvent(AppEventType.annotationEditView, data={"updateCurrentFrame": startFrame})
        self.eventManager.onEvent(event)