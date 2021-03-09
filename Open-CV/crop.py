import cv2 as cv

#cropping
image=cv.imread("./my.jpg")
print(image.shape) #prints resolutions 

resize = cv.resize(image,(200,200))

crop =image[0:50, 150:200]

cv.imshow("resized pic", resize)
cv.imshow("normal pic", image)#normal img

cv.imshow("normal pic croped", crop)#normal img


cv.waitKey(0)