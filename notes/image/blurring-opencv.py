import cv2
import os

img = cv2.imread(os.path.join('.', 'assets', 'zer_3_resized.jpg'))

k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
img_medianblur = cv2.medianBlur(img, k_size)

cv2.imshow('imagen', img)
cv2.imshow('blur', img_blur)
cv2.imshow('median blur', img_medianblur)
cv2.waitKey(0)
