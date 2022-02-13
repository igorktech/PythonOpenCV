import cv2.cv2 as cv2
import numpy as np
print(cv2)

#1
image_path = "LW1\\IMG.jpg"
img = cv2.imread(image_path, cv2.IMREAD_COLOR)
cv2.imshow("IMAGE1", img)
cv2.waitKey(5000)
cv2.destroyWindow("IMAGE1")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY IMAGE", img_gray)
cv2.waitKey(7000)
cv2.destroyWindow("GRAY IMAGE")

img_scale_down2 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow("IMAGE SCALE DOWN 2", img_scale_down2)
cv2.waitKey(9000)
cv2.destroyWindow("IMAGE SCALE DOWN 2")

img_scale_down4 = cv2.resize(img_gray, (0, 0), fx=0.25, fy=0.25)
cv2.imshow("IMAGE SCALE DOWN 4", img_scale_down4)
cv2.waitKey(11000)
cv2.destroyWindow("IMAGE SCALE DOWN 4")

#2
img2  = np.full((480, 640, 3), (1, 1, 1),np.float64)
cv2.line(img2, (0, 0), (639, 479), (0, 1, 0), 2)
cv2.circle(img2, (600, 40), 30, (1, 0, 0), 2)
cv2.rectangle(img2,(0,440),(100,479),(0,0,1),2)

font                   = cv2.FONT_HERSHEY_COMPLEX
bottomLeftCornerOfText = (400,40)
fontScale              = 0.5
fontColor              = (0,0,0)
thickness              = 1
lineType               = 2

cv2.putText(img2,'окружность',
    bottomLeftCornerOfText,
    font,
    fontScale,
    fontColor,
    thickness,
    lineType)

bottomLeftCornerOfText = (120,460)
cv2.putText(img2,'прямоугольник',
    bottomLeftCornerOfText,
    font,
    fontScale,
    fontColor,
    thickness,
    lineType)

bottomLeftCornerOfText = (100,240)
cv2.putText(img2,'линия',
    bottomLeftCornerOfText,
    font,
    fontScale,
    fontColor,
    thickness,
    lineType)
cv2.imshow("DRAW", img2)
cv2.waitKey(5000)
cv2.destroyWindow("DRAW")


#3

img_color  = np.full((320, 480, 3), (1, 1, 1),np.float64)

i = 0
k = 0
for i in range(0,6):
    for k in range(0,4):
        cv2.rectangle(img_color,(i*160+(k%2)*80,k*80),(i*160+80+(k%2)*80,k*80+80),(1,0,1),-1)
cv2.imshow("CHESS",img_color)
cv2.waitKey(0)
cv2.destroyWindow("CHESS")
#4
idx = 0
cap = cv2.VideoCapture(idx)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray feed', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


        
cap.release()
cv2.destroyAllWindows()


