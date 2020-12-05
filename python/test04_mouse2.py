import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        strtext = str(y)+','+str(x)  # 행(row) & 열(column)
        cv2.putText(img, strtext, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)

    # 마우스 움직임도 이벤트가 됨. 각 조건문에 별도로 프린트 구문을 넣어야 함.
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]            # 마우스 좌표 : x,y >> 이미지 좌표 : y,x
        green = img[y, x, 1]
        red = img[y, x, 2]
        mycolor = np.zeros((200, 200, 3), np.uint8)
        mycolor[:] = [blue, green, red]
        print(blue, green, red)
        cv2.imshow('color', mycolor)
        strtext = str(blue)+','+str(green)+','+str(red)
        cv2.putText(img, strtext, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)


img = cv2.imread('test.jpg', 1)
width, height, channel = img.shape
print(width, height, channel)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
