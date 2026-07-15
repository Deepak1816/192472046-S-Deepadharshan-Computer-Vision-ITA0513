import cv2

# Read the video file
cap = cv2.VideoCapture("sample.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert each frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display original and processed video
    cv2.imshow("Original Video", frame)
    cv2.imshow("Grayscale Video", gray)

    # Press 'q' to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
