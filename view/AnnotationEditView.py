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
import allwidgets
import cv2
from typing import Tuple

from view.View import View


class AnnotationEditView(View):

    def __init__(self, recordingController: RecordingController, eventManager: EventManager) -> None:
        super().__init__()
        self.eventManager = eventManager
        self.recordingController = recordingController
        self.currentAnnotationStartFrame = tk.IntVar(value=0)
        self.currentAnnotationEndFrame = tk.IntVar(value=0)
    
    def _renderView(self, parent: TKMT.WidgetFrame):
        # parent.Text("Frame # " + str(self.currentAnnotation.frame))
        parent.setActiveCol(0)
        self.pedBehaviorFrame = parent.addLabelFrame("Pedestrian Behavior", padx=(0,0), pady=(10,0))
        self._renderPedOptions(self.pedBehaviorFrame)
        self.vehBehaviorFrame = parent.addLabelFrame("Vehicle Behavior", padx=(0,0), pady=(5,0))
        self._renderVehicleOptions(self.vehBehaviorFrame)
        self.envBehaviorFrame = parent.addLabelFrame("Environment Behavior", padx=(0,0), pady=(5,0))
        self._renderSceneOptions(self.envBehaviorFrame)
        self._renderTextField(parent)
        self._renderSaveButton(parent)


    def render(self, parent: TKMT.WidgetFrame):
        # frame information
        self.pedTags = [PedestrianTag]
        self.egoTags = [VehicleTag]
        self.sceneTags = [SceneTag]
        self._renderView(parent)

    def renderSingleEdit(self, parent: TKMT.WidgetFrame, existingAnnotation: SingleFrameAnnotation):
        # you do the same thing, but read information from the existingAnnotation object
        self.currentAnnotation = existingAnnotation
        self._renderView(parent)

    
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

    def _renderTextField(self, parent: TKMT.WidgetFrame):

        parent.Text("Additional Notes:", col=1, row=0)
        # parent.nextCol()

        self.textinputvar = tk.StringVar()
        self.textinputvar.trace_add('write', self.textupdate)
        parent.Entry(
            self.textinputvar,
            validatecommand=self.validateText, 
            validatecommandargs=(self.textinputvar,),
            col=1,
            row=1,
            rowspan=3
            )

    def _renderSaveButton(self, parent: TKMT.WidgetFrame):
        self.togglebuttonvar = tk.BooleanVar()
        parent.Button("Save Annotation", self.handleSave)

    def behaviorChangeHandler(self, option: PedestrianTag, var: tk.BooleanVar):
        print("Checkbox number:", option, "was pressed")
        print("Checkboxes: ", var.get())
        if var.get():
            self.pedTags.append(option)
        #update the currentAnnotation object's tags
        else:
            self.pedTags.remove(option)

    def egoBehaviorChangeHandler(self, option: VehicleTag, var: tk.BooleanVar):
        print("Checkbox number:", option, "was pressed")
        print("Checkboxes: ", var.get())
        if var.get():
            self.egoTags.append(option)
        else:
            self.egoTags.remove(option)

    def envBehaviorChangeHandler(self, option: SceneTag, var: tk.BooleanVar):
        print("Checkbox number:", option, "was pressed")
        print("Checkboxes: ", var.get())
        if var.get():
            self.sceneTags.append(option)
        else:
            self.sceneTags.remove(option)

    def validateText(self, inputVar):
        print("Current text status:", inputVar.get())
        
    def textupdate(self, _var, _indx, _mode):
        print("Current text status:", self.textinputvar.get())

    def handleSave(self):
        print("Button clicked. Current toggle button state: ", self.togglebuttonvar.get())

        self.eventManager.onEvent(AppEvent(type=AppEventType.requestAnnotation, data={}))

        if self.currentAnnotationStartFrame.get() == self.currentAnnotationEndFrame.get():
            currentAnnotation = SingleFrameAnnotation(self.currentAnnotationStartFrame.get(),
                                                      self.pedTags,
                                                      self.egoTags,
                                                      self.sceneTags,
                                                      self.textinputvar.get())
            self.recordingController.addSingleFrameAnnotation(currentAnnotation)
        else:
            currentAnnotation = MultiFrameAnnotation(self.currentAnnotationStartFrame.get(),
                                                     self.currentAnnotationEndFrame.get(),
                                                     self.pedTags,
                                                     self.egoTags,
                                                     self.sceneTags,
                                                     self.textinputvar.get())
            self.recordingController.addMultiFrameAnnotation(currentAnnotation)

        self.pedTags = []
        self.egoTags = []
        self.sceneTags = []

        for var in self.pedCheckbuttons:
            var.set(False)
        for var in self.vehicleCheckbuttons:
            var.set(False)
        for var in self.sceneCheckbuttons:
            var.set(False)

        self.textinputvar.set("")
            
        print("frame created")

