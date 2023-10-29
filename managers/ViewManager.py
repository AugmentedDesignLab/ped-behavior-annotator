"""The purpose of this manager is to intantiate all the view objects and supply it to the user of the objects
"""
from controller.RecordingController import RecordingController
from controller.VideoController import VideoController
from view import RecordingView
from view.AnnotationEditView import AnnotationEditView
from view.VideoView import VideoView
#from view import *
class ViewManager:

    def getAnnotationView(self, recordingController: RecordingController): 
        return AnnotationEditView(recordingController)
        
    def getVideoView(self, videoController: VideoController):
        return VideoView(videoController)
