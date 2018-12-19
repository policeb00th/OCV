import cv2
import numpy as num
img=cv2.imread('watch.jpg',1)
img[55,55]=(255,255,255)
px=img[55,55]
img[210:300,210:300]=img[110:200,110:200]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 