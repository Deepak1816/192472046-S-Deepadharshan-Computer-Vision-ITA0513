import cv2
import numpy as np

# Read image
image = cv2.imread("sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to float32
gray = np.float32(gray)

# Harris Corner Detection
corners = cv2.cornerHarris(
    gray,
    blockSize=2,
    ksize=3,
    k=0.04
)

# Dilate corners
corners = cv2.dilate(corners, None)

# Mark detected corners
result = image.copy()
result[corners > 0.01 * corners.max()] = [0, 0, 255]

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Harris Corner Detection", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
