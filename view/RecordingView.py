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

from view.View import View
import time

class RecordingView(View):

    def __init__(self, recordingController: RecordingController, eventManager: EventManager) -> None:
        super().__init__()
        self.eventManager = eventManager
        self.recordingController = recordingController

    def render(self, parent: TKMT.WidgetFrame):
        self.parent = parent
        self.parent.Text("Recording View")

    def updateAnnotations(self):

        self.singleFrameAnnotations = self.recordingController._recording.singleFrameAnnotation
        self.multiFrameAnnotations = self.recordingController._recording.multiFrameAnnotations

        self.singleFrameJSON = [asdict(annotation) for annotation in self.singleFrameAnnotations]
        print(self.singleFrameJSON)
        
        self.parent.Treeview(['Annotations'], [120], 10, self.singleFrameJSON, 'subfiles', ['name', 'purpose'], openkey='open')