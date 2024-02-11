import cv2
import os

# leer imagen
img_path = os.path.join('.', 'data', 'zer_3.jpg')

img = cv2.imread(img_path)

# guardar imagen
cv2.imwrite(os.path.join('.', 'data', 'zer_3_out.jpg'), img)

# visualizar imagen
cv2.imshow('zer_3.jpg', img)
# cv2 mantiene la ventana abierta indefinidamente hasta q se presione una tecla
cv2.waitKey(0)