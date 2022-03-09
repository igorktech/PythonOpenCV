import numpy as np
import cv2.cv2 as cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
#1
image_path = "LW3\\3-1.png"
img31 = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_4)
img31_color = cv2.imread(image_path, cv2.IMREAD_REDUCED_COLOR_4)
image_path = "LW3\\3-2.png"
img32 = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_4)
img32_color = cv2.imread(image_path, cv2.IMREAD_REDUCED_COLOR_4)

# img_blur = cv2.blur(img31_color, (11, 11))
# cv2.imshow("BLUR COLOR", img_blur)
# img_blur = cv2.blur(img31, (11, 11))
# cv2.imshow("BLUR", img_blur)
# img_box= cv2.boxFilter(img31_color, -1, (11, 11), normalize=True)
# cv2.imshow("BOX COLOR", img_box)  
# img_box= cv2.boxFilter(img31, -1, (11, 11), normalize=True)
# cv2.imshow("BOX", img_box) 
# cv2.waitKey(0)

# img_median = cv2.medianBlur(img31_color, 11)
# cv2.imshow("MEDIAN COLOR", img_median)
# img_median = cv2.medianBlur(img31, 11)
# cv2.imshow("MEDIAN", img_median)
# cv2.waitKey(0)


# cv2.waitKey(0)

# img_gauss = cv2.GaussianBlur(img31_color, (3, 3), 0)
# cv2.imshow("GAUSS COLOR", img_gauss)
# img_gauss = cv2.GaussianBlur(img31, (3, 3), 0)
# cv2.imshow("GAUSS", img_gauss)
# cv2.waitKey(0)

# img_bilateral = cv2.bilateralFilter(img31_color, d=50, sigmaColor=200, sigmaSpace=50)
# cv2.imshow("BILATERAL COLOR", img_bilateral)
# img_bilateral = cv2.bilateralFilter(img31, d=50, sigmaColor=200, sigmaSpace=50)
# cv2.imshow("BILATERAL", img_bilateral)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
#2
image_path = "LW3\\3-3.png"
img33 = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_2)
img33_color = cv2.imread(image_path, cv2.IMREAD_REDUCED_COLOR_2)
image_path = "LW3\\3-4.png"
img34 = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_2)
img34_color = cv2.imread(image_path, cv2.IMREAD_REDUCED_COLOR_2)


img_gauss_color = cv2.GaussianBlur(img34_color , (5, 5), 0)
cv2.imshow("GAUSS COLOR", img_gauss_color)
img_gauss = cv2.GaussianBlur(img34, (5, 5), 0)
cv2.imshow("GAUSS", img_gauss)
cv2.waitKey(0)

img_bilateral = cv2.bilateralFilter(img_gauss_color, d=5, sigmaColor=150, sigmaSpace=150)
cv2.imshow("BILATERAL COLOR", img_bilateral)
img_bilateral = cv2.bilateralFilter(img_gauss, d=5, sigmaColor=100, sigmaSpace=150)
cv2.imshow("BILATERAL", img_bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

