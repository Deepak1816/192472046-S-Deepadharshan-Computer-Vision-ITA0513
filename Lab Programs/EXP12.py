import cv2
import numpy as np

# Read the image
image = cv2.imread("sample.jpg")

# Get image height and width
rows, cols = image.shape[:2]

# Four points from original image
pts1 = np.float32([
    [50, 50],
    [cols - 50, 50],
    [50, rows - 50],
    [cols - 50, rows - 50]
])

# Four corresponding output points
pts2 = np.float32([
    [0, 0],
    [cols, 0],
    [0, rows],
    [cols, rows]
])

# Get perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
result = cv2.warpPerspective(
    image,
    matrix,
    (cols, rows)
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
