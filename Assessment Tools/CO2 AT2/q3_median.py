import cv2
import numpy as np
import os

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Read MRI image
image = cv2.imread("images/mri.jpg")

if image is None:
    print("Error: mri.jpg not found!")
    exit()

# Create a copy for adding noise
noisy = image.copy()

# Add Salt and Pepper noise
noise_percentage = 0.10

random_values = np.random.rand(
    image.shape[0],
    image.shape[1]
)

# Pepper noise - black pixels
noisy[random_values < noise_percentage / 2] = 0

# Salt noise - white pixels
noisy[random_values > 1 - noise_percentage / 2] = 255

# Apply 5x5 Median Filter
filtered = cv2.medianBlur(noisy, 5)

# Save outputs
cv2.imwrite("outputs/q3_noisy.jpg", noisy)
cv2.imwrite("outputs/q3_filtered.jpg", filtered)

# Display images
cv2.imshow("Original MRI", image)
cv2.imshow("MRI with Salt and Pepper Noise", noisy)
cv2.imshow("Median Filtered MRI", filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()