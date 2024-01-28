import tkinter as tk
from tkinter import ttk
import TKinterModernThemes as TKMT

class TitleView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def _renderView(self, parent: TKMT.WidgetFrame):
        parent.setActiveCol(0)
        self.titleFrame = parent.addLabelFrame("Title View", padx=(0,1), pady=(0,1))
        newProjButton = parent.Button(text="Add new project", command=self.renderTitleView)
        newProjButton.grid(row=0, column=0, padx=10, pady=10)
        newProjButton.invoke()

    def render(self, parent: TKMT.WidgetFrame):
        parent.Text("Title View")
        self._renderView(parent)

    def _titleView(self, parent: TKMT.WidgetFrame):
        parent.setActiveCol(0)
        self.startFrame = parent.addLabelFrame("Start", padx=(0,1), pady=(0,1))
        self.input_frame = parent.addLabelFrame("Title View", rowspan=2)
        self.textinputvar.trace_add('Add YouTube link here', self.textupdate)
        self.input_frame.Entry(self.textinputvar, validatecommand=self.validateText)

    def renderTitleView(self, parent: TKMT.WidgetFrame):
        self._titleView(parent)