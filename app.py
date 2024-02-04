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
from library.AppEvent import AppEvent, AppEventType
from model.RecordingRepository import RecordingRepository
from view import *
from view.AnnotationEditView import AnnotationEditView
from view.TitleView import TitleView

def buttonCMD():
        print("Button clicked!")

class App(TKMT.ThemedTKinterFrame):
    def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__("PedAnalyze: Pedestrian Behavior Annotator", theme, mode, usecommandlineargs, usethemeconfigfile)
        #self.initContext()
        global firstWindow
        firstWindow = False

        self.eventManager = EventManager()
        self.viewManager = ViewManager(self.eventManager)
        self.controllerManager = ControllerManager()
        self.recordingController = self.controllerManager.getRecordingController()
        # create two widgetframes, nav and content
        self.makeNav()
        self.makeContent()
        self.makeEditor()
        # self.debugPrint()

        self.eventManager.subscribe(AppEventType.newProject, self.handleNewProject)
        self.eventManager.subscribe(AppEventType.requestAnnotation, self.handleNewAnnotation)
        self.eventManager.subscribe(AppEventType.saveProject, self.handleSaveProject)
        self.run()
    
    def makeNav(self):
        #TODO: call render titleview here I think
        self.navFrame = self.addLabelFrame("Title View", padx=(0,0), pady=(10,0))
        # self.navFrame.Button("New Project", buttonCMD)
        # self.navFrame.nextCol()
        # self.navFrame.Button("Save", buttonCMD)
        # self.navFrame.setActiveCol(0)
        # self.navFrame.Text("Recording Name")
        # self.navFrame.Text("Annotation Path")

        titleView = TitleView(self.eventManager, self.recordingController)
        titleView.render(self.navFrame)
    
    def makeContent(self):
        self.contentFrame = self.addFrame("Content", padx=(0,0), pady=(0,0))

        # left and right
        self.leftFrame = self.contentFrame.addFrame("Left", padx=(0,0), pady=(0,0))
        # self.leftFrame.Label("Left Frame")
        self.contentFrame.nextCol()
        self.rightFrame = self.contentFrame.addFrame("Right", padx=(0,0), pady=(0,0))
        # self.rightFrame.Label("Right Frame")

    
    def makeEditor(self):
         # put video player and annotation edit on the left frame
         # put recording on the right
        self.videoFrame = self.leftFrame.addLabelFrame("Video View", padx=(0,0), pady=(10,0))
        # self.createVideoView()
        
        # self.videoFrame.Text("Video")
        # self.leftFrame.Seperator()
        self.annotationFrame = self.leftFrame.addLabelFrame("Annotation Edit View", padx=(0,0), pady=(10,0))
        self.annotationEditView = self.viewManager.getAnnotationEditView(self.recordingController, self.eventManager)
        #self.context["controllers"]["recording"])
        self.annotationEditView.render(self.annotationFrame)


        self.recordingFrame = self.rightFrame.addFrame("Recording", padx=(0,0), pady=(10,0))
        text = self.recordingFrame.Text("Recording")
        # text.pack(side=tk.TOP)

    def handleNewAnnotation(self, event: AppEvent):
        print("Annotation event handled")
        self.annotationEditView.currentAnnotationStartFrame.set(self.videoView.startFrame.get())
        self.annotationEditView.currentAnnotationEndFrame.set(self.videoView.endFrame.get())

    def handleNewProject(self, event: AppEvent):
        print("New project event handled")
        # save current video if exists
        self.createVideoView(**event.data)

    def handleSaveProject(self, event: AppEvent):
        print("Save project event handled")
        self.recordingController.saveProject()
        
    def createVideoView(self, videoURL:str, videoTitle:str, annotationPath: str):
        print(f"Creating video view with url {videoURL} and title {videoTitle} and annotation path {annotationPath}")
        if not hasattr(self, 'videoView') or self.videoView is None:
            self.videoView = self.viewManager.getVideoView()
            self.videoView.render(self.videoFrame, videoURL)
        else:
            self.videoView.updateVideo(videoURL)

        self.recordingController.initNewRecording(videoTitle, annotationPath, videoURL)
    


    

if __name__ == "__main__":
        App("park", "dark")