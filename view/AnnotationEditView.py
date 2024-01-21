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
import allwidgets
import cv2
from typing import Tuple

from view.View import View


class AnnotationEditView(View):

    def __init__(self, recordingController: RecordingController) -> None:
        super().__init__()
        self.recordingController = recordingController

    
    def _renderView(self, parent: TKMT.WidgetFrame):
        parent.Text("Frame # " + str(self.currentAnnotation.frame))
        parent.setActiveCol(0)
        self.pedBehaviorFrame = parent.addLabelFrame("Pedestrian Behavior", padx=(0,1), pady=(0,1))
        self._renderPedOptions(self.pedBehaviorFrame)
        self.vehBehaviorFrame = parent.addLabelFrame("Vehicle Behavior", padx=(0,1), pady=(0,1))
        self._renderVehicleOptions(self.vehBehaviorFrame)
        self.envBehaviorFrame = parent.addLabelFrame("Environment Behavior", padx=(0,1), pady=(0,1))
        self._renderSceneOptions(self.envBehaviorFrame)
        self._renderTextField(parent)
        self._renderSaveButton(parent)


    def render(self, parent: TKMT.WidgetFrame, time: float, frame: int):
        # frame information
        self.currentAnnotation = SingleFrameAnnotation(time, frame)
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
        for option, var in zip(options, self.behaviorCheckVars):
            parent.Checkbutton(option.value, var, self.behaviorChangeHandler, (option, var), col=col) 
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
        for option, var in zip(options, self.behaviorCheckVars):
            parent.Checkbutton(option.value, var, self.egoBehaviorChangeHandler, (option, var), col=col) 
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
        for option, var in zip(options, self.behaviorCheckVars):
            parent.Checkbutton(option.value, var, self.envBehaviorChangeHandler, (option, var), col=col) 
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
            row=1
            )

    def _renderSaveButton(self, parent: TKMT.WidgetFrame):
        self.togglebuttonvar = tk.BooleanVar()
        parent.Button("Save Annotation", self.handleSave)

    def behaviorChangeHandler(self, option: PedestrianTag, var: tk.BooleanVar):
        print("Checkbox number:", option, "was pressed")
        print("Checkboxes: ", var.get())
        self.currentAnnotation.pedTags.append(option)
        #update the currentAnnotation object's tags

    def egoBehaviorChangeHandler(self, option: VehicleTag, var: tk.BooleanVar):
        print("Checkbox number:", option, "was pressed")
        print("Checkboxes: ", var.get())
        self.currentAnnotation.egoTags.append(option)

    def envBehaviorChangeHandler(self, option: SceneTag, var: tk.BooleanVar):
        print("Checkbox number:", option, "was pressed")
        print("Checkboxes: ", var.get())
        self.currentAnnotation.sceneTags.append(option)



    def validateText(self, inputVar):
        print("Current text status:", inputVar.get())
        
    def textupdate(self, _var, _indx, _mode):
        print("Current text status:", self.textinputvar.get())

    def handleSave(self):
        print("Button clicked. Current toggle button state: ", self.togglebuttonvar.get())
        self.recordingController.addSingleFrameAnnotation(self.currentAnnotation)
        print("frame created")


