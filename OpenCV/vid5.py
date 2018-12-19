import cv2  
import numpy as np 
img2=cv2.imread('C.png')
img1=cv2.imread('A.png')
'''add=img1+img2
add=cv2.add(img1,img2)
weighted=cv2.addWeighted(img1,0,img2,1,0)
cv2.imshow('add',weighted)'''
rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]

imggray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(imggray,220,255,cv2.THRESH_BINARY_INV)
mask_inv=cv2.bitwise_not(mask)
img1_bckg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_frg=cv2.bitwise_and(img2,img2,mask=mask)
d=cv2.add(img1_bckg,img2_frg)
img1[0:rows,0:cols]=d
cv2.imshow('img',imggray)
cv2.imshow('mask_inv',mask)
cv2.imshow('img1_bckg',img1_bckg)
cv2.imshow('img2_frg',img2_frg)
cv2.imshow('d',d)

cv2.waitKey(0)  
cv2.destroyAllWindows()