import cv2
import numpy as np

# Read the image
image = cv2.imread("sample.jpg")

# Get image height and width
rows, cols = image.shape[:2]

# Original points
pts1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

# Transformed points
pts2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

# Get affine transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
result = cv2.warpAffine(
    image,
    matrix,
    (cols, rows)
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
