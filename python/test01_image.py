import numpy as np
import matplotlib.pyplot as plt
import cv2

#img = cv2.imread('lena_color.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 3)  # bgr
img = cv2.arrowedLine(img, (0, 255), (255, 0), (0, 255, 0), 3)  # bgr
img = cv2.rectangle(img, (255, 255), (511, 511), (0, 0, 255), 2)
img = cv2.circle(img, (255, 255), 100, (0, 255, 255), 2)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, 400), font, 4,(255, 255, 255), 19, cv2.LINE_AA)

cv2.imshow('tommy', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
1