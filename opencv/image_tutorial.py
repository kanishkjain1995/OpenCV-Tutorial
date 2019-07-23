import cv2
import sys
import matplotlib.pyplot as plt

lib = sys.argv[1]
img = cv2.imread('messi.jpeg', 1)

if lib == "opencv":
    cv2.imshow('messi', img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('messigray2.png', img)
        cv2.destroyAllWindows()
elif lib == "matplotlib":
    plt.imshow(img, cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.show()
