import cv2

# Read image
image = cv2.imread("sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create ORB detector
orb = cv2.ORB_create()

# Detect keypoints and descriptors
keypoints, descriptors = orb.detectAndCompute(
    gray,
    None
)

# Draw detected keypoints
result = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("ORB Feature Detection", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
