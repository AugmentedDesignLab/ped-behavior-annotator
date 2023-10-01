import tkinter as tk
from tkinter import *
from tkinter import ttk
import TKinterModernThemes as TKMT
from TKinterModernThemes.WidgetFrame import Widget
from controller.RecordingController import RecordingController
from model.PedestrianTag import PedestrianTag
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
        self.behaviorFrame = parent.addLabelFrame("Behavior", padx=(0,1), pady=(0,1))
        self._renderOptions(self.behaviorFrame)
        self._renderTextField(self.behaviorFrame)
        self._renderSaveButton(self.behaviorFrame)


    def render(self, parent: TKMT.WidgetFrame, time: float, frame: int):
        # frame information
        self.currentAnnotation = SingleFrameAnnotation(time, frame)
        self._renderView(parent)

    def renderSingleEdit(self, parent: TKMT.WidgetFrame, existingAnnotation: SingleFrameAnnotation):
        # you do the same thing, but read information from the existingAnnotation object
        self.currentAnnotation = existingAnnotation
        self._renderView(parent)

    
    def _renderOptions(self, parent: TKMT.WidgetFrame):
        options = [
            PedestrianTag.Flinch,
            PedestrianTag.Crash,
            PedestrianTag.Jaywalking,
            PedestrianTag.Distracted,
            PedestrianTag.NoLook,
            PedestrianTag.RedLight,
            PedestrianTag.ChangingLight,
            PedestrianTag.NoSigns
        ]

        self.behaviorCheckVars = [tk.BooleanVar(name=option.value) for option in options]
        col = 0
        for option, var in zip(options, self.behaviorCheckVars):
            parent.Checkbutton(option.value, var, self.behaviorChangeHandler, (option, var), col=col) 
            col += 1
            # the behaviorChangeHandler is called whenever a checkbox is pressed with the associated option and var


    def _renderTextField(self, parent: TKMT.WidgetFrame):

        parent.Text("Additional Notes:", col=0)
        parent.nextCol()

        self.textinputvar = tk.StringVar()
        self.textinputvar.trace_add('write', self.textupdate)
        parent.Entry(
            self.textinputvar, 
            colspan=3,
            validatecommand=self.validateText, 
            validatecommandargs=(self.textinputvar,)
            )

    def _renderSaveButton(self, parent: TKMT.WidgetFrame):
        self.togglebuttonvar = tk.BooleanVar()
        parent.Button("Save Annotation", self.handleSave)

    def behaviorChangeHandler(self, option: PedestrianTag, var: tk.BooleanVar):
        print("Checkbox number:", option, "was pressed")
        print("Checkboxes: ", var.get())
        self.currentAnnotation.pedTags.append(option)
        # TODO update the currentAnnotation object's tags


    def validateText(self, inputVar):
        print("Current text status:", inputVar.get())
        
    def textupdate(self, _var, _indx, _mode):
        print("Current text status:", self.textinputvar.get())

    def handleSave(self):
        print("Button clicked. Current toggle button state: ", self.togglebuttonvar.get())
        self.recordingController.addSingleFrameAnnotation(self.currentAnnotation)
        print("frame created")


