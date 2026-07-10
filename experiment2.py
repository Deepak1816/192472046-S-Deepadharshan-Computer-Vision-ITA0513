import cv2

# Read the color image
img = cv2.imread("sample.jpg")

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale images
    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray)

    # Save the grayscale image (optional)
    cv2.imwrite("grayscale.jpg", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()