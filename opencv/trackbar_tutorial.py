import cv2
import numpy as np


def nothing(x):
    pass


def draw(event, x, y, flag, param):
    draw = cv2.getTrackbarPos(switch, 'image')
    print("Event recieved is {}".format(event))
    if event == cv2.EVENT_MOUSEMOVE and draw == 1:
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        bsize = cv2.getTrackbarPos(brush, 'image')
        color = (b, g, r)
        cv2.circle(img, (x, y), bsize, color, -1, cv2.LINE_AA)


img = np.zeros((512, 512, 3), np.uint8)
img[:] = [255, 255, 255]
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

brush = 'size'
cv2.createTrackbar(brush, 'image', 1, 10, nothing)

switch = 'draw'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)


cv2.setMouseCallback('image', draw)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
