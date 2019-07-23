import cv2
import numpy as np

logo = cv2.imread("ellipse.png")
messi = cv2.imread("messi.jpg")

row, col, channel = logo.shape
roi = messi[0:row, 0:col]

gray_logo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray_logo, 10, 255, cv2.THRESH_BINARY)
mask_logo = cv2.bitwise_not(mask)

# blended
blended = cv2.addWeighted(logo, 0.7, roi, 0.3, 0)

# anded
roi_add = cv2.bitwise_and(roi, roi, mask=mask_logo)
logo_add = cv2.bitwise_and(logo, logo, mask=mask)

final_add = cv2.add(roi_add, logo_add)

messi[0:row, 0:col] = final_add

cv2.imshow('result', messi)
cv2.waitKey(0)
cv2.destroyAllWindows()
