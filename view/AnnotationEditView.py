import tkinter as tk
from tkinter import *
from tkinter import ttk
import cv2
from typing import Tuple


class AnnotationEditView:

    def __init__(
        self, 
        rootTitle, 
        frameType,
        window=tk.Tk
    ):
        self.rootTitle=rootTitle
        self.frameType=frameType
        self.window=window
    
    def display(window):
        window = tk.Tk()
        window.title(window.rootTitle)
        frame = window.frameType
        frame.pack()
        tk.mainloop()

    def textWidget(window):
        S = tk.Scrollbar(window)
        T = tk.Text(window, height=4, width=50)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = "text"
        T.insert(tk.END, quote)
        window.mainloop()

    def dropdown(window):
        def show():
            label.config(text = clicked.get())

        options = [
            "flinching",
            "crash",
            "jaywalking",
            "distracted"
        ]

        clicked = StringVar(window)
        clicked.set("choose")
        drop = OptionMenu( window , clicked , *options )
        drop.pack()
        button = Button( window , text = "your label" , command = show ).pack()
        label = Label( window , text = " " )
        label.pack()

        window.mainloop()
