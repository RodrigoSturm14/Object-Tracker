import cv2
import os
import numpy as np

img = cv2.imread(os.path.join('.', 'assets', 'zer_3_resized.jpg'))
# img = cv2.imread(os.path.join('.', 'assets', 'futbol_pibes.png'))
#vresized_img = cv2.resize(img, (683, 384))
# cropped_img = resized_img[30:350, 0:683]
# img_edge = cv2.Canny(img, 50, 100)

# detectar contorno del objeto, los numeros son limites
img_edge = cv2.Canny(img, 100, 500)
# dilatar el contorno --> los hace mas gruesos
img_edge_d = cv2.dilate(img_edge, np.ones((2, 2), dtype=np.int8))
# erosionar contorno --> los hace mas finos
img_edge_e = cv2.erode(img_edge, np.ones((1, 1), dtype=np.int8))

cv2.imshow('img', img)
# cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)
cv2.waitKey(0)
