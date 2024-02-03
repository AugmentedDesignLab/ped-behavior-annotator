import tkinter as tk
from tkinter import ttk
from TKinterModernThemes.WidgetFrame import Widget
import TKinterModernThemes as TKMT

def buttognCMD():
        print("Button clicked!")

class SampleView:
        
    def render(self, parent: TKMT.WidgetFrame):
        parent.Text("Sample View")