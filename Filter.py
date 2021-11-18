import cv2
import numpy as np
img= cv2.imread('wallpaper2you_24547.jpg')
rimg= cv2.resize(img, (448,224))
cv2.imshow('Original', rimg)
cv2.waitKey(0)

#Filter
Iden = np.array([[0,0,0],[0,1,0],[0,0,0]])
Edge1 =np.array([[1,0,-1],[0,0,0],[-1,0,1]])
Edge2 =np.array([[0,1,0],[1,-4,1],[0,1,0]])
Edge3 =np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
Shapr =np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
Blur = np.array([[1,1,1],[1,1,1],[1,1,1]])*1/9
#Identity kernel
im1 = cv2.filter2D(rimg, -1, Iden)
cv2.imshow('Identity kernel', im1)
#shapening kernel
im2 = cv2.filter2D(rimg, -1, Shapr)
cv2.imshow('Sharpening kernel', im2)
#Edge kernel
im3 = cv2.filter2D(rimg, -1, Edge1)
cv2.imshow('Edge1 kernel', im3)
im4 = cv2.filter2D(rimg, -1, Edge2)
cv2.imshow('Edge2 kernel', im4)
im5 = cv2.filter2D(rimg, -1, Edge3)
cv2.imshow('Edge3 kernel', im5)
#Blur kernel
im6 = cv2.filter2D(rimg, -1, Blur)
cv2.imshow('Blur kernel', im6)
cv2.waitKey(0)