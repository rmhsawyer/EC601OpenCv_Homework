#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sun Nov  5 17:26:41 2017
    
    @author: mingheren
    """


import cv2
import  numpy as np 
#Load an image
img = cv2.imread('/Users/mingheren/Desktop/OpenCV_homework/Test_images/Lenna.png')
cv2.namedWindow("Image") 
cv2.imshow("Image",img)

#RGB
print("RGB value: ",img[20,25])

b,g,r = cv2.split(img)

cv2.namedWindow("Red")
cv2.imshow("Red",r)

cv2.namedWindow("Green")
cv2.imshow("Green",g)

cv2.namedWindow("Blue")
cv2.imshow("Blue",b)

#YCrCb
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

print("YCrCb value: ",img2[20,25])

Y,Cb,Cr = cv2.split(img2)
cv2.namedWindow("Y")
cv2.imshow("Y",Y)
cv2.namedWindow("Cb")
cv2.imshow("Cb",Cb)
cv2.namedWindow("Cr")
cv2.imshow("Cr",Cr)

#HSV
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print("HSV value: ",img3[20,25])

H,S,V = cv2.split(img3)
cv2.namedWindow("Hue")
cv2.imshow("Hue",H)
cv2.namedWindow("Saturation")
cv2.imshow("Saturation",S)
cv2.namedWindow("Value")
cv2.imshow("Value",V)

cv2.waitKey(0)
