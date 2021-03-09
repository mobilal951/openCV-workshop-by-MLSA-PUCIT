import cv2 as cv

image = cv.imread("./my.jpg")

cv.imshow("my-img",image)
cv.waitKey(0)