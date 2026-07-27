import cv2

image = cv2.imread("sample.jpg")

# Bigger image
bigger = cv2.resize(image, None, fx=1.5, fy=1.5)

# Smaller image
smaller = cv2.resize(image, None, fx=0.5, fy=0.5)

cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()
