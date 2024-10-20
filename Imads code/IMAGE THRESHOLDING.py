# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:18:03 2024

@author: Dell
"""

import cv2
img=cv2.imread("D:\Imads\car.jpeg")
imggray=cv2.imread("D:\Imads\car.jpeg",cv2.IMREAD_GRAYSCALE)
'''
output = imggray.copy()  
for i in range(imggray.shape[0]):
    for j in range(imggray.shape[1]):
        if imggray[i][j] > 127:
            output[i][j] = 255
        else:
            output[i][j] = 0
            '''
            
threshold_value=127
max_value=255
ret, output = cv2.threshold(imggray,threshold_value, max_value, cv2.THRESH_BINARY)

cv2.imshow("Original image", img)
cv2.imshow("Grayscale image", imggray)
cv2.imshow("Binary image", output)
cv2.waitKey(0)


