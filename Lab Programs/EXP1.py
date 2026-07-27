import cv2

# Read the image
image = cv2.imread("sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original image
cv2.imshow("Original Image", image)

# Display the grayscale image
cv2.imshow("Grayscale Image", gray)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
