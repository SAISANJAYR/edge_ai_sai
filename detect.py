
import cv2
from ultralytics import YOLO
import time

# Load your trained model
model = YOLO("best.pt")

# Open webcam (change index if required)
cap = cv2.VideoCapture(0)

# Camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Webcam not detected!")
    exit()

print("Enclosure detection started. Press Q to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    start = time.time()

    # YOLO inference
    results = model.predict(
        frame,
        imgsz=640,
        conf=0.40,
        verbose=False
    )

    # Draw bounding boxes and labels
    annotated_frame = results[0].plot()

    # Calculate FPS
    fps = 1 / max(time.time() - start, 1e-6)

    cv2.putText(
        annotated_frame,
        f"FPS: {fps:.1f}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow("Enclosure Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
