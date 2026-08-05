import cv2

# Read image
image = cv2.imread("sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and descriptors
keypoints, descriptors = sift.detectAndCompute(
    gray,
    None
)

# Draw keypoints
result = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("SIFT Feature Detection", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
