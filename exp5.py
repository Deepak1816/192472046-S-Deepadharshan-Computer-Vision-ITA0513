import cv2
import numpy as np

img = cv2.imread("sample.jpg", 0)

edges = cv2.Canny(img, 100, 200)

kernel = np.ones((5,5), np.uint8)

eroded = cv2.erode(edges, kernel, iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()