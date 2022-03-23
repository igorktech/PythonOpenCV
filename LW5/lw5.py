import numpy as np
import cv2.cv2 as cv2

image_path = "test_sobel.jpeg"
image_path2 = "2.png"
image_path3 = "test_filters.jpg"


#1
img = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_4)
cv2.imshow("IMAGE", img)

sobel = cv2.Sobel(img, cv2.CV_8U, dx=1, dy=1, ksize=3)  #На изображение накладывается ядро K размером s на s пикселей, для каждого пикселя считается взвешенная сумма пикселей, на
                                                        #которые наложено ядро оператора.
"""
ksize = 1 ->  1 x 3 or 3 x 1 (no Gaussian smoothing)
"""
cv2.imshow("Sobel", sobel)

laplace = cv2.Laplacian(img, -1, ksize=3) #сумма частных производных второго порядка
cv2.imshow("Laplacian", laplace)

img_gauss = cv2.GaussianBlur(img, (5, 5), 0)
canny = cv2.Canny(img_gauss, threshold1=30, #нижинй порог
                  threshold2=120,#верхний порог
                  apertureSize=3)
#Вычисление градиента выполняется с помощью уже известного оператора
#Собеля. Он применяется дважды: для вычисления значения в горизонтальном
#направлении – значение Gx – и в вертикальном направлении – значение Gy
#По этим данным можно вычислить модуль и направление градиента.

#В последний аргумент передаем булевое значение L2gradient. Если
#значение True, то градиент по направлению вычисляется с помощью нормы L2,
#если значение False – с помощью нормы L1.
cv2.imshow("Canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()



#2
img_border1 = cv2.imread(image_path2, cv2.IMREAD_REDUCED_COLOR_2)
# excluding noise
img_bilat = cv2.bilateralFilter(img_border1, d=50, sigmaColor=60, sigmaSpace=30)
img_gauss = cv2.GaussianBlur(img_bilat, (7, 7), 0)

canny = cv2.Canny(img_gauss, threshold1=45, #нижинй порог
                  threshold2=90,#верхний порог
                  apertureSize=3)
cv2.imshow("Canny", canny)

cv2.waitKey(0)
img_border2 = cv2.imread(image_path3,cv2.IMREAD_REDUCED_COLOR_2  )

img_gauss2 = cv2.GaussianBlur(img_border2, (11, 11), 0)

canny2 = cv2.Canny(img_gauss2, threshold1=45, #нижинй порог
                  threshold2=90,#верхний порог
                  apertureSize=3)
cv2.imshow("Canny2", canny2)

cv2.waitKey(0)

#3
cap = cv2.VideoCapture("test_video.mp4")
kernel = np.ones((3, 3), np.uint8)
straightRectColor = (200, 255, 70)
BORDER_WIDTH = 5
threshold = 125
maxVal = 255
kernel = np.ones((3, 3), np.uint8)
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # prepearation for canny borders
    gray_gauss = cv2.GaussianBlur(frame, (11, 11), 0)
    # find all borders with canny
    canny_video = cv2.Canny(gray_gauss, threshold1=30,  # lower
                       threshold2=100,  # upper
                       apertureSize=3)
    # preparation for window boder excluding
    _, thresh_binary_inv = cv2.threshold(canny_video,threshold,maxVal,cv2.THRESH_BINARY_INV)
    # additing border to picture
    img_copy = cv2.copyMakeBorder(thresh_binary_inv, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, cv2.BORDER_CONSTANT,
                                  value=(255, 255, 255))
    # making lines wider
    img_erode = cv2.erode(img_copy,kernel,iterations = 4)

    # connecting lines together
    img_open = cv2.morphologyEx(img_erode, cv2.MORPH_OPEN, kernel, iterations=10)
    # inversion to exclude window border
    _, thresh_binary_inv = cv2.threshold(img_open,threshold,maxVal,cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh_binary_inv, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    print("contours", len(contours))

    if(contours != ()):
        # main external contour that we have to detect
        mainContour = contours[0]
        x, y, w, h = cv2.boundingRect(mainContour)
        # draw this rect on our picture
        cv2.rectangle(frame, (x-BORDER_WIDTH , y-BORDER_WIDTH), (x + w, y + h), straightRectColor, 16)
    # delay
    cv2.waitKey(10)
    # show result
    cv2.imshow('frame',frame)
    cv2.imshow('canny',canny_video)

    # if q we leave
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()