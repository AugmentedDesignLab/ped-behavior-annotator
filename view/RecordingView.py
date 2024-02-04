import tkinter as tk
from tkinter import ttk
from typing import Callable
import TKinterModernThemes as TKMT
import cv2
from PIL import Image, ImageTk
from pytube import YouTube
import threading
import queue
from typing import *
from controller.VideoController import VideoController
from controller.YoutubeController import YoutubeController
from library.AppEvent import AppEvent, AppEventType
from managers.EventManager import EventManager
from managers.ViewEventManager import ViewEventManager
from controller.RecordingController import RecordingController
from model.SingleFrameAnnotation import SingleFrameAnnotation
from model.MultiFrameAnnotation import MultiFrameAnnotation
import json
from dataclasses import dataclass, field, asdict
import platform

from view.View import View
import time

class RecordingView(View):

    def __init__(self, recordingController: RecordingController, eventManager: EventManager, viewEventManager: ViewEventManager) -> None:
        super().__init__()
        self.eventManager = eventManager
        self.viewEventManager = viewEventManager
        self.recordingController = recordingController

    def handleEvent(self, appEvent: AppEvent):
        if appEvent.type == AppEventType.recording:
            if "newAnnotation" in appEvent.data:
                self.updateAnnotations(appEvent.data["newAnnotation"])
        pass

        
    def render(self, parent: TKMT.WidgetFrame):

        # Create a canvas
        self.canvas = tk.Canvas(parent.master)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Set the focus to the canvas to enable scrolling
        self.canvas.focus_set()

        # Create a frame to hold widgets
        self.inner_frame = ttk.Frame(self.canvas)
        self.recordingFrame = TKMT.WidgetFrame(self.inner_frame, "Recording View")
        self.recordingFrame.Text("Click on a annotation to open in the edit view")
        inner_frame_id = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # no initial cards
        # Populate the inner frame with widgets
        # self.singleFrameAnnotations = self.recordingController._recording.singleFrameAnnotation
        # for annotation in self.singleFrameAnnotations:
        #     card_frame = self.create_annotation_card(self.inner_frame, annotation)
        #     card_frame.pack(pady=5, padx=10, fill="both")

        self.canvas.bind("<Configure>", self.on_configure)

        # Call on_configure once to set up the initial scrolling region
        self.on_configure(None)

        def on_mousewheel(event):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        # Bind the mouse wheel event to the canvas
        self.canvas.bind("<MouseWheel>", on_mousewheel)

    # Function to update the canvas scrolling region
    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def createSingleAnnotationCard(self, annotation: SingleFrameAnnotation) -> TKMT.WidgetFrame:
        cardFrame = self.recordingFrame.addLabelFrame(str(annotation.frame), padx=(5,5), pady=(10,0))
        # print("createSingleAnnotationCard", pedTags)
        self.addTagsToCard(cardFrame, annotation)
        return cardFrame

    def addTagsToCard(self, cardFrame: TKMT.WidgetFrame, annotation: Union[SingleFrameAnnotation, MultiFrameAnnotation]):
        cardFrame.setActiveCol(0)
        cardFrame.Text("Ped Tags:")
        pedTags = ', '.join(map(lambda tag: tag.value, annotation.pedTags))
        cardFrame.nextCol()
        cardFrame.Text(pedTags)

        cardFrame.setActiveCol(0)
        cardFrame.Text("Ego Tags:")
        egoTags = ', '.join(map(lambda tag: tag.value, annotation.egoTags))
        cardFrame.nextCol()
        cardFrame.Text(egoTags)

        cardFrame.setActiveCol(0)
        cardFrame.Text("Scene Tags:")
        sceneTags = ', '.join(map(lambda tag: tag.value, annotation.sceneTags))
        cardFrame.nextCol()
        cardFrame.Text(sceneTags)


        cardFrame.setActiveCol(0)
        cardFrame.Text("Notes:")
        cardFrame.nextCol()
        cardFrame.Text(annotation.additionalNotes)
        pass

    def createMultiAnnotationCard(self, annotation: SingleFrameAnnotation) -> TKMT.WidgetFrame:
        cardFrame = self.recordingFrame.addLabelFrame(f"{annotation.frameStart} to {annotation.frameEnd}", padx=(5,5), pady=(10,0))
        # print("createSingleAnnotationCard", pedTags)
        self.addTagsToCard(cardFrame, annotation)
        return cardFrame

    
    
    def addAnnotationCard(self, new_annotation):

        # Create and pack a new annotation card
        if type(new_annotation) == SingleFrameAnnotation:
            # card_frame = self.create_singleFrame_annotation_card(self.inner_frame, new_annotation)
            cardFrame = self.createSingleAnnotationCard(new_annotation)

        else: # otherwise, it's a multi frame annotation
            # card_frame = self.create_multiFrame_annotation_card(self.inner_frame, new_annotation)
            # card_frame.pack(pady=5, padx=10, fill="both")
            cardFrame = self.createMultiAnnotationCard(new_annotation)

        # Call on_configure to update the canvas scrolling region
        self.on_configure(None)

    def updateAnnotations(self, annotation):
        # self.add_annotation_card(annotation)
        # We need to reload the whole thing
        # clear current
        self.clear()
        recording = self.recordingController.recording
        print(recording.singleFrameAnnotations)
        print(recording.multiFrameAnnotations)
        # order annotations by start frame
        allAnnotations = self.recordingController.getSortedAnnotationsByStartFrame(recording)
        for annotation in allAnnotations:
            self.addAnnotationCard(annotation)
    
    def clear(self):

        # for cardWiget in self.recordingFrame.widgets:
        #     cardFrame = cardWiget.widget # the label WidgetFrame
        #     cardTKFrame = cardFrame.master
        #     cardTKFrame.destroy()
        # self.recordingFrame.widgets.widgetlist.clear()
        
        for widgets in self.inner_frame.winfo_children():
            print(widgets)
            widgets.destroy()
        
        self.recordingFrame = TKMT.WidgetFrame(self.inner_frame, "Recording View")
