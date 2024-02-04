import tkinter as tk
from tkinter import ttk
from typing import Callable
import TKinterModernThemes as TKMT
import cv2
from PIL import Image, ImageTk
from pytube import YouTube
import threading
import queue
from controller.VideoController import VideoController
from controller.YoutubeController import YoutubeController
from library.AppEvent import AppEvent, AppEventType
from managers.EventManager import EventManager
from controller.RecordingController import RecordingController
import json
from dataclasses import dataclass, field, asdict
import platform

from view.View import View
import time

class RecordingView(View):

    def __init__(self, recordingController: RecordingController, eventManager: EventManager) -> None:
        super().__init__()
        self.eventManager = eventManager
        self.recordingController = recordingController

    def render(self, parent: TKMT.WidgetFrame):

        # Create a canvas
        canvas = tk.Canvas(parent.master)
        canvas.pack(side="left", fill="both", expand=True)

        # Create a frame to hold widgets
        inner_frame = ttk.Frame(canvas)
        inner_frame_id = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Function to update the canvas scrolling region
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind("<Configure>", on_configure)

        # Function to update the inner frame position
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", on_mousewheel)

        # Populate the inner frame with widgets
        for i in range(20):  # Adjust the range as needed
            widget_frame = ttk.Frame(inner_frame, height=40, width=200)
            widget_frame.pack(pady=5, padx=10, fill="both")
            label = ttk.Label(widget_frame, text=f"Label {i}")
            label.pack()

        # Call on_configure once to set up the initial scrolling region
        on_configure(None)

    def updateAnnotations(self):

        self.singleFrameAnnotations = self.recordingController._recording.singleFrameAnnotation
        self.multiFrameAnnotations = self.recordingController._recording.multiFrameAnnotations

        self.singleFrameJSON = [asdict(annotation) for annotation in self.singleFrameAnnotations]
        print(self.singleFrameJSON)
        
        self.parent.Treeview(['Annotations'], [120], 10, self.singleFrameJSON, 'subfiles', ['name', 'purpose'], openkey='open')