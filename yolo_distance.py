import cv2
from ultralytics import YOLO
from distance_calculator import DistanceCalculator
import config

# Load the YOLOv8 model
model = YOLO('yolov8s-seg.pt')  # or your custom trained model

# Initialize distance calculator with known object dimensions
distance_calculator = DistanceCalculator(
    known_width_person = known_width_monitor = 0.4   # Average widthof specified classes in meters 
)

cctv_url = config.CCTV_URL

# Open the video capture
cap = cv2.VideoCapture(cctv_url)

if not cap.isOpened():
    print("Error opening video stream or file")
    exit()

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference on the frame
    results = model(frame)

    # Visualize and calculate distances
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            if class_id == 0:  # Person
                distance = distance_calculator.calculate_distance_class(box)
                label = f"Person {distance:.2f}m"
            elif class_id == 62:  # Monitor
                distance = distance_calculator.calculate_distance_class(box)
                label = f"Monitor {distance:.2f}m"
            else:
                continue

            # Extract box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('YOLOv8 Inference', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
