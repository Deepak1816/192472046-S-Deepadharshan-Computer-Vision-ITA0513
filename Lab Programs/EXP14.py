import cv2
import numpy as np

# Read the image
image = cv2.imread("sample.jpg")

# Get image height and width
rows, cols = image.shape[:2]

# Source points
pts1 = np.float32([
    [50, 50],
    [cols - 50, 50],
    [50, rows - 50],
    [cols - 50, rows - 50]
])

# Destination points
pts2 = np.float32([
    [20, 80],
    [cols - 20, 30],
    [70, rows - 30],
    [cols - 50, rows - 80]
])

# Calculate Homography Matrix
H, status = cv2.findHomography(pts1, pts2)

# Apply Homography Transformation
result = cv2.warpPerspective(
    image,
    H,
    (cols, rows)
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Homography Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
