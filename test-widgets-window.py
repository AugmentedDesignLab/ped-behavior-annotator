#imports 
import tkinter as tk
from tkinter import *

root = tk.Tk()

#makes the text box widget you can type in it plus add text to display and scroll through it
S = tk.Scrollbar(root)
T = tk.Text(root, height=4, width=50)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = " "
T.insert(tk.END, quote)

#makes the dropdown widgets
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


