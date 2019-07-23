import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("logo/ellipse.png")
height, width = (600, 400)
img = cv2.resize(img, (height, width), cv2.INTER_LINEAR)

# gaussian noise
row, col, ch = img.shape
mean = 0
var = 0.1
sigma = var**0.5
gauss = np.random.normal(mean, sigma, (row, col, ch))
gauss = gauss.reshape(row, col, ch)
noisy = img + gauss

# gaussian filtering
gaus_blur = cv2.GaussianBlur(noisy, (5, 5), 0)
blur = cv2.blur(noisy, (5, 5))
bil_blur = cv2.bilateralFilter(noisy, 9, 75, 75)
plt.subplot(121), plt.imshow(gaus_blur), plt.title('Gaussian Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(bil_blur), plt.title('Bilateral Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
