import cv2
import numpy as np
from matplotlib import pyplot as plt

# Gaussian Pyramid
img = cv2.imread('lena_color.jpg')
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr1 = cv2.pyrUp(lr2)

cv2.imshow("Org Img", img)
cv2.imshow("pyrDown1 Img", lr1)
cv2.imshow("pyrDown2 Img", lr2)
cv2.imshow("pyrUp1 Img", hr1)
cv2.waitKey(0)
cv2.destroyAllWindows()
