import tkinter as tk
from tkinter import ttk
import TKinterModernThemes as TKMT
from library.AppEvent import AppEvent, AppEventType
from managers.EventManager import EventManager
from controller.RecordingController import RecordingController

class TitleView(tk.Frame):
   
    def __init__(self, eventManager: EventManager, recordingController: RecordingController, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.eventManager = eventManager
        self.recordingController = recordingController

        self.videoURL = tk.StringVar(value="")
        self.videoURL.trace_add('write', self.videoURLUpdated)
        self.parent = None
    
    def render(self, parent: TKMT.WidgetFrame):
        self.parent= parent
        # self.parent.Text("Title View")
        self.parent.setActiveCol(0)
        # self.titleFrame = self.parent.addLabelFrame("Title View", padx=(0,1), pady=(0,1))
        newProjButton = self.parent.Button(text="Add new project", command=self.renderNewProjectView)
        newProjButton.grid(row=0, column=0, padx=10, pady=10)
        saveProjButton = self.parent.Button(text="Save project", command=self.saveProject)
        saveProjButton.grid(row=0, column=1, padx=10, pady=10)
        recordingName = self.parent.Text(text="Recording Name: " + self.recordingController._recording.name)
        recordingName.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        annotationPath = self.parent.Text(text="Annotation Path: " + self.recordingController._recording.annotation_path)
        annotationPath.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        videoPath = self.parent.Text(text="Video Path: " + self.recordingController._recording.video_path)
        videoPath.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def saveProject(self):
        self.eventManager.onEvent(AppEvent(type=AppEventType.saveProject, data={}))

    def renderNewProjectView(self):
        NewProjectWindow(self, "park", "dark")

    def videoURLUpdated(self, *args):
        print("Video URL updated", self.videoURL)
        self.eventManager.onEvent(AppEvent(type=AppEventType.newProject, data={"videoURL": self.videoURL.get()}))
    
class NewProjectWindow(TKMT.ThemedTKinterFrame):
    def __init__(self, titleView: TitleView, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__("TITLE", theme, mode, usecommandlineargs, usethemeconfigfile)
        self.titleView = titleView

        self.newVideoURL = tk.StringVar(value="")
        self.newVideoURL.trace_add('write', self.videoURLUpdated)
        
        self.setActiveCol(0)
        # self.startFrame = self.parent.addLabelFrame("Start", padx=(0,1), pady=(0,1))
        self.input_frame = self.addLabelFrame("Video URL", rowspan=2)
        self.input_frame.Entry(self.newVideoURL)
        self.Button("Save", self.save)
        self.Button("Cancel", self.cancel)

    def videoURLUpdated(self, *args):
        print("Video URL updated", self.newVideoURL)
    
    def save(self):
        self.titleView.videoURL.set(self.newVideoURL.get())
        self.root.destroy()
    
    def cancel(self):
        self.root.destroy()
