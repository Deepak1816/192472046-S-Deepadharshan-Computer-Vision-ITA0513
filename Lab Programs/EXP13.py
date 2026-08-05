import cv2
import numpy as np

# Read the video
cap = cv2.VideoCapture("sample.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Get frame size
    rows, cols = frame.shape[:2]

    # Source points
    pts1 = np.float32([
        [50, 50],
        [cols - 50, 50],
        [50, rows - 50],
        [cols - 50, rows - 50]
    ])

    # Destination points
    pts2 = np.float32([
        [0, 0],
        [cols, 0],
        [0, rows],
        [cols, rows]
    ])

    # Perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply perspective transformation
    result = cv2.warpPerspective(
        frame,
        matrix,
        (cols, rows)
    )

    # Display videos
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", result)

    # Press q to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
