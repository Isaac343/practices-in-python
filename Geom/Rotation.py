import cv2
import numpy as np

src = cv2.imread('idea.png')
rows, cols = src.shape[:2]

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 70, 1)
dst = cv2.warpAffine(src, M, (cols, rows))

cv2.imshow('idea.png', src)
cv2.imshow('Rotate', dst)
cv2.waitKey()
