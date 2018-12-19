import numpy as np
import cv2 
img=cv2.imread('watch.jpg',1)
pts=np.array([[10,20],[20,30],[30,40],[110,30],[60,70]],np.int64)
pts=pts.reshape((-1,1,2))
cv2.polylines(img, [pts],True,(119,119,119),15)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Iski maa ka bhosda',(0,130),font,1,(255,255,255),2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    