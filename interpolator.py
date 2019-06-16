import numpy as np
import cv2

start = cv2.imread('white.png')
end = cv2.imread('black.png')

def convert(image):
    height, width = image.shape[:2]
    output = []

    for column in range(width):
        columnList = []
        for row in range(height):
            columnList.append(list(image[column,row]))
        output.append(columnList)

    return(output)

def main(start, end):
    startList = convert(start)
    endList = convert(end)

    print(startList)

main(start, end)
