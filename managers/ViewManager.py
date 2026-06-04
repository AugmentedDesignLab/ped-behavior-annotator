"""The purpose of this manager is to intantiate all the view objects and supply it to the user of the objects
"""
from controller.RecordingController import RecordingController
from controller.VideoController import VideoController
from managers.EventManager import EventManager
from managers.ViewEventManager import ViewEventManager
from view.RecordingView import RecordingView
from view.AnnotationEditView import AnnotationEditView
from view.VideoView import VideoView
from view.TitleView import TitleView
from view.BehaviorTagView import BehaviorTagView
from library.AppEvent import *
#from view import *
class ViewManager:

    def __init__(self, eventManager: EventManager, viewEventManager) -> None:
        self.eventManager = eventManager
        self.viewEventManager = viewEventManager

    def getAnnotationEditView(self, recordingController: RecordingController): 
        view = AnnotationEditView(recordingController, self.eventManager, self.viewEventManager)
        self.eventManager.subscribe(AppEventType.annotationEditView, view.handleEvent)
        return view
    
    def getRecordingView(self, recordingController: RecordingController): 
        view = RecordingView(recordingController, self.eventManager, self.viewEventManager)
        self.eventManager.subscribe(AppEventType.recording, view.handleEvent)
        return view
        
    def getVideoView(self):
        view = VideoView(self.eventManager, self.viewEventManager)
        self.eventManager.subscribe(AppEventType.videoView, view.handleEvent)
        return view

    def getTitleView(self, recordingController: RecordingController):
        return TitleView(recordingController, self.eventManager, self.viewEventManager)
    
    def getBehaviorTagView(self): 
        view = BehaviorTagView(self.eventManager, self.viewEventManager)
        #self.eventManager.subscribe(AppEventType.BehaviorTagView, view.handleEvent)
        return view
