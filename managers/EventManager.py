
from library import AppEvent
from library.AppEvent import AppEventType
from typing import Callable

class EventManager:
    def __init__(self) -> None:
        
        ### event streams
        self.initEventStreams()
        pass

    def initEventStreams(self):
         self.annotateFrameHandlers = [] # kust if functions to be called when a annotation is requested
         self.newProjectHandlers = []

         
    def unsubscribe(self, appEvent: AppEventType, handler: Callable):
        if appEvent == AppEventType.requestAnnotation:
            self.annotateFrameHandlers.remove(handler)
        if appEvent == AppEventType.newProject:
            self.newProjectHandlers.remove(handler)

    
    def subscribe(self, appEvent: AppEventType, handler: Callable):
        if appEvent == AppEventType.requestAnnotation:
            self.annotateFrameHandlers.append(handler)
        if appEvent == AppEventType.newProject:
            self.newProjectHandlers.append(handler)
    
    def onEvent(self, appEvent: AppEvent):
        # if appEvent.type == AppEventType.requestAnnotation:
        #     # self.annotationFrame = self.leftFrame.addLabelFrame("Annotation Edit View", padx=(0,0), pady=(0,0))
        #     # annotationView = AnnotationEditView(self.context["controllers"]["recording"])
        #     # annotationView.render(self.annotationFrame, 5, 100)
        #     print("requestAnnotation event will be handled")
             
        #     # for handler in self.annotateFrameHandlers:
        #     #     handler(appEvent.data["timestamp"], appEvent.data["frame"])
        # if appEvent.type == AppEventType.newProject:
        #     handlers = self.annotateFrameHandlers[appEvent.type]
        if appEvent.type == AppEventType.requestAnnotation:
            for handler in self.annotateFrameHandlers:
                handler(appEvent)

        if appEvent.type == AppEventType.newProject:
            for handler in self.newProjectHandlers:
                handler(appEvent)