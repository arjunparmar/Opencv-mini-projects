import cv2
import numpy as np

cap=cv2.VideoCapture("my.avi")
fg_bg=cv2.BackgroundSubtractorMOG2()

while True:
    ret,frame=cap.read()
    fgmask=fg_bg.apply(frame)
    cv2.imshow("op",fgmask)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()