import numpy as np
import matplotlib.pyplot as plt
import cv2

print(cv2.__version__)
image = cv2.imread("lena_color.jpg", 1)
len_x = len(image)
len_y = len(image[0])
print(len_x, len_y)
hist = list()

hist = np.zeros([255], np.uint8)
"""
for li in range(0, 255):
    hist.append(0)
print(image[0][0][0])
"""

for x in range(0, len_x):
    for y in range(0, len_y):
        hist[image[x][y][0]] += 1

plt.bar(range(0, 255), hist)
plt.show()
cv2.imshow("lena", image)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("lena_color.png", image)
    cv2.destroyAllWindows()
