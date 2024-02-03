from base64 import urlsafe_b64encode
from controller.RecordingController import RecordingController
from controller.VideoController import VideoController
#from controller.YoutubeController import YoutubeController
from model.RecordingRepository import RecordingRepository

class ControllerManager: 
        
    def __init__(self) -> None:
        self.initContext()

    def initContext(self) -> None:
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

    def getRecordingController(self) -> RecordingController:
        return self.context["controllers"]["recording"]
    
    #def getVideoController(self, url) -> VideoController:
        #youtubeController = YoutubeController(url)
        #return youtubeController