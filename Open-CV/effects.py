import cv2 as cv

pic = cv.imread("./my.jpg")
gray = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)
blur= cv.GaussianBlur(pic,(7,7),0)#rate should be odd

cv.imshow("gray pic", gray)
cv.imshow("normal pic", pic)
cv.imshow("blur pic", blur)
cv.waitKey(0)