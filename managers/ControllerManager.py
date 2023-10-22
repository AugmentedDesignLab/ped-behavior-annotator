from controller.RecordingController import RecordingController
from controller.VideoController import VideoController
from controller.YoutubeController import YoutubeController
from model import RecordingRepository


class ControllerManager: 

    def __init__(self):
        self.initContext(self)
        
    def initContext(self):
        ### Set up all the global objects #
        recordingRepo = RecordingRepository("./data")
        
        self.context = {
            "controllers": {
                "recording": RecordingController(recordingRepo),
            },
            "repositoryies": {
                 "recording": recordingRepo,
            }
            
        }

    def getRecordingController(self):
        return self.context["controllers"]["recording"]
    
    def makeVideoController(self) -> VideoController:
        youtubeController = YoutubeController("https://www.youtube.com/watch?v=eu4QqwsfXFE")
        return youtubeController
