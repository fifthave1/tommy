import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX


def click_event(event, x, y, flags, param):
    # 마우스 움직임도 이벤트가 됨. 각 조건문에 별도로 프린트 구문을 넣어야 함.
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
        points.append((x, y))
        print(points)
        if len(points) % 2:
            cv2.line(img, points[-1], points[-2], (0, 255, 0), 5)
        cv2.imshow('image', img)


img = cv2.imread('test.jpg', 1)
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
