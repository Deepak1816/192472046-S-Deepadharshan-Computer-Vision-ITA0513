import cv2
import numpy as np
import os

os.makedirs("outputs", exist_ok=True)

image = cv2.imread("images/cameraman.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: cameraman.jpg not found!")
    exit()

fft = np.fft.fft2(image)
fft_shift = np.fft.fftshift(fft)

magnitude = np.log(np.abs(fft_shift)+1)

rows, cols = image.shape
crow, ccol = rows//2, cols//2

mask = np.zeros((rows, cols), np.uint8)
cv2.circle(mask, (ccol, crow), 40, 1, -1)

filtered = fft_shift * mask

inverse = np.fft.ifft2(np.fft.ifftshift(filtered))
inverse = np.abs(inverse)

inverse = cv2.normalize(inverse,None,0,255,cv2.NORM_MINMAX).astype(np.uint8)
spectrum = cv2.normalize(magnitude,None,0,255,cv2.NORM_MINMAX).astype(np.uint8)

cv2.imwrite("outputs/q6_fft_spectrum.jpg", spectrum)
cv2.imwrite("outputs/q6_filtered.jpg", inverse)

cv2.imshow("Original", image)
cv2.imshow("FFT Spectrum", spectrum)
cv2.imshow("Filtered Image", inverse)

cv2.waitKey(0)
cv2.destroyAllWindows()