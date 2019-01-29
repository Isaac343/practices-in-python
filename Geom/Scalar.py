import cv2
import numpy as np

src = cv2.imread('idea.png')
dst = cv2.resize(src, None, fx=0.50, fy=0.70, interpolation=cv2.INTER_CUBIC)

cv2.imshow('idea.png', src)
cv2.imshow('Scale', dst)
cv2.waitKey()
