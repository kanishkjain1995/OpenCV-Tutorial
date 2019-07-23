import cv2
import numpy as np

img = cv2.imread("images/messi1.jpg", 0)

# resize image
height, width = (600, 400)
resized = cv2.resize(img, (height, width), cv2.INTER_LINEAR)
rows, cols = resized.shape[:2]

# translation
# M = np.float32([[1, 0, 100], [0, 1, 50]])
# dst = cv2.warpAffine(resized, M, (cols, rows))

# rotation
# M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
# dst = cv2.warpAffine(resized, M, (cols, rows))

# affine transformation
# pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
# pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
# M = cv2.getAffineTransform(pts1, pts2)
# dst = cv2.warpAffine(resized, M, (cols, rows))

# perspective transformation
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(resized, M, (300, 300))

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
