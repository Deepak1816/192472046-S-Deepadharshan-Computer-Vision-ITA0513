import cv2
import numpy as np

image = cv2.imread("sample.jpg")

height, width = image.shape[:2]

# Move 100 pixels right and 50 pixels down
matrix = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])

moved = cv2.warpAffine(image, matrix, (width, height))

cv2.imshow("Original Image", image)
cv2.imshow("Moved Image", moved)

cv2.waitKey(0)
cv2.destroyAllWindows()
