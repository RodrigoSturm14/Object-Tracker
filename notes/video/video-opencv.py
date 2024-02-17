import cv2
import os
# leer video
video_path = os.path.join('.', 'data', 'Twitter-Follow-Card-react.mp4')
video = cv2.VideoCapture(video_path)

# visualizar video
ret = True
while ret:
  ret, frame = video.read()

  if ret:
    cv2.imshow('video', frame)
    cv2.waitKey(33)

video.release()
cv2.destroyAllWindows()