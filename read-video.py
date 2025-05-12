import cv2
import numpy as np

# Use 0 for webcam or provide path to video file
cap = cv2.VideoCapture('video1.mp4')  # or 'path/to/video.mp4'
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define codec and output file
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # or 'MJPG', 'mp4v'
out = cv2.VideoWriter('green_highlighted_output.avi', fourcc, fps, (frame_width, frame_height))



if not cap.isOpened():
    raise IOError("Cannot open video")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize (optional) for speed/viewing
    # frame = cv2.resize(frame, (640, 480))

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define broad yellow range
    lower_green = np.array([35, 20, 20], dtype=np.uint8)
    upper_green = np.array([85, 255, 255], dtype=np.uint8)

    # Create mask and inverse
    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)

    # Convert to grayscale and back to BGR
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Isolate yellow and gray parts
    yellow_part = cv2.bitwise_and(frame, frame, mask=mask)
    gray_part = cv2.bitwise_and(gray_bgr, gray_bgr, mask=mask_inv)

    # Combine and display
    combined = cv2.add(yellow_part, gray_part)
    out.write(combined)

    # cv2.imshow('Yellow Highlighted Video', combined)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
