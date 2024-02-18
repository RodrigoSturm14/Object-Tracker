import cv2
from getHSVcolor import get_limits
from PIL import Image

BGR_BLUE = [255, 0, 0]
lowerLimit, upperLimit = get_limits(color=BGR_BLUE)

webcam = cv2.VideoCapture(0)

while True:
  ret, frame = webcam.read()
  # pasar frame a hsv
  hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  # crear mascara con los limites del color elegido
  # inRange aplica un threshold a la imagen con los limites del color
  mask = cv2.inRange(hsvFrame, lowerLimit, upperLimit)
  # pasar a otro formato
  maskPIL = Image.fromarray(mask)
  # obtener limites del area blanca
  bbox = maskPIL.getbbox()

  if bbox is not None:
    x1, y1, x2, y2 = bbox
    # dibujar rectangulo con coordenadas 
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)

  cv2.imshow('camara', frame)

  if cv2.waitKey(40) & 0xFF == ord('q'):
    break

webcam.release()
cv2.destroyAllWindows()
