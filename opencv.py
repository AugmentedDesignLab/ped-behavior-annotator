import cv2
import pafy

# URL of the YouTube video
video_url = "https://www.youtube.com/watch?v=zY0X-9tN7OU"

# Create a pafy object to fetch YouTube video information
video = pafy.new(video_url)

# Get the best available video stream
best_stream = video.getbest()

# Open the video stream
cap = cv2.VideoCapture(best_stream.url)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error opening video.")
    exit()

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if we reach the end of the video
    if not ret:
        break

    # Annotate the frame (e.g., draw a rectangle and text)
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
    cv2.putText(frame, "Annotation", (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the annotated frame
    cv2.imshow("Annotated YouTube Video", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
