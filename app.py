import tkinter as tk
from tkinter import ttk
from typing import Callable
from TKinterModernThemes.WidgetFrame import Widget
import TKinterModernThemes as TKMT
from controller.RecordingController import RecordingController
from controller.VideoController import VideoController
from controller.YoutubeController import YoutubeController
from managers.ControllerManager import ControllerManager
from managers.EventManager import EventManager
from managers.ViewManager import ViewManager
from model.RecordingRepository import RecordingRepository
from view import *
from view.AnnotationEditView import AnnotationEditView
from view.TitleView import TitleView

def buttonCMD():
        print("Button clicked!")

class App(TKMT.ThemedTKinterFrame):
    def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__("TITLE", theme, mode, usecommandlineargs, usethemeconfigfile)
        #self.initContext()
        global firstWindow
        firstWindow = False

        self.eventManager = EventManager()
        self.viewManager = ViewManager(self.eventManager)
        self.controllerManager = ControllerManager()
        # create two widgetframes, nav and content
        self.makeNav()
        self.makeContent()
        self.makeEditor()
        # self.debugPrint()
        self.run()
    
    def makeNav(self):
        #TODO: call render titleview here I think
        self.navFrame = self.addFrame("Nav")
        self.navFrame.Button("New Project", buttonCMD)
        self.navFrame.nextCol()
        self.navFrame.Button("Save", buttonCMD)
        self.navFrame.setActiveCol(0)
        self.navFrame.Text("Recording Name")
        self.navFrame.Text("Annotation Path")

        titleView = TitleView()
        titleView.render(self.navFrame)
    
    def makeContent(self):
        self.contentFrame = self.addFrame("Content", padx=(0,0), pady=(0,0))

        # left and right
        self.leftFrame = self.contentFrame.addFrame("Left", padx=(0,0), pady=(0,0))
        self.leftFrame.Label("Left Frame")
        self.contentFrame.nextCol()
        self.rightFrame = self.contentFrame.addFrame("Right", padx=(0,0), pady=(0,0))
        self.rightFrame.Label("Right Frame")

    
    def makeEditor(self):
         # put video player and annotation edit on the left frame
         # put recording on the right
        self.videoFrame = self.leftFrame.addFrame("Video", padx=(0,0), pady=(0,0))
        videoView = self.viewManager.getVideoView()
        videoView.render(self.videoFrame)
        # self.videoFrame.Text("Video")
        # self.leftFrame.Seperator()
        self.annotationFrame = self.leftFrame.addLabelFrame("Annotation Edit View", padx=(0,0), pady=(0,0))
        recordController = self.controllerManager.getRecordingController()
        annotationView = self.viewManager.getAnnotationView(recordController)
        #self.context["controllers"]["recording"])
        annotationView.render(self.annotationFrame, 5, 100)


        self.recordingFrame = self.rightFrame.addFrame("Recording", padx=(0,0), pady=(0,0))
        text = self.recordingFrame.Text("Recording")
        # text.pack(side=tk.TOP)


        sampleView = SampleView()
        sampleView.render(self.videoFrame)


    def makeVideoController(self) -> VideoController:
        youtubeController = YoutubeController("https://www.youtube.com/watch?v=eu4QqwsfXFE")
        return youtubeController



    

if __name__ == "__main__":
        App("park", "dark")