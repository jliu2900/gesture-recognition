#  captures video input and display it
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # returns two things, boolean and the image itself
    # width = int(cap.get(3))  # x is the property number
    # height = int(cap.get(4))  # so 4 is height, look at doc
    #
    # image = np.zeros(frame.shape, np.uint8)
    # smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # image[:height//2, :width//2] = smaller_frame  # top left
    # image[height//2, :width//2] = smaller_frame  # bottom left
    # image[:height//2, width//2] = smaller_frame  # top right
    # image[height//2, width//2] = smaller_frame  # bottom right

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):  # waits x milliseconds, and returns the ascii key that we pressed
        break

cap.release()  # releases the resources
cv2.destroyAllWindows()
