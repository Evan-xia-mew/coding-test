import cv2
import numpy as np
def contrast(img0):   
    img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY) 
    m, n = img1.shape

    img1_ext = cv2.copyMakeBorder(img1,1,1,1,1,cv2.BORDER_REPLICATE) 
    rows_ext,cols_ext = img1_ext.shape
    b = 0.0
    for i in range(1,rows_ext-1):
        for j in range(1,cols_ext-1):
            b += ((img1_ext[i,j]-img1_ext[i,j+1])**2 + (img1_ext[i,j]-img1_ext[i,j-1])**2 + (img1_ext[i,j]-img1_ext[i+1,j])**2 + (img1_ext[i,j]-img1_ext[i-1,j])**2)

    cg = b/(4*(m-2)*(n-2)+3*(2*(m-2)+2*(n-2))+2*4) 
    print(cg)
   
img0 = cv2.imread('exposure-4100.png')
contrast(img0)
img1 = cv2.imread('exposure-8100.png')
contrast(img1)
img2 = cv2.imread('exposure-12100.png')
contrast(img2)
img3 = cv2.imread('exposure-16100.png')
contrast(img3)
img4 = cv2.imread('exposure-20100.png')
contrast(img3)

#find largest number and use that img 