import cv2
import os

img = cv2.imread(os.path.join('.', 'assets', 'zer_3.jpg'))
resized_img = cv2.resize(img, (1040, 586))

img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
print(img_gray.shape)

cv2.imshow('imagen bgr', resized_img)
cv2.imshow('imagen gray', img_gray)
cv2.waitKey(0)