import cv2
import os

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# Read document image in grayscale
image = cv2.imread(
    "images/document.jpg",
    cv2.IMREAD_GRAYSCALE
)

if image is None:
    print("Error: document.jpg not found!")
    exit()

# Apply slight Gaussian blur
blurred = cv2.GaussianBlur(image, (3, 3), 0)

# Apply Adaptive Gaussian Thresholding
binary = cv2.adaptiveThreshold(
    blurred,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

# Save outputs
cv2.imwrite("outputs/q8_grayscale.jpg", image)
cv2.imwrite("outputs/q8_threshold.jpg", binary)

# Display results
cv2.imshow("Original Document", image)
cv2.imshow("Adaptive Threshold Output", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()