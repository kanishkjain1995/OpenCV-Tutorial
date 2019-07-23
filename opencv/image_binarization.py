import cv2
import random
import numpy as np
import matplotlib.pyplot as plt


def calculate_threshold(hist):
    idx_nonzero, = np.nonzero(hist[:, 0])
    thresh = (idx_nonzero[0]+idx_nonzero[-1])//2

    print("Initial threshold is {}".format(thresh))
    s1 = set(range(0, thresh))
    s2 = set(range(thresh, 256))

    while 1:
        d1 = np.sum([hist[x, 0] for x in s1])
        d2 = np.sum([hist[x, 0] for x in s2])
        m1 = sum([x*hist[x, 0] for x in s1])/d1
        m2 = sum([x*hist[x, 0] for x in s2])/d2
        changed = False
        for k in range(0, 256):

            if d1 != hist[k, 0] and k in s1:
                score1 = (np.square(k-m1)*hist[k, 0]*d1)/(d1-hist[k, 0])
                score2 = (np.square(k-m2)*hist[k, 0]*d2)/(d2+hist[k, 0])

                if score1 > score2:
                    m1 = m1 - np.divide(np.multiply(k-m1, hist[k, 0]), d1 - hist[k, 0])
                    m2 = m2 - np.divide(np.multiply(k-m2, hist[k, 0]), d2 - hist[k, 0])
                    d1 = d1 - hist[k, 0]
                    d2 = d2 + hist[k, 0]
                    s1.remove(k)
                    s2.add(k)
                    changed = True

        if changed == False:
            break
    return s1, s2


img = cv2.imread("grayImages/img14.png", 0)
# img = cv2.GaussianBlur(img, (5, 5), 0)

# optimized OTSU
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
s1, s2 = calculate_threshold(hist)
i = 0
thresh = len(s1)
for x in s1:
    if i != x:
        thresh = i
        break
    i += 1

print("Updated Threshold is {}".format(thresh))
ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

# CV2 OTSU
# thresh, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# print("Updated Threshold is {}".format(thresh))

# plot hisogram of image
# plt.plot(hist, color='r')
# plt.xlim([0, 256])
# plt.show()

# display image
cv2.imshow('binary_image', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
