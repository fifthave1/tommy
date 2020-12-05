import numpy as np
import cv2

#img = np.zeros([256, 256, 3], np.uint8)

img = cv2.imread('dog2.jpg', 0)
print(img.shape)

img2 = cv2.resize(img, (700, 400), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('tommy', img2)
cv2.imwrite('test_img2.png', img2)

'''
# make blue block
cv2.circle(img, (100, 100), 50, (255, 0, 0), -1)
# make green block
cv2.circle(img, (200, 200), 50, (0, 255, 0), -1)
# make red block
cv2.circle(img, (300, 300), 50, (0, 0, 255), -1)
'''

# make spacial size img

#cv2.putText(img, 'Tommy', (100, 540), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 25, cv2.LINE_AA)

""" for j in range(0,256):
    for i in range(0,256):
        img[j,i,0] = i
        img[j,i,1] = i
        img[j,i,2] = i """


cv2.waitKey(0)
cv2.destroyAllWindows()
