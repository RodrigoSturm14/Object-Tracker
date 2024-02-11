import cv2
import os

# leer imagen
img = cv2.imread(os.path.join('.', 'assets', 'zer_3.jpg'))
# ver alto, ancho y canales de la imagen, en ese orden
print(img.shape) 

# cambiar ancho y alto de la imagen
resized_img = cv2.resize(img, (1040, 586))
print(resized_img.shape)

# recortar imagen en intervalos, [alto, ancho] --> [(y:y),(x:x)] --> desde y hasta y, desde x hasta x
cropped_img = resized_img[20:550, 200:780]

#  ---- visualizar imagen ----
# cv2.imshow('imagen', img)
cv2.imshow('imagen modificada', resized_img)
cv2.imshow('imagen recortada', cropped_img)
# cv2 mantiene la ventana abierta indefinidamente hasta q se presione una tecla
cv2.waitKey(0)