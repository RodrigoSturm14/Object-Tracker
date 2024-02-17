import cv2
# leer webcam
webcam = cv2.VideoCapture(0)

#visualizar camara
while True:
  ret, frame = webcam.read()
  cv2.imshow('Camara Web', frame)

  if cv2.waitKey(40) & 0xFF == ord('q'):
    break

webcam.release()
cv2.destroyAllWindows()