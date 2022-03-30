import cv2
import numpy as np

# path
IMAGE_1 = "ref.png"    # template
IMAGE_2 = "task.png"     # source image

# display function
def show(name, img):
    cv2.namedWindow(name)
    cv2.imshow(name, img)

# template preparation
img_1_color = cv2.imread(IMAGE_1, cv2.IMREAD_REDUCED_COLOR_2)
img_1 = cv2.cvtColor(img_1_color, cv2.COLOR_BGR2GRAY)
img_1 = 255 - img_1
img_1 = cv2.GaussianBlur(img_1, (3, 3), 0)


# source image preparation
img_2_color = cv2.imread(IMAGE_2, cv2.IMREAD_REDUCED_COLOR_2)
img_2 = cv2.cvtColor(img_2_color, cv2.COLOR_BGR2GRAY)
img_2 = 255 - img_2
img_2 = cv2.GaussianBlur(img_2, (3, 3), 0)

# find contours
contours1, _ = cv2.findContours(img_1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours2, _ = cv2.findContours(img_2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

mu_1_0 = cv2.moments(contours1[0])
hu_1_0 = cv2.HuMoments(mu_1_0)
# print('mu_source', mu_1_0)
# print("source Hu moments: ", hu_1_0)
for i in range(len(contours2)):
    mu_2_i = cv2.moments(contours2[i])
    hu_2_i = cv2.HuMoments(mu_2_i)
    print('mu_2_i', mu_2_i)
    # check rotation moments
    if abs((hu_1_0[0] - hu_2_i[0]) / hu_1_0[0]) <= 0.04:
        if abs((hu_1_0[1] - hu_2_i[1]) / hu_1_0[1]) <= 0.2:
            # check length
            if abs((mu_1_0['m00'] - mu_2_i['m00']) / mu_1_0['m00']) <= 0.43:
                cv2.drawContours(img_2_color, contours2, i, (200, 190, 255), 2)

show("PATTERN", img_1_color)
show("RESULT", img_2_color)

while cv2.waitKey(0) !=ord('q'):
    pass