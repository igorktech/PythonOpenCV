
import cv2.cv2 as cv2
import numpy as np

#IMAGE = "C:\\Users\\User\\Desktop\\CV_scripts\\image.png"

#img = cv2.imread(IMAGE, cv2.IMREAD_COLOR)
#print(img.shape[0])
# cv2.line(img, (20, 20), (200, 200), (0, 255, 0), 5)

# cv2.imwrite("C:\\Users\\User\\Desktop\\CV_scripts\\image_gray.png", img)
# print("finished")

# img2 = np.copy(img)
# cv2.imshow("IMAGE2", img2)

img_zeros = np.zeros((480, 640, 3))
cv2.imshow("IMAGE_ZEROS", img_zeros)
#cv2.imshow("ONES", img_ones)
cv2.waitKey(4000)
print(type(img_zeros[0, 0, 0]))

img_ones = np.ones((480, 640, 3))
cv2.imshow("ONES", img_ones)
cv2.waitKey(4000)
# img_color = np.full((480, 640, 3), (255/255, 0/255, 255/255))
# print(type(img_color[0, 0, 0]))
# cv2.imshow("COLOR", img_color)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.line(img_gray, (20, 20), (200, 200), (0, 255, 0), 5)
cv2.imshow("GRAY IMAGE", img_gray)

b, g, r = cv2.split(img)
# cv2.imshow("b", b)
# cv2.imshow("g", g)
# cv2.imshow("r", r)

img_rgb = cv2.merge([r, g, b])
cv2.imshow("merged", img_rgb)


cv2.imshow("IMAGE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.destroyWindow("name")
print("END")