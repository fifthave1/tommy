import numpy as np
import cv2

img = cv2.imread('test.jpg', 1)
img_tommy = cv2.imread('img.jpg', 1)

print(img.shape)
print(img.size)
print(img.dtype)

print(img_tommy.shape)

empty = np.zeros((img.shape[0], img.shape[1]), np.uint8)
img_empty1 = np.zeros((150, 150, 3), np.uint8)
img_empty2 = img_empty1

b, g, r = cv2.split(img)
img2 = cv2.merge((b, g, r))
img_b = cv2.merge((b, empty, empty))
img_g = cv2.merge((empty, g, empty))
img_r = cv2.merge((empty, empty, r))

img2 = cv2.resize(img, (int(
    img.shape[1]*0.6), int(img.shape[0]*0.6)), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow('image', img2)
cv2.imshow('blue', img_b)
cv2.imshow('green', img_g)
cv2.imshow('red', img_r)


img_empty1 = img[200:350, 200:350]
img_empty2 = img[300:450, 300:450]
img_empty3 = cv2.add(img, img_tommy)
# gamma = additional scale value
# img_empty3 = cv2.addWeighted(img, 0.5, img_tommy, 0.5, 0)
# cv2.imshow('seg1', img_empty1)
# cv2.imshow('seg2', img_empty2)
cv2.imshow('add', img_empty3)


cv2.waitKey(0)
cv2.destroyAllWindows()
