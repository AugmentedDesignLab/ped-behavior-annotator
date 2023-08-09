import tkinter as tk
from tkinter import ttk
from TKinterModernThemes.WidgetFrame import Widget
import TKinterModernThemes as TKMT
from view import *

def buttonCMD():
        print("Button clicked!")

class App(TKMT.ThemedTKinterFrame):
    def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__("TITLE", theme, mode, usecommandlineargs, usethemeconfigfile)
        # self.Button("Auto placed button!", buttonCMD)  # placed at row 0, col 0

        # self.button_frame = self.addLabelFrame("Frame Label")  # placed at row 1, col 0

        # self.button_frame.Button("Button Text", buttonCMD)  # the button is dropped straight into the frame

        # button = ttk.Button(self.button_frame.master, text="Button in frame!")
        # button.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # button = ttk.Button(self.master, text="Button outside frame!")
        # button.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        # button = ttk.Button(self.master, text="debugPrint() finds this button")
        # button.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')
        # self.widgets.widgetlist.append(Widget(button, "Button", 3, 0, 1, 1,
        #                                       "debugPrint() finds this button"))
        # self.debugPrint()

        # create two widgetframes, nav and content
        self.makeNav()
        self.makeContent()
        self.makeEditor()
        # self.debugPrint()
        self.run()
    
    def makeNav(self):
        self.navFrame = self.addFrame("Nav")
        self.navFrame.Button("New Project", buttonCMD)
        self.navFrame.nextCol()
        self.navFrame.Button("Save", buttonCMD)
        self.navFrame.setActiveCol(0)
        self.navFrame.Text("Recording Name")
        self.navFrame.Text("Annotation Path")
    
    def makeContent(self):
        self.contentFrame = self.addFrame("Content", padx=(0,0), pady=(0,0))

        # left and right
        self.leftFrame = self.contentFrame.addFrame("Left", padx=(0,0), pady=(0,0))
        self.leftFrame.Text("Left Frame")
        self.contentFrame.nextCol()
        self.rightFrame = self.contentFrame.addFrame("Right", padx=(0,0), pady=(0,0))
        self.rightFrame.Text("Right Frame")

    
    def makeEditor(self):
         # put video player and annotation edit on the left frame
         # put recording on the right
        self.videoFrame = self.leftFrame.addFrame("Video", padx=(0,0), pady=(0,0))
        # self.videoFrame.Text("Video")
        # self.leftFrame.Seperator()
        self.annotationFrame = self.leftFrame.addFrame("Annotation", padx=(0,0), pady=(0,0))
        self.annotationFrame.Text("Annotation")


        self.recordingFrame = self.rightFrame.addFrame("Recording", padx=(0,0), pady=(0,0))
        text = self.recordingFrame.Text("Recording")
        # text.pack(side=tk.TOP)


        sampleView = SampleView()
        sampleView.render(self.videoFrame)

        videoView = VideoView()
        videoView.render(self.videoFrame)


if __name__ == "__main__":
        App("park", "dark")