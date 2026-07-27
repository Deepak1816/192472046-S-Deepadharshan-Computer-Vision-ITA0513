import cv2

image = cv2.imread("sample.jpg")

# Rotate clockwise
clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Rotate counter-clockwise
counter_clockwise = cv2.rotate(
    image,
    cv2.ROTATE_90_COUNTERCLOCKWISE
)

cv2.imshow("Original Image", image)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter_clockwise)

cv2.waitKey(0)
cv2.destroyAllWindows()
