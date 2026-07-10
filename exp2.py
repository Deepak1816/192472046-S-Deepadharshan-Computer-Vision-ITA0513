import cv2

img = cv2.imread("sample.jpg")

blur = cv2.GaussianBlur(img, (9, 9), 0)

cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()