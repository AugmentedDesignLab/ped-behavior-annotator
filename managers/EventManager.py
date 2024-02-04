
from library import AppEvent
from library.AppEvent import AppEventType
from typing import Callable
from collections import defaultdict

class EventManager:
    def __init__(self) -> None:
        
        ### event streams
        self.initEventStreams()
        pass

    def initEventStreams(self):
         self.handlers = defaultdict(lambda: [])
         
    def unsubscribe(self, eventType: AppEventType, handler: Callable):
        self.handlers[eventType].remove(handler)

    
    def subscribe(self, eventType: AppEventType, handler: Callable):
        self.handlers[eventType].append(handler)
    
    def onEvent(self, appEvent: AppEvent):
        for handler in self.handlers[appEvent.type]:
            handler(appEvent)
    

    def publishExceptionMessage(self, message):
        event = AppEvent(type=AppEventType.exceptions, data={"message": message})
        self.onEvent(event)

    def publishException(self, e: Exception):
        event = AppEvent(type=AppEventType.exceptions, data=e)
        self.onEvent(event)