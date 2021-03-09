import cv2 as cv

vid = cv.VideoCapture("./vid.mp4")

while True:
	success,video=vid.read()
	cv.imshow("Le-frames",video)
	if cv.waitKey(1) and 0xFF == ord('q'):
		break
#cv.waitKey(0)