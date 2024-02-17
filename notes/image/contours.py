import cv2
import os

img = cv2.imread(os.path.join('.', 'assets', 'birds.jpg'))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 1 aplicar threshold global invertido
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

# contours guarda un tuple de las coordenadas de las secciones blancas
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# iterar para cada una de los contornos
for cnt in contours:
  # limitar las areas blancas q se van a iterar
  if cv2.contourArea(cnt) > 100:
    # cv2.drawContours(img, cnt, -1, (200, 0, 0), 2)

    x1, y1, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (200, 0, 0), 2)

cv2.imshow('imagen', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)