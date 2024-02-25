import mediapipe as mp
import cv2
import numpy as np
import uuid
import os

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hand

cap = cv2.VideoCapture(0)
while cap.isOpened():
  ret, frame = cap.read()

  # Detection
  image = cv2.cvtColor(frame, cv2.COLOR_BGR2RBG)

  cv2.imshow('Hand tracking', frame)

  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()