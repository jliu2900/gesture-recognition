import mediapipe as mp
import numpy as np
import cv2

class HandModel:
  def __init__(self, callback_fn):
    self.mp_hands = mp.solutions.hands.Hands()
    self.image = cv2.VideoCapture(0)
    self.callback_fn = callback_fn  # Store the callback function

  def get_fingertip_coordinates(self):
    _, image = self.image.read() 

    print(image)
    print(type(image))

    if image is None:
      return None
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = self.mp_hands.process(image)

    # Combined coordinates
    coordinates = []

    # Extract fingertip coordinates from each detected hand
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        # Extract index fingertip
        fingertip_x = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].x
        fingertip_y = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y
        coordinates.append((fingertip_x, fingertip_y))  # Append as tuple

    # Call the callback function with the extracted coordinates
    if self.callback_fn:
      self.callback_fn(coordinates)

    # return the coordinates    
    return coordinates 
  
  def start_tracking(self):
    # Continuously captures frames, extracts coordinates, and calls the callback.
    while True: 
      coordinates = self.get_fingertip_coordinates()
      if cv2.waitKey(1) == ord('q'):
        break
    
    # Release resources
    self.image.release()
    cv2.destroyAllWindows()