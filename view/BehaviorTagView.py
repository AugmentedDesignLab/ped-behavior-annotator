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
from model.MultiFrameAnnotation import MultiFrameAnnotation
from library.AppEvent import AppEvent, AppEventType
from managers.EventManager import EventManager
from managers.ViewEventManager import ViewEventManager
import allwidgets
import cv2
from typing import *

from view.View import View


class BehaviorTagView(View):

    def __init__(self, eventManager: EventManager, viewEventManager: ViewEventManager) -> None:
        super().__init__()
        self.eventManager = eventManager
        self.viewEventManager = viewEventManager
        # self.currentAnnotationStartFrame = tk.IntVar(value=0)
        # self.currentAnnotationEndFrame = tk.IntVar(value=0)
        # self.annotationTypeRadioVar = tk.StringVar(value='Multi')

    def handleEvent(self, appEvent: AppEvent):
        # if "updateStartFrame" in appEvent.data:
        #     self.currentAnnotationStartFrame.set(appEvent.data["updateStartFrame"])
        #     print(f"updated start frame in the edit view with {appEvent.data['updateStartFrame']} == {self.currentAnnotationStartFrame.get()}")
        # if "updateEndFrame" in appEvent.data:
        #     self.currentAnnotationEndFrame.set(appEvent.data["updateEndFrame"])
        #     print("updated end frame in the edit view")
        pass

    def render(self, parent: TKMT.WidgetFrame):
        pass