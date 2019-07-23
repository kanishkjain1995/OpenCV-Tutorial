import cv2
import numpy as np

ix, iy = -1, -1
mode = False


def switch_shape(event, x, y, flag, param):
    global ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        if mode:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 1)
        else:
            cv2.circle(img, (x, y), 10, (0, 0, 255), 1)


def draw_circle(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(img[x, y], (x, y))
        print(np.array_equal(img[x, y], np.array([0, 0, 0])))
        if np.array_equal(img[x, y], np.array([0, 0, 0])):
            color = (0, 0, 255)
        elif np.array_equal(img[x, y], np.array([0, 0, 255])):
            color = (255, 255, 255)
        else:
            color = (255, 0, 0)
        print("Event {} triggered".format(event))
        cv2.circle(img, (x, y), 50, color, 1)
        print("Circle Drawn")


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', switch_shape)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('q'):
        break
cv2.destroyAllWindows()
