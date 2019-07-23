import cv2
import time
import numpy as np

default_shape = (600, 400)

img0 = np.zeros((400, 600, 3), np.uint8)

for x in range(1, 11):
    filename = "images/messi{}.jpg".format(x)
    img = cv2.imread(filename)
    img = cv2.resize(img, default_shape)

    for a in range(1, 11):
        cv2.imshow('smooth', cv2.addWeighted(img, a/10, img0, 1-a/10, 0))
        time.sleep(0.01)
        cv2.waitKey(1)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    img0 = img

cv2.destroyAllWindows()
