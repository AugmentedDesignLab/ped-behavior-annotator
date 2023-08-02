from controller.VideoController import VideoController


class YoutubeController(VideoController):
    def __init__(self, url: str) -> None:

        # read the video and create the capture object
        capture = None
        super().__init__(capture)