import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

# Check if webcam is opened
if not cap.isOpened():
    print("Error: Cannot access webcam.")
    exit()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Cannot receive frame.")
        break

    # Display the webcam video
    cv2.imshow("Webcam Video", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
