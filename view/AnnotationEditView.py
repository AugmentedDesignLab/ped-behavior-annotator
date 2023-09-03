import tkinter as tk
from tkinter import *
from tkinter import ttk
import cv2
from typing import Tuple


class AnnotationEditView:

    def __init__(
        self, 
        rootTitle, 
        frameType
    ):
        self.rootTitle=rootTitle
        self.frameType=frameType
    
    def display(self):
        root = tk.Tk()
        root.title(self.rootTitle)
        frame = self.frameType
        frame.pack()
        tk.mainloop()

    def textWidget(self):
        root = tk.Tk()
        root.title(self.rootTitle)
        S = tk.Scrollbar(root)
        T = tk.Text(root, height=4, width=50)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = "text"
        T.insert(tk.END, quote)
        tk.mainloop()

    def dropdown(self):
        root = tk.Tk()
        
        def show():
            label.config(text = clicked.get())

        options = [
            "flinching",
            "crash",
            "jaywalking",
            "distracted"
        ]

        clicked = StringVar(root)
        clicked.set("choose")
        drop = OptionMenu( root , clicked , *options )
        drop.pack()
        button = Button( root , text = "your label" , command = show ).pack()
        label = Label( root , text = " " )
        label.pack()

        root.mainloop()
