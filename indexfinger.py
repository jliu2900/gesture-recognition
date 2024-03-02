import mediapipe as mp
import cv2
import numpy as np
from mediapipe.framework.formats import landmark_pb2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    ret, frame = cap.read()

    # BGR 2 RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Set flag
    image.flags.writeable = False

    # Detection
    results = hands.process(image)

    # Set flag to true
    image.flags.writeable = True

    # RGB 2 BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    landmarks_coord = []
    # Rendering results
    if results.multi_hand_landmarks:
      image_height, image_width, _ = image.shape

      # red dot styles
      dot_coordinates = [250, 250]
      dot_color = (0, 0, 255)
      dot_radius = 8

      for landmarks in results.multi_hand_landmarks:
        index_finger_landmark = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
        fingertip_x = int(index_finger_landmark.x * image_width)
        fingertip_y = int(index_finger_landmark.y * image_height)
        cv2.circle(image, (fingertip_x, fingertip_y), dot_radius, dot_color, -1)

      #   landmarks.append(index_finger_landmark)
      #   print('Index Fingertip Coordinate:', fingertip_x, fingertip_y)
      mp_drawing.draw_landmarks(image, landmarks, None, landmark_drawing_spec=draw.DrawingSpec(color=(0, 255, 255), circle_radius=1))
        
    cv2.imshow('Hand tracking', image)

    if cv2.waitKey(1) == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()