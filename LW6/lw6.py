import cv2.cv2 as cv2
import numpy as np
import math
img_path = "img.png"

BORDER_WIDTH = 10


straightRectColor = (0, 255, 0)




# preparation
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img_copy = cv2.copyMakeBorder(img, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, cv2.BORDER_CONSTANT, value=(255, 255, 255))
img_g = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
_, img_t = cv2.threshold(img_g, 140, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3, 3), np.uint8)

img_open0 = cv2.morphologyEx(img_t, cv2.MORPH_CLOSE, kernel, iterations=3)
# find all external contours
contours, hierarchy = cv2.findContours(img_open0, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
print("contours", contours)

_, img_open0 = cv2.threshold(img_open0, 140, 255, cv2.THRESH_BINARY_INV)
# for each detected contours
img_open0 = cv2.cvtColor(img_open0, cv2.COLOR_GRAY2BGR)
cv2.imshow('First detected contour', img_open0)
cv2.waitKey(0)
font                   = cv2.FONT_HERSHEY_COMPLEX
fontScale              = 0.7
fontColor              = (120,50,60)
thickness              = 2
lineType               = 2

X = 20
Y = 20
print(range(len(contours)))
for contour_num in range(len(contours)):


    # Find number of points of detected contour
    end_points = cv2.approxPolyDP(contours[contour_num], 0.01 * cv2.arcLength(contours[contour_num], True),True) #close contour length


    # (Rejecting unwanted contours)
    if (cv2.contourArea(contours[contour_num])) > 1000:

        # Find first point of each shape
        point_x = end_points[0][0][0]
        point_y = end_points[0][0][1]


        # If a contour have three end points,triangle
        if len(contours[contour_num]) == 3:
            cv2.putText(img_open0, '1',
                        (point_x+X, point_y+Y),
                        font,
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)

        # rectangle or square
        elif len(contours[contour_num]) == 4:
            x, y, w, h = cv2.boundingRect(end_points)
            # rectangle
            if (abs(w - h) > 3):
                cv2.putText(img_open0, '2',
                            (point_x+X, point_y+Y),
                            font,
                            fontScale,
                            fontColor,
                            thickness,
                            lineType)
            # square
            else:
                cv2.putText(img_open0, '4',
                            (point_x + X, point_y + Y),
                            font,
                            fontScale,
                            fontColor,
                            thickness,
                            lineType)

        # pentagon
        elif len(contours[contour_num]) == 5:
            cv2.putText(img_open0, '5',
                        (point_x+X, point_y+Y),
                        font,
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)

        # circle or ellipse
        elif len(contours[contour_num]) > 5:
            x, y, w, h = cv2.boundingRect(end_points)
            # ellipse
            if(abs(w-h)>10):
                cv2.putText(img_open0, '3',
                            (point_x+X, point_y+Y),
                            font,
                            fontScale,
                            fontColor,
                            thickness,
                            lineType)
                cv2.line(img_open0,  (point_x, point_y
                                      ),  (point_x+w, point_y+h), (0, 100, 0), 2)
                cv2.line(img_open0, (point_x +w, point_y), (point_x, point_y + h), (0, 100, 0), 2)
            # circle
            else:
                cv2.putText(img_open0, '1',
                            (point_x + X, point_y + Y),
                            font,
                            fontScale,
                            fontColor,
                            thickness,
                            lineType)

cv2.imshow('First detected contour',img_open0)
cv2.waitKey(0)
cv2.destroyAllWindows()