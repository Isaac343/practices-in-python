import cv2
import numpy as np

src = cv2.imread('idea.png')

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(src, M, (512 + 100,  512 + 50))

cv2.imshow('idea.png', src)
cv2.imshow('Traslate', dst)
cv2.waitKey()
