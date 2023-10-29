import tkinter as tk
from tkinter import Scrollbar, Canvas, Frame

def add_annotation(annotation_text):
    top_canvas.create_text(50, (len(annotations) + 1) * 30, text=annotation_text, anchor=tk.W)

    card = tk.Frame(cards_frame, bg="lightgray", bd=1, relief=tk.SUNKEN)
    card.pack(pady=5, padx=5, fill=tk.X)
    label = tk.Label(card, text=annotation_text, bg="lightgray", wraplength=250)
    label.pack(padx=10, pady=10)
    
    annotations.append(annotation_text)

def on_configure(event):
    cards_canvas.configure(scrollregion=cards_canvas.bbox('all'))

root = tk.Tk()
root.title("Annotations Viewer")

top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)

bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=5)

top_canvas = Canvas(top_frame, bg="white")
top_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

cards_canvas = Canvas(bottom_frame, bg="white")
cards_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(bottom_frame, command=cards_canvas.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

cards_canvas.configure(yscrollcommand=scrollbar.set)

cards_frame = Frame(cards_canvas)
cards_canvas.create_window((0, 0), window=cards_frame, anchor='nw')
cards_frame.bind('<Configure>', on_configure)

annotations = []

root.mainloop()