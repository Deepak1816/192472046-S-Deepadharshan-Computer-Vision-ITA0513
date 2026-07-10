import cv2

img = cv2.imread("sample.jpg")

if img is None:
    print("Error: Image not found!")
else:
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()