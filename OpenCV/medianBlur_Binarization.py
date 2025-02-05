#!/usr/bin/env python3
""" Created on Wed Apr  3 14:54:28 2019 @author: jklhj """

import cv2
import numpy as np

def adaptiveThresh(img, winSize, ratio=0.15):
    img_mean = cv2.boxFilter(img, cv2.CV_32FC1, winSize)

    out = img - (1.0-ratio)*img_mean

    out[out>=0] = 255
 
    out[out<0] = 0 
 
    out = out.astype(np.uint8)
 
    return out

def calcGrayHist(image):
    rows, cols = image.shape

    grayHist = np.zeros([256], np.uint8)

    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] += 1

    return grayHist


#img = cv2.imread('Sc_257.bmp')
img = cv2.imread('587465-cut.png', 0)

width, height = img.shape
img = cv2.resize(img, (int(width*0.3), int(height*0.3)))

img_hist = calcGrayHist(img)
print(img_hist, img_hist.shape)

adap = adaptiveThresh(img, (31,31))

print(img.shape)


blur = cv2.medianBlur(img, 3)

#ret, thred_orig = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
ret, thred_orig = cv2.threshold(img, 50, 255, cv2.THRESH_OTSU)
print(ret)

#ret, thred_blur = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
ret, thred_blur = cv2.threshold(blur, 127, 255, cv2.THRESH_TRIANGLE)
print(ret)

cv2.imshow("Original", img)
cv2.imshow("medianBlur", blur)
cv2.imshow("thred_orig", thred_orig)
cv2.imshow("thred_blur", thred_blur)
cv2.imshow('adap', adap)
#
cv2.waitKey(0)  
