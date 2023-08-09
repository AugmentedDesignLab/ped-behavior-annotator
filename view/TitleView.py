import tkinter as tk
from tkinter import ttk

class TitleView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        newProjLabel = ttk.Label(master=self, text="Add new project", font=20)
        newProjLabel.grid(row=0, column=0, padx=10, pady=10)