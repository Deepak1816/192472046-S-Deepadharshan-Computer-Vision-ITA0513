import cv2
import matplotlib.pyplot as plt
import os

# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Read image
image = cv2.imread("images/histogram.jpg")

if image is None:
    print("Error: histogram.jpg not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Global Histogram Equalization
global_eq = cv2.equalizeHist(gray)

# CLAHE
clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8,8))
clahe_img = clahe.apply(gray)

# Save images
cv2.imwrite("outputs/q2_original.jpg", gray)
cv2.imwrite("outputs/q2_global.jpg", global_eq)
cv2.imwrite("outputs/q2_clahe.jpg", clahe_img)

# Display
cv2.imshow("Original", gray)
cv2.imshow("Global Histogram Equalization", global_eq)
cv2.imshow("CLAHE", clahe_img)

# Histogram
plt.figure(figsize=(8,5))
plt.hist(gray.ravel(),256,[0,256],label="Original")
plt.hist(global_eq.ravel(),256,[0,256],label="Global")
plt.hist(clahe_img.ravel(),256,[0,256],label="CLAHE")
plt.title("Histogram Comparison")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()

plt.savefig("outputs/q2_histogram.jpg")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()