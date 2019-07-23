import numpy as np
import cv2
x = 5
%timeit y = x**2
%timeit y = x*x
z = np.uint8([5])
%timeit y = z*z
%timeit y = np.square(z)

img = cv2.imread("messi.jpeg", 0)

%timeit z = cv2.countNonZero(img)
%timeit z = np.count_nonzero(img)
