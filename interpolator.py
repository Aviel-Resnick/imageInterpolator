import numpy as np
import cv2

sampleA = cv2.imread('blop.png')
sampleB = cv2.imread('black.png')


height, width = sampleA.shape[:2]

for x in range(width):
    for y in range(height):
        color = sampleA[x,y]
        print(color)
