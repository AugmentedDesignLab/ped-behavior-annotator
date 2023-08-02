import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import cv2
from PIL import Image, ImageTk
from pytube import YouTube
import threading
import queue

def start_video_stream(video_url, frame_queue):
    # Download the YouTube video
    yt = YouTube(video_url)
    stream = yt.streams.filter(file_extension='mp4').first()

    # Open the video stream
    cap = cv2.VideoCapture(stream.url)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        
        if not ret:
            break

        # Put the frame into the queue
        frame_queue.put(frame)

    # Release the video stream
    cap.release()

def update_frame(video_label, frame_queue):
    # Get the frame from the queue (if available)
    try:
        frame = frame_queue.get_nowait()

        # Resize the frame to the desired size
        frame = cv2.resize(frame, (960, 540))  # Change the size here as needed

        # Convert frame to PIL Image
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)

        # Convert PIL Image to Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image=pil_image)

        # Update the Tkinter Label with the new frame
        video_label.config(image=photo)
        video_label.image = photo

    except queue.Empty:
        # If the queue is empty, there's no new frame yet, so do nothing
        pass

    # Call this function again after a delay to update frames continuously
    video_label.after(10, update_frame, video_label, frame_queue)

# Create the Tkinter GUI
window = tk.Tk()
window.title("YouTube Video Stream")
window.geometry("1920x1080")

# # Create a themed style
# style = ThemedStyle(window)
# style.set_theme("clam")  # Choose the theme you like (e.g., "clam", "arc", "plastik", "equilux", etc.)

# Set the initial theme
window.tk.call("source", "azure.tcl")
# window.tk.call("set_theme", "light")
window.tk.call("set_theme", "azure")

frameTitle = ttk.Frame(master=window, height=20)
frameTitle.pack(fill=tk.X, ipadx=10, ipady=10)
frame3 = ttk.Frame(master=window)
frame3.pack()

newProjLabel = ttk.Label(master=frameTitle, text="Add new project", font=20)
newProjLabel.pack(side=tk.LEFT)

# call tkinter frame a content area
frame1 = tk.Frame(master=frame3, width = 1000, height=580, bg="red", border=2)
frame2 = tk.Frame(master=frame3, width = 1000, height=580, bg="light green")
frame1.grid(row=0, column=0, padx=10, pady=10)
frame2.grid(row=0, column=1, padx=10, pady=10)

# Create a label to display the video stream
video = ttk.Label(master=frame1)
video.pack()

def on_slider_move(value):
    # This function will be called when the slider is moved
    print("Slider moved to:", value)

# Create a Scale widget
slider = ttk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=on_slider_move)
slider.pack(padx=20, pady=10)

# Create a queue to pass frames between threads
frame_queue = queue.Queue()

# Start video streaming in a separate thread
video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"
video_thread = threading.Thread(target=start_video_stream, args=(video_url, frame_queue))
video_thread.start()

# Start updating frames in the GUI thread
update_thread = threading.Thread(target=update_frame, args=(video, frame_queue))
update_thread.start()

# Create widgets using ttk (themed widgets)
label = ttk.Label(master=frame2, text="Hello, Tkinter!", font=("Helvetica", 20))
label.pack(padx=20, pady=40)

button = ttk.Button(master=frame2, text="Click Me!", command=lambda: print("Button clicked"))
button.pack(pady=10)

# Run the Tkinter main loop
window.mainloop()
