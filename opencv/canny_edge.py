import cv2
import time
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


img = cv2.imread('images/messi5.jpg', 0)
img = cv2.resize(img, (900, 600))
cv2.namedWindow('image')
cv2.createTrackbar('MaxVal', 'image', 200, 255, nothing)
cv2.createTrackbar('MinVal', 'image', 100, 255, nothing)

max_thresh, min_thresh = 200, 100
edges = cv2.Canny(img, min_thresh, max_thresh)
while 1:
    max_thresh = cv2.getTrackbarPos('MaxVal', 'image')
    min_thresh = cv2.getTrackbarPos('MinVal', 'image')
    cv2.imshow('image', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('b'):
        edges = cv2.Canny(img, min_thresh, max_thresh)
        print(max_thresh, min_thresh)

cv2.destroyAllWindows()
