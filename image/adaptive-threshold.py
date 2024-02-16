import cv2
import os

img = cv2.imread(os.path.join('.', 'assets', 'futbol_pibes.png'))
resized_img = cv2.resize(img, (683, 384))
cropped_img = resized_img[30:350, 0:683]

img_gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 6)

cv2.imshow('resized_img', resized_img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)