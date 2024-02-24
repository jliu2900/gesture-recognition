# How to import, resize, rotate an image
import cv2

img = cv2.imread('assets/hand.jpg', 1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('assets/new_img.jpg', img)  # write an image aka save a new img

cv2.imshow('Hand', img)
cv2.waitKey(0)  # waits x seconds, 0 is infinite
cv2.destroyAllWindows()



