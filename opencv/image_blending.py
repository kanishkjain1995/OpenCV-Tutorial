import cv2
import numpy as np
import sys

default_size = (512, 512)

A = cv2.imread('apple.jpg')
A = cv2.resize(A, default_size)
B = cv2.imread('orange.jpg')
B = cv2.resize(B, default_size)

gpA = []
G = A.copy()
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

gpB = []
G = B.copy()
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

lapA = [gpA[5]]
for i in range(5, 0, -1):
    G = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1], G)
    lapA.append(L)

lapB = [gpB[5]]
for i in range(5, 0, -1):
    G = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1], G)
    lapB.append(L)

lap = []
for x, y in zip(lapA, lapB):
    row, col, ch = x.shape
    ls = np.hstack((x[:, :col//2], y[:, col//2:]))
    lap.append(ls)

ls_ = lap[0]
for i in range(1, 6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, lap[i])

cv2.imshow('Blended', ls_)
cv2.waitKey(0)
cv2.destroyAllWindows()
