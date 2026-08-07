import cv2

# Load Haar Cascade XML
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

# Read image
image = cv2.imread("sample1.jpg")

if image is None:
    print("Error: sample1.jpg not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect eyes
eyes = eye_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(20,20)
)

# Draw rectangles
for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255,0,0), 2)

# Display
cv2.imshow("Eye Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
