import cv2
import numpy as np

def sketch(image):
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gaussianImage = cv2.GaussianBlur(grayImage, (5,5), 0)

    canny = cv2.Canny(gaussianImage, 10, 100)

    ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY_INV)

    return mask

capture = cv2.VideoCapture(0)

while True:
    ret, liveFrame = capture.read()
    cv2.imshow('Our Live Sketch', sketch(liveFrame))

    if cv2.waitKey(1) == 13:
        break

capture.release()
cv2.destroyAllWindows()