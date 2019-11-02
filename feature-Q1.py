#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2 as cv
import numpy as np
 
def contrast_brightness_image(src1, a, g):
    h, w, ch = src1.shape
 

    src2 = np.zeros([h, w, ch], src1.dtype)
    dst = cv.addWeighted(src1, a, src2, 1-a, g)
    cv.imshow("con-bri-demo", dst)
 
src = cv.imread("exposure-4100.png")
cv.namedWindow("original", cv.WINDOW_NORMAL)
cv.imshow("original", src)
contrast_brightness_image(src, 1.3, 80)
cv.waitKey(0)

cv.destroyAllWindows()
