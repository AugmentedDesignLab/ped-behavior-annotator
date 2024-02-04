from typing import *
from library.AppEvent import *
from managers.EventManager import *
from model import SingleFrameAnnotation, MultiFrameAnnotation


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


    def publishNewAnnotation(self, annotation: Union[SingleFrameAnnotation, MultiFrameAnnotation]):
        event = AppEvent(AppEventType.recording, data={"newAnnotation": annotation})
        self.eventManager.onEvent(event)