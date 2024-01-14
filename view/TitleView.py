import tkinter as tk
from tkinter import ttk
import TKinterModernThemes as TKMT

class TitleView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        newProjButton = ttk.Button(master=self, text="Add new project", font=20, command=self._renderTitleView)
        newProjButton.grid(row=0, column=0, padx=10, pady=10)
        newProjButton.invoke()

    def _renderTitleView(self, parent: TKMT.WidgetFrame):
        self.input_frame = parent.addLabelFrame("Title View", rowspan=2)
        self.textinputvar.trace_add('Add YouTube link here', parent.textupdate)
        self.input_frame.Entry(parent.textinputvar, validatecommand=parent.validateText)