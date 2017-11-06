#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 17:26:41 2017

@author: mingheren
"""

import cv2
import numpy as np 


def Add_gaussian_Noise(img,mean,sigma):
    noiseArr = img.copy()
    noiseArr = np.random.normal(mean,sigma,img.shape)
    np.add(img,noiseArr,img,casting="unsafe")
    return;

def Add_salt_pepper_Noise(img,pa,pb):
    row,col,ch=img.shape
#Controls the amount of black spots in the noise
    amount1=row*col*pa
#Controls the amount of white spots in the noise    
    amount2=row*col*pb
    for i in range(int(amount1)):
        img[int(np.random.uniform(0,row))][int(np.random.uniform(0,col))]=0
    for i in range(int(amount2)):
        img[int(np.random.uniform(0,row))][int(np.random.uniform(0,col))]=255

def main():

    img=cv2.imread('/Users/mingheren/Desktop/OpenCV_homework/Test_images/Lenna.png')
    cv2.namedWindow('Original image')
    cv2.imshow('Original',img)

#gaussian_Noise
    noise_img=img.copy()
    mean=0
    sigma=50
    Add_gaussian_Noise(noise_img,mean,sigma)
    cv2.imshow('Gaussian Noise',noise_img)

    noise_dst=noise_img.copy()
    cv2.blur(noise_dst,(3,3))
    cv2.imshow('Box filter',noise_dst)

    noise_dst1=noise_img.copy()
    cv2.GaussianBlur(noise_dst1,(3,3),1.5)
    cv2.imshow('GaussianBlur filter',noise_dst1)

    noise_dst2=noise_img.copy()
    cv2.medianBlur(noise_dst2,3)
    cv2.imshow('Median filter',noise_dst2)


#salt_pepper_Noise
    noise_img2=img.copy()
    pa=0.01
    pb=0.01
    Add_salt_pepper_Noise(noise_img2,pa,pb)
    cv2.imshow("Salt and Peper Noise", noise_img2)

    noise_dst3=noise_img2.copy()
    cv2.blur(noise_dst3,(3,3))
    cv2.imshow('Box filter2',noise_dst3)

    noise_dst4=noise_img2.copy()
    cv2.GaussianBlur(noise_dst4,(3,3),1.5)
    cv2.imshow('GaussianBlur filter2',noise_dst4)

    noise_dst5=noise_img2.copy()
    cv2.medianBlur(noise_dst5,3)
    cv2.imshow('Medianfilter2',noise_dst5)
    
    print('mean:',mean)
    print('sigma:',sigma)
    print('pa:',pa)
    print('pb:',pb)
    print('best kernel size: 3x3')
   
    cv2.waitKey(0)


if __name__ == "__main__":
    main()














