import tkinter as tk
from tkinter import *
from tkinter import ttk
import TKinterModernThemes as TKMT
from TKinterModernThemes.WidgetFrame import Widget
from controller.RecordingController import RecordingController
from model.PedestrianTag import PedestrianTag
from model.SceneTag import SceneTag
from model.VehicleTag import VehicleTag
from model.SingleFrameAnnotation import SingleFrameAnnotation
from model.MultiFrameAnnotation import MultiFrameAnnotation
from library.AppEvent import AppEvent, AppEventType
from managers.EventManager import EventManager
from managers.ViewEventManager import ViewEventManager
import allwidgets
import cv2
from typing import *

from view.View import View


class PedestrianTagView(View):

    def __init__(self, eventManager: EventManager, viewEventManager: ViewEventManager) -> None:
        super().__init__()
        self.eventManager = eventManager
        self.viewEventManager = viewEventManager
        self.currentAnnotationStartFrame = tk.IntVar(value=0)
        self.currentAnnotationEndFrame = tk.IntVar(value=0)
        self.annotationTypeRadioVar = tk.StringVar(value='Multi')

    def handleEvent(self, appEvent: AppEvent):
        if "updateStartFrame" in appEvent.data:
            self.currentAnnotationStartFrame.set(appEvent.data["updateStartFrame"])
            print(f"updated start frame in the edit view with {appEvent.data['updateStartFrame']} == {self.currentAnnotationStartFrame.get()}")
        if "updateEndFrame" in appEvent.data:
            self.currentAnnotationEndFrame.set(appEvent.data["updateEndFrame"])
            print("updated end frame in the edit view")

    def render(self, parent: TKMT.WidgetFrame):
        # frame information
        # self.pedTags: List[PedestrianTag] = []
        self._renderView(parent)
        self.resetAnnotation()

    def renderSingleEdit(self, parent: TKMT.WidgetFrame, existingAnnotation: SingleFrameAnnotation):
        # you do the same thing, but read information from the existingAnnotation object
        self.currentAnnotation = existingAnnotation
        self._renderView(parent)
    
    def _renderView(self, parent: TKMT.WidgetFrame):
        # parent.Text("Frame # " + str(self.currentAnnotation.frame))
        # parent.setActiveCol(0)
        # self._renderMeta(parent)
        
        # parent.setActiveCol(0)
        # self._renderAnnotationTypeSelector(parent)

        # parent.setActiveCol(0)
        # self.pedBehaviorFrame = parent.addLabelFrame("Pedestrian Behavior", padx=(10,10), pady=(10, 0))
        # self._renderPedOptions(self.pedBehaviorFrame)

        # parent.setActiveCol(0)
        # self.vehBehaviorFrame = parent.addLabelFrame("Vehicle Behavior", padx=(10,10), pady=(10, 0))
        # self._renderVehicleOptions(self.vehBehaviorFrame)

        # parent.setActiveCol(0)
        # self.envBehaviorFrame = parent.addLabelFrame("Environment Behavior", padx=(10,10), pady=(10, 0))
        # self._renderSceneOptions(self.envBehaviorFrame)

        # parent.setActiveCol(0)
        # self._renderNotesField(parent)
        # self._renderSaveButton(parent)

        self.pane = parent.PanedWindow("Behavior Tag View")
        self.panePedestrianBehavior = self.pane.addWindow()

        # Create a canvas
        self.canvasPedestrianBehavior = tk.Canvas(self.panePedestrianBehavior.master)
        self.canvasPedestrianBehavior.pack(side="left", fill="both", expand=True)
        # Create a vertical scrollbar
        scrollbarPedestrianBehavior = ttk.Scrollbar(self.canvasPedestrianBehavior, orient="vertical", command=self.canvasPedestrianBehavior.yview)
        scrollbarPedestrianBehavior.pack(side="right", fill="y")
        self.canvasPedestrianBehavior.configure(yscrollcommand=scrollbarPedestrianBehavior.set)
        # Create a frame to hold widgets
        self.innerFrame = ttk.Frame(self.canvasPedestrianBehavior)
        self.framePedestrianBehavior = TKMT.WidgetFrame(self.innerFrame, "Pedestrian Behaviors")
        innerFrameID = self.canvasPedestrianBehavior.create_window((0, 0), window=self.innerFrame, anchor="nw")
        
        # Render checkboxes
        self._renderPedOptions(self.framePedestrianBehavior)

        # Bind function to configure
        self.canvasPedestrianBehavior.bind("<Configure>", self.on_configure_pedestrian_behavior)
        # Call on_configure once to set up the initial scrolling region
        self.on_configure_pedestrian_behavior(None)

        def on_mousewheel(event):
            self.canvasPedestrianBehavior.yview_scroll(int(-1 * (event.delta / 120)), "units")

        # Bind the mouse wheel event to the canvas
        self.canvasPedestrianBehavior.bind("<MouseWheel>", on_mousewheel)

        # add radio button for single/multi
        # frame # being annotated

    # Function to update the canvas scrolling region
    def on_configure_pedestrian_behavior(self, event):
        self.canvasPedestrianBehavior.configure(scrollregion=self.canvasPedestrianBehavior.bbox("all"))
        
    def _renderMeta(self, parent: TKMT.WidgetFrame):
        self.metaFrame = parent.addLabelFrame("Frame Info", padx=(10,10), pady=(10, 0))
        sticky=tk.W 

        self.metaFrame.Text("Start Frame:", row=0, col=0, sticky=tk.E)
        self.metaFrame.Text(text="0", widgetkwargs={"textvariable":self.currentAnnotationStartFrame}, row=0, col=1, sticky=tk.W)
        self.metaFrame.Text("End Frame:", row=0, col=2, sticky=tk.E)
        self.metaFrame.Text(text="0", widgetkwargs={"textvariable":self.currentAnnotationEndFrame}, row=0, col=3, sticky=tk.W)

    def _renderAnnotationTypeSelector(self, parent: TKMT.WidgetFrame):
        self.annotationTypeFrame = parent.addLabelFrame("Annotation Type", padx=(10,10), pady=(10, 0))
        self.annotationTypeFrame.Radiobutton("Multi", self.annotationTypeRadioVar, value="Multi", row=0, col=0)
        self.annotationTypeFrame.Radiobutton("Single", self.annotationTypeRadioVar, value="Single", row=0, col=1)              

    def _renderPedOptions(self, parent: TKMT.WidgetFrame):
        options = [
            PedestrianTag.Trip,
            PedestrianTag.AloneLane,
            PedestrianTag.BriskWalk,
            PedestrianTag.GroupWalk,
            PedestrianTag.GroupDisperse,
            PedestrianTag.DogWalk,
            PedestrianTag.Retreat,
            PedestrianTag.SpeedUp,
            PedestrianTag.SlowDown,
            PedestrianTag.Wander,
            PedestrianTag.PauseStart,
            PedestrianTag.Jaywalking,
            PedestrianTag.CrossOnRed,
            PedestrianTag.Swerve,
            PedestrianTag.Break,
            PedestrianTag.FlinchOut,
            PedestrianTag.FlinchIn,
            PedestrianTag.Frozen,
            PedestrianTag.Collision,
            PedestrianTag.NearMiss,
            PedestrianTag.RunIntoTraffic,
            PedestrianTag.ThrownBack,
            PedestrianTag.MakeStop,
            PedestrianTag.MakeGo,
            PedestrianTag.Aggression,
            PedestrianTag.Observing,
            PedestrianTag.Looking,
            PedestrianTag.Glancing,
            PedestrianTag.NotLookingGlancing,
            PedestrianTag.Distracted,
            PedestrianTag.Agitated,
            PedestrianTag.Cautious,
            PedestrianTag.Indecisive,
            PedestrianTag.Cross,
            PedestrianTag.NotCross,
            PedestrianTag.NotSureCross
        ]


        self.behaviorCheckVars = [tk.BooleanVar(name=option.value) for option in options]
        row = 0
        col = 0

        #Adding a SearchBar 
        self.searchBarLabel = parent.Label("Search Tag: ", row=row, col=col)
        #self.searchBarLabel.pack(pady = 20)
        col+=1
        self.prevlaue = ''
        self.searchEntry = parent.Entry(self, row=row, col=col)
        self.searchEntry.bind("<KeyRelease>", self.OnEntryClick)
        
        row+=1
        col=0
        self.pedCheckbuttons =   []
        for option, var in zip(options, self.behaviorCheckVars):
            parent.Checkbutton(option.value, var, self.behaviorChangeHandler, (option, var), row=row, col=col) 
            self.pedCheckbuttons.append(var)
            col += 1
            if col == 5:
                row += 1
                col = 0
            # the behaviorChangeHandler is called whenever a checkbox is pressed with the associated option and var
        return row, col
    
    def OnEntryClick(self, event):
        value=self.searchEntry.get().strip()
        changed = True if self.prevlaue != value else False
        print(value, 'Text has changed ? {}'.format(changed))
        self.prevlaue = value
        self.vehicleCheckbuttons.clear()
        print(self.vehicleCheckbuttons)

    def _renderNotesField(self, parent: TKMT.WidgetFrame):

        parent.Text("Additional Notes:", col=1, row=0)
        # parent.nextCol()

        self.notesVar = tk.StringVar()
        parent.Entry(
            self.notesVar,
            col=1,
            row=1,
            rowspan=3
            )

    def _renderSaveButton(self, parent: TKMT.WidgetFrame):
        self.togglebuttonvar = tk.BooleanVar()
        parent.Button("Save Annotation", self.handleSave)
    

    def behaviorChangeHandler(self, option: PedestrianTag, var: tk.BooleanVar):
        # print("Checkbox number:", option, "was pressed")
        # print("Checkboxes: ", var.get())
        if var.get():
            self.pedTags.append(option)
        #update the currentAnnotation object's tags
        else:
            self.pedTags.remove(option)

    def handleSave(self):
        print("Button clicked. Current toggle button state: ", self.togglebuttonvar.get())

        # self.eventManager.onEvent(AppEvent(type=AppEventType.requestAnnotation, data={}))

        if self.annotationTypeRadioVar.get() == "Single":
            newAnnotation = SingleFrameAnnotation(self.currentAnnotationStartFrame.get(),
                                                      self.pedTags,
                                                      self.egoTags,
                                                      self.sceneTags,
                                                      self.notesVar.get())
            self.recordingController.addSingleFrameAnnotation(newAnnotation) # must be an event
        else:
            newAnnotation = MultiFrameAnnotation(self.currentAnnotationStartFrame.get(),
                                                     self.currentAnnotationEndFrame.get(),
                                                     self.pedTags,
                                                     self.egoTags,
                                                     self.sceneTags,
                                                     self.notesVar.get())
            self.recordingController.addMultiFrameAnnotation(newAnnotation) # TODO, this is anti pattern.

        self.viewEventManager.publishNewAnnotation(newAnnotation)
        self.resetAnnotation()

    def resetAnnotation(self):
        self.pedTags = []

        for var in self.pedCheckbuttons:
            var.set(False)
        
        #self.notesVar.set("")
            
        print("annotation reset")



