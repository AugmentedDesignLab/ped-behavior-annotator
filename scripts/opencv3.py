import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import cv2
from PIL import Image, ImageTk
from pytube import YouTube
import threading

def start_video_stream():
    # URL of the YouTube video
    # video_url = "https://www.youtube.com/watch?v=zY0X-9tN7OUs"
    video_url = "https://www.youtube.com/watch?v=SFf7Hump8pQ"

    # Download the YouTube video
    yt = YouTube(video_url)
    stream = yt.streams.filter(file_extension='mp4', res='1080p').first()

    # Open the video stream
    cap = cv2.VideoCapture(stream.url)

    def update_frame():
        # Read a frame from the video
        ret, frame = cap.read()

        if ret:
            # Resize the frame to the desired size
            frame = cv2.resize(frame, (960, 540))  # Change the size here as needed

            # Convert frame to PIL Image
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)

            # Convert PIL Image to Tkinter PhotoImage
            photo = ImageTk.PhotoImage(image=pil_image)

            # Update the Tkinter Label with the new frame
            label.config(image=photo)
            label.image = photo

        # Call this function recursively to update frames continuously
        label.after(10, update_frame)

    update_frame()


# Create the Tkinter GUI
window = tk.Tk()
window.title("YouTube Video Stream")
window.geometry("1920x1080")

# # Create a themed style
# style = ThemedStyle(window)
# style.set_theme("clam")  # Choose the theme you like (e.g., "clam", "arc", "plastik", "equilux", etc.)

# Set the initial theme
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "light")

frame1 = tk.Frame(master=window, width = 1000, height=580, bg="gray")
frame2 = tk.Frame(master=window, bg="light green")

# frame1.grid(row=0, column=0, padx=10, pady=10)
# frame2.grid(row=0, column=1, padx=10, pady=10)
# Place the frames side by side
frame1.pack(side=tk.LEFT)
frame2.pack(side=tk.LEFT)

# Create a label to display the video stream
video = ttk.Label(master=frame1)
video.pack()

# Start video streaming in a separate thread to prevent blocking the main Tkinter loop
video_thread = threading.Thread(target=start_video_stream)
video_thread.start()

# Create widgets using ttk (themed widgets)
label = ttk.Label(master=frame2, text="Hello, Tkinter!", font=("Helvetica", 20))
label.pack(padx=20, pady=40)

button = ttk.Button(master=frame2, text="Click Me!", command=lambda: print("Button clicked"))
button.pack(pady=10)

# Run the Tkinter main loop
window.mainloop()
