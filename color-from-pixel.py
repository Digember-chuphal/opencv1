import cv2
import numpy as np

def classify_color(h, s, v):
    if s < 20 and v > 200:
        return 'white'
    elif v < 50:
        return 'black'
    elif s < 40:
        return 'gray'
    elif 0 <= h < 10 or 160 <= h <= 179:
        return 'red'
    elif 10 <= h < 25:
        return 'orange'
    elif 25 <= h < 35:
        return 'yellow'
    elif 35 <= h < 85:
        return 'green'
    elif 85 <= h < 130:
        return 'blue'
    elif 130 <= h < 160:
        return 'purple'
    else:
        return 'unknown'


image = cv2.imread('yellow.JPG')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print(len(hsv))
# Resize or sample if needed
sampled = hsv[::10, ::10]  # sample every 10th pixel

color_counts = {}

for row in sampled:
    for pixel in row:
        h, s, v = pixel
        color = classify_color(h, s, v)
        color_counts[color] = color_counts.get(color, 0) + 1

print(color_counts)
