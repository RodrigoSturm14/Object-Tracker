import cv2
import os

img = cv2.imread(os.path.join('.', 'assets', 'zer_3_resized.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

thresh = cv2.blur(thresh, (7, 7))

ret, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('imagen', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)