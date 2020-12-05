import numpy as np
import matplotlib.pyplot as plt
import cv2
import datetime

cap = cv2.VideoCapture(1)
cap.set(3,1280)  # 3: width of video
cap.set(4,720)  # 4: height of video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        date = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, date, (10, 50), font, 1,
                    (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break
cap.release()
# out.release()
cv2.destroyAllWindows()
