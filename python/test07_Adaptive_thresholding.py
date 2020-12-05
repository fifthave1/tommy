import cv2
import numpy as np

img = cv2.imread('sudoku.png',0)
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# adaptive threshold는 입력으로 1ch을 받기 때문에, 입력 이미지를 Gray로 변환해야 한다.
# 컬러 이미지는 error 발생함.

cv2.imshow('image', img)
cv2.imshow('th1', th1)
cv2.imshow('Adaptive th2_M', th2)
cv2.imshow('Adaptive th2_G', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
