import numpy as np
import cv2.cv2 as cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
#1
image_path = "LW2\\lab2-1.jpg"
img = mpimg.imread(image_path)
img1 = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_4)
image_path = "LW2\\lab2-2.jpg"
img2 = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_4)
image_path = "LW2\\lab2-3.jpg"
img3 = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_4)

#manual threshold 
threshold = 127
maxVal = 255

#cv2.THRESH_BINARI
threshold_new, thresh_binary = cv2.threshold(img1,threshold,maxVal,cv2.THRESH_BINARY)


#cv2.THRESH_BINARY_INV
threshold_new, thresh_binary_inv = cv2.threshold(img2,threshold,maxVal,cv2.THRESH_BINARY_INV)


#cv2.THRESH_TOZERO
threshold_new, thresh_tozero = cv2.threshold(img3,threshold,maxVal,cv2.THRESH_TOZERO)


#cv2.THRESH_TOZERO_INV 
threshold_new, thresh_tozero_inv = cv2.threshold(img1,threshold,maxVal,cv2.THRESH_TOZERO_INV)


#cv2.THRESH_TRUNC
threshold_new, thresh_trunc = cv2.threshold(img2,threshold,maxVal,cv2.THRESH_TOZERO_INV)


#automatic threshold
#triangle method
#cv2.THRESH_TRIANGLE
threshold_new, thresh_triangle = cv2.threshold(img2,threshold,maxVal,cv2.THRESH_TRIANGLE)
print(threshold_new)


#Otsu's method
#cv2.THRESH_OTSU
threshold_new, thresh_otsu = cv2.threshold(img1,threshold,maxVal,cv2.THRESH_OTSU)
# n, bins, patches =plt.hist(img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
# plt.show()
print(threshold_new)

titles = ['Original Image 1','Original Image 2','Original Image 3','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV','THRESH_TRIANGLE','THRESH_OTSU']
images = [img1,img2,img3, thresh_binary, thresh_binary_inv, thresh_trunc, thresh_tozero,thresh_tozero_inv, thresh_triangle,thresh_otsu]
for i in range(10):
    plt.subplot(2,5,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)


#2
image_path = "LW2\\text.png"
img_text = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_4)

# adaptive methods

new_img =  cv2.adaptiveThreshold(img_text,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)
cv2.imshow("IMG TEXT",img_text)
cv2.imshow("THRESH_GAUSSIAN",new_img)
new_img2 =  cv2.adaptiveThreshold(img_text,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,10)
cv2.imshow("THRESH_MEAN",new_img2)
cv2.waitKey(0)

#3

cap = cv2.VideoCapture("LW2\\lab2-4.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gr, (0, 0), fx=0.25, fy=0.25)
    new_gray=  cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,35,25)
    cv2.imshow('frame', new_gray)
    # if q we leave
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()

#question 1
image_path = "LW2\\test.jpg"
img_test = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_4)
new_img =  cv2.adaptiveThreshold(img_test,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,10)
cv2.imshow("IMG TEXT",img_test)
cv2.imshow("THRESH_GAUSSIAN",new_img)
new_img2 =  cv2.adaptiveThreshold(img_test,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,25)
cv2.imshow("THRESH_MEAN",new_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()