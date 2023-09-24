import tkinter as tk
from tkinter import *
from tkinter import ttk
import TKinterModernThemes as TKMT
from TKinterModernThemes.WidgetFrame import Widget
from model import SingleFrameAnnotation
import allwidgets
import cv2
from typing import Tuple

from view.View import View


class AnnotationEditView(View):

    def render(self, parent: TKMT.WidgetFrame, time, frame): #also pass time and frame number (comes from outside)
        # frame information
        self.time=time
        self.frame=frame
        parent.Text("Frame # " + str(self.frame))
        parent.setActiveCol(0)
        self.behaviorFrame = parent.addLabelFrame("Behavior", padx=(0,1), pady=(0,1))
        self._renderOptions(self.behaviorFrame)
        self._renderTextField(self.behaviorFrame)
        self._renderSaveButton(self.behaviorFrame)
        
    
    def _renderOptions(self, parent: TKMT.WidgetFrame):
        options = [
            "flinching",
            "crash",
            "jaywalking",
            "distracted"
        ]

        self.behaviorCheckVars = [tk.BooleanVar(name=option) for option in options]
        col = 0
        for option, var in zip(options, self.behaviorCheckVars):
            parent.Checkbutton(option, var, self.behaviorChangeHandler, (option, var), col=col) 
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
        parent.Button("Save Annotation", self.handleButtonClick)

    def behaviorChangeHandler(self, option: str, var: tk.BooleanVar):
        print("Checkbox number:", option, "was pressed")
        print("Checkboxes: ", var.get())

    def validateText(self, inputVar):
        print("Current text status:", inputVar.get())
        
    def textupdate(self, _var, _indx, _mode):
        print("Current text status:", self.textinputvar.get())

    def handleButtonClick(self):
        print("Button clicked. Current toggle button state: ", self.togglebuttonvar.get())
        self.savedFrame = SingleFrameAnnotation(self.time, self.frame)
        print("frame created")


