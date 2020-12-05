import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena_color.png', cv2.IMREAD_GRAYSCALE)
# b, g, r = cv2.split(img)
# img = cv2.merge([r, g, b])


# Canny Edge detection
# step 1 : Noise reduction
# step 2 : Gradient Cal
# step 3 : Non-Maximum suppression
# step 4 : Double threshold
# step 5 : Edge Tracking by Hysteresis

canny = cv2.Canny(img, 100, 200)


titles = ['image', 'canny']
images = [img, canny]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
