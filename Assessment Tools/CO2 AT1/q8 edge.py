import cv2
import numpy as np
import os

os.makedirs("outputs", exist_ok=True)

image = cv2.imread("images/bricks.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: bricks.jpg not found!")
    exit()

sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

gradient = cv2.magnitude(
    sobelx.astype(np.float32),
    sobely.astype(np.float32)
)

laplacian = cv2.Laplacian(image, cv2.CV_64F)

sobel5 = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)
gradient = cv2.convertScaleAbs(gradient)
laplacian = cv2.convertScaleAbs(laplacian)
sobel5 = cv2.convertScaleAbs(sobel5)

cv2.imwrite("outputs/q8_sobelx.jpg", sobelx)
cv2.imwrite("outputs/q8_sobely.jpg", sobely)
cv2.imwrite("outputs/q8_gradient.jpg", gradient)
cv2.imwrite("outputs/q8_laplacian.jpg", laplacian)
cv2.imwrite("outputs/q8_sobel5.jpg", sobel5)

cv2.imshow("Original", image)
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)
cv2.imshow("Gradient Magnitude", gradient)
cv2.imshow("Laplacian", laplacian)
cv2.imshow("Sobel 5x5", sobel5)

cv2.waitKey(0)
cv2.destroyAllWindows()