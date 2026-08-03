import cv2
import numpy as np
import os

os.makedirs("outputs", exist_ok=True)

image = cv2.imread("images/lena.jpg")

if image is None:
    print("Error: lena.jpg not found!")
    exit()

noisy = image.copy()

probability = 0.15

random = np.random.rand(image.shape[0], image.shape[1])

noisy[random < probability/2] = 0
noisy[random > 1-probability/2] = 255

gaussian = cv2.GaussianBlur(noisy,(3,3),0)
median = cv2.medianBlur(noisy,3)

cv2.imwrite("outputs/q5_noise.jpg", noisy)
cv2.imwrite("outputs/q5_gaussian.jpg", gaussian)
cv2.imwrite("outputs/q5_median.jpg", median)

cv2.imshow("Original", image)
cv2.imshow("Salt & Pepper Noise", noisy)
cv2.imshow("Gaussian Filter", gaussian)
cv2.imshow("Median Filter", median)

cv2.waitKey(0)
cv2.destroyAllWindows()