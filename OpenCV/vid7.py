import cv2
import numpy as np
img = cv2.imread("3.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([85, 100, 100])
upper_red = np.array([130, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask=mask)
kernel = np.ones((15, 15), np.float64)/225
smooth = cv2.filter2D(res, -1, kernel)
blur = cv2.GaussianBlur(img, (15, 15), 0)
median = cv2.medianBlur(res, 15)
edges=cv2.Canny(blur,25,25)
# bilateral=cv2.bilateralFilter(res,15,75,75) #eats a lot of processing power
cv2.imshow('res', res)
cv2.imshow('smooth', smooth)
cv2.imshow('canny',edges)
cv2.imshow('median', median)
cv2.imshow('image',img)
# cv2.imshow('bilateral',bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

