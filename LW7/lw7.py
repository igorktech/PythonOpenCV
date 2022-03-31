import cv2.cv2 as cv2
import numpy as np
import math
#image path
path_lines = "Lines.png"
path_circles = "Circles.png"
path_sign1 = "Road_sign1.jpg"
path_sign2 = "Road_sign2.jpg"
path_sign3 = "Road_sign3.jpg"
# draw HoughLines
def draw_line(rho, theta, img, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA):
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        x0 = cos_t * rho
        y0 = sin_t * rho
        pt1 = int(x0 - 1000 * sin_t), int(y0 + 1000 * cos_t)
        pt2 = int(x0 + 1000 * sin_t), int(y0 - 1000 * cos_t)
        cv2.line(img, pt1, pt2, color, thickness, lineType)

# draw HoughLinesP
def draw_line_P(x0, y0, x1, y1, img, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA):
    cv2.line(img, (x0, y0), (x1, y1), color, thickness, lineType)

# show image on a screen
def show(name, img):
    cv2.namedWindow(name)
    cv2.imshow(name, img)
# #1
# img = cv2.imread(path_lines, cv2.IMREAD_REDUCED_COLOR_2)
# img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# _,img_th = cv2.threshold(img_g,127,255,cv2.THRESH_BINARY_INV)
# cv2.imshow("GRAYSCALE", img)
#
# lines = cv2.HoughLines(img_th, 1, math.pi/60, 70)
# hv_lines = cv2.HoughLines(img_th, 1, math.pi/2, 70)
# for line in lines:
#     #print("line: ", line)
#     line = line[0]
#     draw_line(line[0], line[1], img)
# cv2.imshow("LINES", img)
# cv2.waitKey()
# # find vertical and horizontal lines
# for line in hv_lines:
#     line = line[0]
#     draw_line(line[0],line[1],img, color=(0,255,0))
# cv2.imshow("LINES", img)
# cv2.waitKey()
#
# # find the largest line
# lines = cv2.HoughLinesP(img_th, 1, math.pi/90, 100)
# print(lines)
# print("lines:", len(lines))
#
# res = [0,0,0,0]
# for [[x0, y0, x1, y1]] in lines:
#     if math.sqrt(abs(x0 - x1) ** 2 + abs(y0 - y1) ** 2) > math.sqrt(abs(res[0] - res[1]) ** 2 + abs(res[2] - res[3]) ** 2):
#         res = [x0, y0, x1, y1]
#         print(res)
# x0,y0,x1,y1 = res
# draw_line_P(x0, y0, x1, y1, img, (255, 0, 0), thickness=2)
#
# cv2.imshow("LINES", img)
# cv2.waitKey(0)
# #2
# cap = cv2.VideoCapture("test_video.mp4")
# straightRectColor = (200, 255, 70)
# BORDER_WIDTH = 2
# threshold = 125
# maxVal = 255
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     img_g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     _,img_th = cv2.threshold(img_g,threshold,maxVal,cv2.THRESH_BINARY_INV)
#     lines = cv2.HoughLinesP(img_th, 1, math.pi / 2, 400)
#     if lines is not None:
#         for [[x0, y0, x1, y1]] in lines:
#             draw_line_P(x0, y0, x1, y1, frame, straightRectColor, thickness=BORDER_WIDTH)
#
#     # delay
#     cv2.waitKey(10)
#     # show result
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cap.release()
# #3
#
#
#
# img = cv2.imread(path_circles, cv2.IMREAD_COLOR)
# A = img.shape[0]
# img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_g = cv2.GaussianBlur(img_g, (11, 11), 0)
# # dp - accumulator scale
# # minDist - distance between two circles
# # param1 - high Canny threshold
# # pamam2 - accumulator threshold
# circles = cv2.HoughCircles(img_g, cv2.HOUGH_GRADIENT, 1, minDist=(A//16), param1=100, param2=A//16)
#
#
# print("\n", circles)
# if circles is not None:
#     for circle in circles[0]:
#         print(circle)
#         cv2.circle(img, (int(circle[0]), int(circle[1])), int(circle[2]), color=(0, 0, 255), thickness=3)
#
# show("SOURCE", img)
# cv2.waitKey(0)


#4
img = cv2.imread(path_sign1, cv2.IMREAD_COLOR)
A = img.shape[0]
img_bilat = cv2.bilateralFilter(img, d=50, sigmaColor=60, sigmaSpace=30)
img_g = cv2.cvtColor(img_bilat, cv2.COLOR_BGR2GRAY)
img_th = cv2.adaptiveThreshold(img_g,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)
img_gauss = cv2.GaussianBlur(img_g, (11, 11), 0)

canny = cv2.Canny(img_gauss, threshold1=75,threshold2=150,apertureSize=3)
cv2.imshow("Canny", canny)
# dp - accumulator scale
# minDist - distance between two circles
# param1 - high Canny threshold
# pamam2 - accumulator threshold
circles = cv2.HoughCircles(img_gauss, cv2.HOUGH_GRADIENT, 1, minDist=(A//32), param1=100, param2=A//8)



print("\n", circles)
if circles is not None:
    for circle in circles[0]:
        print(circle)
        cv2.circle(img, (int(circle[0]), int(circle[1])), int(circle[2]), color=(0, 0, 255), thickness=3)

show("SOURCE1", img)
cv2.waitKey(0)

#4.2
img = cv2.imread(path_sign2, cv2.IMREAD_COLOR)
A = img.shape[0]
img_bilat = cv2.bilateralFilter(img, d=50, sigmaColor=60, sigmaSpace=30)
img_g = cv2.cvtColor(img_bilat, cv2.COLOR_BGR2GRAY)
img_th = cv2.adaptiveThreshold(img_g,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)
img_gauss = cv2.GaussianBlur(img_g, (11, 11), 0)

canny = cv2.Canny(img_gauss, threshold1=75,threshold2=100,apertureSize=3)
cv2.imshow("Canny", canny)
# dp - accumulator scale
# minDist - distance between two circles
# param1 - high Canny threshold
# pamam2 - accumulator threshold
circles = cv2.HoughCircles(img_gauss, cv2.HOUGH_GRADIENT, 1, minDist=(A//8), param1=100, param2=A//16+A//8)



print("\n", circles)
if circles is not None:
    for circle in circles[0]:
        print(circle)
        cv2.circle(img, (int(circle[0]), int(circle[1])), int(circle[2]), color=(0, 0, 255), thickness=3)

show("SOURCE2", img)
cv2.waitKey(0)

#4.3
img = cv2.imread(path_sign3, cv2.IMREAD_COLOR)
A = img.shape[0]
img_bilat = cv2.bilateralFilter(img, d=50, sigmaColor=60, sigmaSpace=30)
img_g = cv2.cvtColor(img_bilat, cv2.COLOR_BGR2GRAY)
img_th = cv2.adaptiveThreshold(img_g,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)
img_gauss = cv2.GaussianBlur(img_g, (11, 11), 0)

canny = cv2.Canny(img_gauss, threshold1=75,threshold2=100,apertureSize=3)
cv2.imshow("Canny", canny)
# param1 - high Canny threshold
# pamam2 - accumulator threshold
circles = cv2.HoughCircles(img_gauss, cv2.HOUGH_GRADIENT, 1, minDist=(A//16), param1=100, param2=A//16+A//16)



print("\n", circles)
if circles is not None:
    for circle in circles[0]:
        print(circle)
        cv2.circle(img, (int(circle[0]), int(circle[1])), int(circle[2]), color=(0, 0, 255), thickness=3)

show("SOURCE3", img)
cv2.waitKey(0)



