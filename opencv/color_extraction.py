import numpy as np
import cv2

mode = True


def get_mask(event, x, y, flag, param):
    global mode

    if event == cv2.EVENT_LBUTTONDOWN and mode:
        print("Pixel ({},{})".format(x, y))
        color = messi[y, x]
        print("Color of pixel is {}.".format(color))
        hsv_color = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)
        print("HSV value for color is {}".format(hsv_color[0, 0]))
        lower_bound = hsv_color[0, 0]-30
        upper_bound = hsv_color[0, 0]+30
        mask = cv2.inRange(hsv_messi, lower_bound, upper_bound)
        result = cv2.bitwise_or(messi, messi, mask=mask)
        cv2.imshow('result', result)
        if(cv2.waitKey(0) & 0xFF == ord('x')):
            cv2.destroyWindow('result')


messi = cv2.imread("messi.jpeg")
hsv_messi = cv2.cvtColor(messi, cv2.COLOR_BGR2HSV)
print("Image shape is {}".format(messi.shape))
cv2.namedWindow('image')

# cv2.namedWindow('result')
# black_img = np.zeros(messi.shape[:2], np.uint8)
# cv2.setMouseCallback('image', get_mask)

while(1):
    lower_bound1, upper_bound1 = np.array([30, 148, 135]), np.array([70, 208, 175])
    mask1 = cv2.inRange(hsv_messi, lower_bound1, upper_bound1)
    lower_bound2, upper_bound2 = np.array([81, 187, 156]), np.array([141, 247, 216])
    mask2 = cv2.inRange(hsv_messi, lower_bound2, upper_bound2)
    mask = cv2.bitwise_or(mask1, mask2)
    bit_and = cv2.bitwise_and(messi, messi, mask=mask)
    cv2.imshow('image', bit_and)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('m'):
        print("Mode toggled")
        mode = not mode

cv2.destroyAllWindows()
