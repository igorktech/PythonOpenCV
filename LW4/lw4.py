

import cv2
import numpy as np


#1
# IMAGE_1 = "LW4\\text.png"

# img_text = cv2.imread(IMAGE_1, cv2.IMREAD_GRAYSCALE)
# cv2.imshow("IMAGE", img_text)

# img_1_t = cv2.adaptiveThreshold(img_text,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,9)
# cv2.imshow("1",img_1_t)
# kernel = np.ones((5, 5), np.uint8)
# img_erode0 = cv2.erode(img_1_t, kernel, iterations=1)
# cv2.imshow("Erode0", img_erode0)
# kernel = np.ones((3, 3), np.uint8)
# img_open0 = cv2.morphologyEx(img_erode0, cv2.MORPH_CLOSE, kernel, iterations=3)
# cv2.imshow("Open00", img_open0)

# cv2.waitKey(0)


#2
kernel = np.ones((3, 3), np.uint8)
cap = cv2.VideoCapture("LW4\\lab2-4.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gr, (0, 0), fx=0.25, fy=0.25)
    new_gray=  cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,35,25)
    img_dilate  = cv2.dilate(new_gray,kernel,iterations = 1)
    img_open = cv2.morphologyEx(img_dilate, cv2.MORPH_OPEN, kernel, iterations=10)
    cv2.imshow('frame', img_open)
    # if q we leave
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()