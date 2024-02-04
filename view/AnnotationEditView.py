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


class AnnotationEditView(View):

    def __init__(self, recordingController: RecordingController, eventManager: EventManager, viewEventManager: ViewEventManager) -> None:
        super().__init__()
        self.eventManager = eventManager
        self.viewEventManager = viewEventManager
        self.recordingController = recordingController
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
        parent.setActiveCol(0)
        self._renderMeta(parent)
        
        parent.setActiveCol(0)
        self._renderAnnotationTypeSelector(parent)

        parent.setActiveCol(0)
        self.pedBehaviorFrame = parent.addLabelFrame("Pedestrian Behavior", padx=(10,10), pady=(10, 0))
        self._renderPedOptions(self.pedBehaviorFrame)

        parent.setActiveCol(0)
        self.vehBehaviorFrame = parent.addLabelFrame("Vehicle Behavior", padx=(10,10), pady=(10, 0))
        self._renderVehicleOptions(self.vehBehaviorFrame)

        parent.setActiveCol(0)
        self.envBehaviorFrame = parent.addLabelFrame("Environment Behavior", padx=(10,10), pady=(10, 0))
        self._renderSceneOptions(self.envBehaviorFrame)

        parent.setActiveCol(0)
        self._renderNotesField(parent)
        self._renderSaveButton(parent)

        # add radio button for single/multi
        # frame # being annotated
        
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
            PedestrianTag.Flinch,
            PedestrianTag.Crash,
            PedestrianTag.Jaywalking,
            PedestrianTag.Distracted,
            PedestrianTag.NoLook,
        ]

        self.behaviorCheckVars = [tk.BooleanVar(name=option.value) for option in options]
        col = 0
        self.pedCheckbuttons = []
        for option, var in zip(options, self.behaviorCheckVars):
            parent.Checkbutton(option.value, var, self.behaviorChangeHandler, (option, var), col=col) 
            self.pedCheckbuttons.append(var)
            col += 1
            # the behaviorChangeHandler is called whenever a checkbox is pressed with the associated option and var

    def _renderVehicleOptions(self, parent: TKMT.WidgetFrame):
        options = [
            VehicleTag.Brake,
            VehicleTag.Speeding,
            VehicleTag.RunRed,
            VehicleTag.Distracted
        ]

        self.behaviorCheckVars = [tk.BooleanVar(name=option.value) for option in options]
        col = 0
        self.vehicleCheckbuttons = []
        for option, var in zip(options, self.behaviorCheckVars):
            parent.Checkbutton(option.value, var, self.egoBehaviorChangeHandler, (option, var), col=col) 
            self.vehicleCheckbuttons.append(var)
            col += 1

    def _renderSceneOptions(self, parent: TKMT.WidgetFrame):
        options = [
            SceneTag.RedLight,
            SceneTag.ChangingLight,
            SceneTag.NoSigns,
            SceneTag.NoLight
        ]

        self.behaviorCheckVars = [tk.BooleanVar(name=option.value) for option in options]
        col = 0
        self.sceneCheckbuttons = []
        for option, var in zip(options, self.behaviorCheckVars):
            parent.Checkbutton(option.value, var, self.envBehaviorChangeHandler, (option, var), col=col) 
            self.sceneCheckbuttons.append(var)
            col += 1

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
            self.recordingController.addMultiFrameAnnotation(newAnnotation)

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

        self.notesVar.set("")
            
        print("annotation reset")

