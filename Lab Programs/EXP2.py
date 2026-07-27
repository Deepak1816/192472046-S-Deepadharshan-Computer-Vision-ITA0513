import cv2

# Read the image
image = cv2.imread("sample.jpg")

# Blur the image
blur = cv2.GaussianBlur(image, (15, 15), 0)

# Display the original image
cv2.imshow("Original Image", image)

# Display the blurred image
cv2.imshow("Blurred Image", blur)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
