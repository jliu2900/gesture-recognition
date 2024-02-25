from dollarpy import Recognizer, Point
from my_app.handmodel import HandModel

# Define the callback function to receive coordinates
def on_coordinates_update(coordinates):
  # Create point objects from the received coordinates
  data_points = []
  for x, y in coordinates:
    data_points.append(Point(x, y))
  
  # Perform the gesture recognition
  recognizer = Recognizer(None)
  result = recognizer.recognize(data_points)
  
  # Print or use the recognition result
  print("Recognized gesture", result)

# Create an instance of HandModel, passing the callback function
hand_model = HandModel(on_coordinates_update)

# Start the hand tracking loop
while True:
  hand_model.get_fingertip_coordinates()  # Trigger coordinate updates



