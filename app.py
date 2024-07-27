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
from managers.ViewEventManager import ViewEventManager
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
        firstWindow = False  # super important for popups
        
        
        # Instantiating Style class 
        self.style = ttk.Style(self.master)
        self.fontsize = 12
        # Changing font-size of all the Label Widget 
        self.style.configure("TLabel", font=('Arial', self.fontsize))
        self.style.configure("TEntry", font=('Arial', self.fontsize)) 
        
        self.style.configure("TButton", font=('Arial', self.fontsize)) 
        self.style.configure("TCheckbutton", font=('Arial', self.fontsize)) 
        self.style.configure("TRadiobutton", font=('Arial', self.fontsize))
        
        self.style.configure("TFrame", font=('Arial', self.fontsize)) 
        self.style.configure("TLabelFrame", font=('Arial', self.fontsize)) 
        self.style.configure("TCombobox", font=('Arial', self.fontsize)) 
        self.style.configure("TLabelFrame", font=('Arial', self.fontsize)) 
        self.style.configure("TMenubutton", font=('Arial', self.fontsize)) 

        self.eventManager = EventManager()
        self.viewEventManager = ViewEventManager(self.eventManager)
        self.viewManager = ViewManager(self.eventManager, self.viewEventManager)
        self.controllerManager = ControllerManager(self.eventManager)
        self.recordingController = self.controllerManager.getRecordingController()
        # create two widgetframes, nav and content
        self.makeNav()
        self.makeContent()
        self.makeEditor()
        # self.debugPrint()

        self.eventManager.subscribe(AppEventType.newProject, self.handleNewProject)
        self.eventManager.subscribe(AppEventType.requestAnnotation, self.handleNewAnnotation)
        self.eventManager.subscribe(AppEventType.saveProject, self.handleSaveProject)
        self.eventManager.subscribe(AppEventType.exceptions, self.handleException)
        
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

        # titleView = TitleView(self.eventManager, self.recordingController)
        titleView = self.viewManager.getTitleView(self.recordingController)
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
        # self.annotationFrame = self.leftFrame.addLabelFrame("Annotation Edit View", padx=(0,0), pady=(10,0))
        # self.annotationEditView = self.viewManager.getAnnotationEditView(self.recordingController)
        # #self.context["controllers"]["recording"])
        # self.annotationEditView.render(self.annotationFrame)
        self.behaviorTagFrame = self.leftFrame.addLabelFrame("Behavior Tag Frame", padx=(0,0), pady=(10,0))
        self.behaviorTagView = self.viewManager.getBehaviorTagView()
        self.behaviorTagView.render(self.behaviorTagFrame)

        self.recordingFrame = self.rightFrame.addFrame("Recording", padx=(0,0), pady=(10,0))
        self.recordingView = self.viewManager.getRecordingView(self.recordingController)
        self.recordingView.render(self.recordingFrame)
        # text = self.recordingFrame.Text("Recording")
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
        status, message = self.recordingController.saveProject()
        PopupView(message, "park", "dark")
    
    def handleException(self, event: AppEvent):
        print("Exception event handled")
        if isinstance(event.data, Exception):
            PopupView(str(event.data), "park", "dark")
        else:
            PopupView(event.data["message"], "park", "dark")
        
    def createVideoView(self, videoURL:str, videoTitle:str, annotationPath: str):
        self.recordingController.initNewRecording(videoTitle, None, annotationPath, videoURL)
        print(f"Creating video view with url {videoURL} and title {videoTitle} and annotation path {annotationPath}")
        if not hasattr(self, 'videoView') or self.videoView is None:
            self.videoView = self.viewManager.getVideoView()
            self.videoView.render(self.videoFrame, videoURL)
        else:
            self.videoView.updateVideo(videoURL)

    

    


    

if __name__ == "__main__":
        App("park", "dark")