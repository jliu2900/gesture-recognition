from my_app import handmodel, dollarRecognizer

# Start hand tracking and gesture recognition
hand_model = handmodel.HandModel(dollarRecognizer.on_coordinates_update)
hand_model.start_tracking()
