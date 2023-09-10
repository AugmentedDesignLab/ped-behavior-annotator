import tkinter as tk
from tkinter import *
from tkinter import ttk
import TKinterModernThemes as TKMT
from TKinterModernThemes.WidgetFrame import Widget
import cv2
from typing import Tuple

from view.View import View


class AnnotationEditView(View):

    # def __init__(
    #     self, 
    #     rootTitle, 
    #     frameType,
    #     window=tk.Tk
    # ):
    #     self.rootTitle=rootTitle
    #     self.frameType=frameType
    #     self.window=window
    
    # def display(window):
    #     window = tk.Tk()
    #     window.title(window.rootTitle)
    #     frame = window.frameType
    #     frame.pack()
    #     tk.mainloop()

    # def textWidget(window):
    #     S = tk.Scrollbar(window)
    #     T = tk.Text(window, height=4, width=50)
    #     S.pack(side=tk.RIGHT, fill=tk.Y)
    #     T.pack(side=tk.LEFT, fill=tk.Y)
    #     S.config(command=T.yview)
    #     T.config(yscrollcommand=S.set)
    #     quote = "text"
    #     T.insert(tk.END, quote)
    #     window.mainloop()

    # def dropdown(window):
    #     def show():
    #         label.config(text = clicked.get())

    #     options = [
    #         "flinching",
    #         "crash",
    #         "jaywalking",
    #         "distracted"
    #     ]

    #     clicked = StringVar(window)
    #     clicked.set("choose")
    #     drop = OptionMenu( window , clicked , *options )
    #     drop.pack()
    #     button = Button( window , text = "your label" , command = show ).pack()
    #     label = Label( window , text = " " )
    #     label.pack()

    #     window.mainloop()

    
    def render(self, parent: TKMT.WidgetFrame):
        # frame information
        parent.Text("Frame #")
        parent.nextCol()
        parent.Text("100")
        parent.setActiveCol(0)

        self.behaviorFrame = parent.addLabelFrame("Behavior", padx=(0,0), pady=(0,0))
        self._renderOptions(self.behaviorFrame)
        self._renderTextField(self.behaviorFrame)
    
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


    def behaviorChangeHandler(self, option: str, var: tk.BooleanVar):
        print("Checkbox number:", option, "was pressed")
        print("Checkboxes: ", var.get())

    def validateText(self, inputVar):
        print("Current text status:", inputVar.get())
        
    def textupdate(self, _var, _indx, _mode):
        print("Current text status:", self.textinputvar.get())