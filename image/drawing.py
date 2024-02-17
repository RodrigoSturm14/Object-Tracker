import cv2
import os

img = cv2.imread(os.path.join('.', 'assets', 'zer_3_resized.jpg'))
print(img.shape)

# dibujar linea 
cv2.line(img, (200, 100), (400, 500), (100, 0, 0), 10)

# dibujar rectangulo
cv2.rectangle(img, (400, 350), (500, 500), (0, 150, 0), 4)

# dibujar circulo
cv2.circle(img, (450, 400), 25, (120, 0, 120), -1)

# dibujar texto
cv2.putText(img, ('Hola texto'), (600, 200), cv2.FONT_ITALIC, 2, (0, 0, 100), 4)

cv2.imshow('imagen', img)
cv2.waitKey(0)