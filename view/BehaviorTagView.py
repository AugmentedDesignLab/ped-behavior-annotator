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


class BehaviorTagView(View):

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
        # self.egoTags: List[VehicleTag] = []
        # self.sceneTags: List[SceneTag] = []
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

        self.notebook = parent.Notebook("Behavior Tag View")

        self.tabPedestrianBehavior = self.notebook.addTab("Pedestrian Behavior")

        # Create a canvas
        self.canvasPedestrianBehavior = tk.Canvas(self.tabPedestrianBehavior.master)
        self.canvasPedestrianBehavior.pack(side="left", fill="both", expand=True)
        # Create a vertical scrollbar
        scrollbarPedestrianBehavior = ttk.Scrollbar(self.canvasPedestrianBehavior, orient="vertical", command=self.canvasPedestrianBehavior.yview)
        scrollbarPedestrianBehavior.pack(side="right", fill="y")
        self.canvasPedestrianBehavior.configure(yscrollcommand=scrollbarPedestrianBehavior.set)
        # Create a frame to hold widgets
        self.innerFramePedestrianBehavior = ttk.Frame(self.canvasPedestrianBehavior)
        self.framePedestrianBehavior = TKMT.WidgetFrame(self.innerFramePedestrianBehavior, "Pedestrian Behaviors")
        innerFrameIDPedestrianBehavior = self.canvasPedestrianBehavior.create_window((0, 0), window=self.innerFramePedestrianBehavior, anchor="nw")

        # Bind function to configure
        self.canvasPedestrianBehavior.bind("<Configure>", self.on_configure_pedestrian_behavior)
        # Call on_configure once to set up the initial scrolling region
        self.on_configure_pedestrian_behavior(None)

        # Render checkboxes
        self._renderPedOptions(self.framePedestrianBehavior)

        self.tabVehicleBehavior = self.notebook.addTab("Vehicle Behavior")

        # Create a canvas
        self.canvasVehicleBehavior = tk.Canvas(self.tabVehicleBehavior.master)
        self.canvasVehicleBehavior.pack(side="left", fill="both", expand=True)
        # Create a vertical scrollbar
        scrollbarVehicleBehavior = ttk.Scrollbar(self.canvasVehicleBehavior, orient="vertical", command=self.canvasVehicleBehavior.yview)
        scrollbarVehicleBehavior.pack(side="right", fill="y")
        self.canvasVehicleBehavior.configure(yscrollcommand=scrollbarVehicleBehavior.set)
        # Create a frame to hold widgets
        self.innerFrameVehicleBehavior = ttk.Frame(self.canvasVehicleBehavior)
        self.frameVehicleBehavior = TKMT.WidgetFrame(self.innerFrameVehicleBehavior, "Vehicle Behaviors")
        innerFrameIDVehicleBehavior = self.canvasVehicleBehavior.create_window((0, 0), window=self.innerFrameVehicleBehavior, anchor="nw")

        # Bind function to configure
        self.canvasVehicleBehavior.bind("<Configure>", self.on_configure_vehicle_behavior)
        # Call on_configure once to set up the initial scrolling region
        self.on_configure_vehicle_behavior(None)

        # Render checkboxes
        self._renderVehicleOptions(self.frameVehicleBehavior)
    
        self.tabEnvironmentConditions = self.notebook.addTab("Environment Conditions")

        # Create a canvas
        self.canvasEnvironmentConditions = tk.Canvas(self.tabEnvironmentConditions.master)
        self.canvasEnvironmentConditions.pack(side="left", fill="both", expand=True)
        # Create a vertical scrollbar
        scrollbarEnvironmentConditions = ttk.Scrollbar(self.canvasEnvironmentConditions, orient="vertical", command=self.canvasEnvironmentConditions.yview)
        scrollbarEnvironmentConditions.pack(side="right", fill="y")
        self.canvasEnvironmentConditions.configure(yscrollcommand=scrollbarEnvironmentConditions.set)
        # Create a frame to hold widgets
        self.innerFrameEnvironmentConditions = ttk.Frame(self.canvasEnvironmentConditions)
        self.frameEnvironmentConditions = TKMT.WidgetFrame(self.innerFrameEnvironmentConditions, "Vehicle Behaviors")
        innerFrameIDEnvironmentConditions = self.canvasEnvironmentConditions.create_window((0, 0), window=self.innerFrameEnvironmentConditions, anchor="nw")

        # Bind function to configure
        self.canvasEnvironmentConditions.bind("<Configure>", self.on_configure_environment_conditions)
        # Call on_configure once to set up the initial scrolling region
        self.on_configure_environment_conditions(None)
        
        self._renderSceneOptions(self.frameEnvironmentConditions)

        def on_mousewheel_pedestrian_behavior(event):
            self.canvasPedestrianBehavior.yview_scroll(int(-1 * (event.delta / 120)), "units")
        def on_mousewheel_vehicle_behavior(event):
            self.canvasVehicleBehavior.yview_scroll(int(-1 * (event.delta / 120)), "units")
        def on_mousewheel_environment_conditions(event):
            self.canvasEnvironmentConditions.yview_scroll(int(-1 * (event.delta / 120)), "units")

        # Bind the mouse wheel event to the canvas
        self.canvasPedestrianBehavior.bind("<MouseWheel>", on_mousewheel_pedestrian_behavior)
        self.canvasVehicleBehavior.bind("<MouseWheel>", on_mousewheel_vehicle_behavior)
        self.canvasEnvironmentConditions.bind("<MouseWheel>", on_mousewheel_environment_conditions)

        # add radio button for single/multi
        # frame # being annotated

    # Function to update the canvas scrolling region
    def on_configure_pedestrian_behavior(self, event):
        self.canvasPedestrianBehavior.configure(scrollregion=self.canvasPedestrianBehavior.bbox("all"))
    def on_configure_vehicle_behavior(self, event):
        self.canvasVehicleBehavior.configure(scrollregion=self.canvasVehicleBehavior.bbox("all"))
    def on_configure_environment_conditions(self, event):
        self.canvasEnvironmentConditions.configure(scrollregion=self.canvasEnvironmentConditions.bbox("all"))
        
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
        self.pedCheckbuttons = []
        for option, var in zip(options, self.behaviorCheckVars):
            parent.Checkbutton(option.value, var, self.behaviorChangeHandler, (option, var), row=row, col=col) 
            self.pedCheckbuttons.append(var)
            col += 1
            if col == 5:
                row += 1
                col = 0
            # the behaviorChangeHandler is called whenever a checkbox is pressed with the associated option and var
        return row, col

    def _renderVehicleOptions(self, parent: TKMT.WidgetFrame):
        options = [
            VehicleTag.SpeedUp,
            VehicleTag.SlowDown,
            VehicleTag.GradualSpeedUp,
            VehicleTag.GradualSlowDown,
            VehicleTag.SlowReverse,
            VehicleTag.QuickReverse,
            VehicleTag.LaneChange,
            VehicleTag.Speeding,
            VehicleTag.Halt,
            VehicleTag.InducedCollision,
            VehicleTag.RunStop,
            VehicleTag.Swerve,
            VehicleTag.MakeGo,
            VehicleTag.Sidewalk
        ]

        self.behaviorCheckVars = [tk.BooleanVar(name=option.value) for option in options]
        row = 0
        col = 0
        self.vehicleCheckbuttons = []
        for option, var in zip(options, self.behaviorCheckVars):
            parent.Checkbutton(option.value, var, self.egoBehaviorChangeHandler, (option, var), row=row, col=col) 
            self.vehicleCheckbuttons.append(var)
            col += 1
            if col == 5:
                row += 1
                col = 0

    def _renderSceneOptions(self, parent: TKMT.WidgetFrame):
        options = [
            SceneTag.Day,
            SceneTag.Night,
            SceneTag.Sunny,
            SceneTag.Foggy,
            SceneTag.Cloudy,
            SceneTag.Snowy,
            SceneTag.NoTrafficLight,
            SceneTag.GreenTrafficLight,
            SceneTag.YellowTrafficLight,
            SceneTag.BlinkingYellowTrafficLight,
            SceneTag.RedTrafficLight,
            SceneTag.StopSign,
            SceneTag.Crosswalk,
            SceneTag.NoCrosswalk,
            SceneTag.Roundabout,
            SceneTag.LightTraffic,
            SceneTag.ModerateTraffic,
            SceneTag.HeavyTraffic,
            SceneTag.OneWayTraffic,
            SceneTag.TwoWayTraffic,
            SceneTag.OccludedPedestrian,
            SceneTag.GlareOnWindshield
        ]

        self.behaviorCheckVars = [tk.BooleanVar(name=option.value) for option in options]
        row = 0
        col = 0
        self.sceneCheckbuttons = []
        for option, var in zip(options, self.behaviorCheckVars):
            parent.Checkbutton(option.value, var, self.envBehaviorChangeHandler, (option, var), row = row, col=col) 
            self.sceneCheckbuttons.append(var)
            col += 1
            if col == 5:
                row += 1
                col = 0

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

    def egoBehaviorChangeHandler(self, option: VehicleTag, var: tk.BooleanVar):
        # print("Checkbox number:", option, "was pressed")
        # print("Checkboxes: ", var.get())
        if var.get():
            self.egoTags.append(option)
        else:
            self.egoTags.remove(option)

    def envBehaviorChangeHandler(self, option: SceneTag, var: tk.BooleanVar):
        # print("Checkbox number:", option, "was pressed")
        # print("Checkboxes: ", var.get())
        if var.get():
            self.sceneTags.append(option)
        else:
            self.sceneTags.remove(option)

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
        self.egoTags = []
        self.sceneTags = []

        for var in self.pedCheckbuttons:
            var.set(False)
        for var in self.vehicleCheckbuttons:
            var.set(False)
        for var in self.sceneCheckbuttons:
            var.set(False)

        #self.notesVar.set("")
            
        print("annotation reset")