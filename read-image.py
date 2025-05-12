import cv2
import pyautogui
import numpy as np

screen_width, screen_height = pyautogui.size()
print(f"Screen width: {screen_width}, Screen height: {screen_height}")

print(cv2.__version__)
image=cv2.imread('yellow.JPG')
height, width,channels  = image.shape

print(f"Width: {width}, Height: {height}")
resized_image = cv2.resize(image, (800, 800))

# Convert to HSV color space
hsv = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)

# Define yellow color range in HSV
lower_yellow = np.array([15, 50, 50], dtype=np.uint8)
upper_yellow = np.array([35, 255, 255], dtype=np.uint8)

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Invert mask to get non-yellow areas
mask_inv = cv2.bitwise_not(mask)

# Convert image to grayscale and then back to BGR for merging
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# Extract yellow parts from original image
yellow_part = cv2.bitwise_and(resized_image, resized_image, mask=mask)

# Extract non-yellow (gray) parts
gray_part = cv2.bitwise_and(gray_bgr, gray_bgr, mask=mask_inv)

# Combine yellow and grayscale parts
combined = cv2.add(yellow_part, gray_part)

# Show result
cv2.imshow("Yellow Highlighted", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
