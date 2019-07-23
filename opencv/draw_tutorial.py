import cv2
import numpy as np
import math

img = np.zeros((300, 200, 3), np.uint8)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)

out_r, in_r = 40, 20
black = (0, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)

img = cv2.ellipse(img, (100, 100), (out_r, out_r), 120, 0, 300, red, -1, cv2.LINE_AA)
img = cv2.circle(img, (100, 100), in_r, black, -1, cv2.LINE_AA)
img = cv2.ellipse(img, (50, 180), (out_r, out_r), -60, 0, -300, green, -1, cv2.LINE_AA)
img = cv2.circle(img, (50, 180), in_r, black, -1, cv2.LINE_AA)
img = cv2.ellipse(img, (140, 180), (out_r, out_r), -120, 0, -300, blue, -1, cv2.LINE_AA)
img = cv2.circle(img, (140, 180), in_r, black, -1, cv2.LINE_AA)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (40, 260), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.imwrite('ellipse-2.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
