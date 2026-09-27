from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolo11n.pt")

# Vehicle classes
vehicle_classes = ["car", "motorcycle", "bus", "truck"]

# Open webcam
cap = cv2.VideoCapture(0)

# Get webcam dimensions
ret, frame = cap.read()

if not ret:
    print("Could not open webcam")
    cap.release()
    exit()

height, width = frame.shape[:2]

# Horizontal counting line
line_y = height // 2

# Store IDs of vehicles already counted
counted_ids = set()

# Total vehicle count
total_count = 0

while True:

    success, frame = cap.read()

    if not success:
        print("Could not read webcam")
        break

    # YOLO tracking
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml"
    )

    # Draw counting line
    cv2.line(
        frame,
        (0, line_y),
        (width, line_y),
        (0, 0, 255),
        3
    )

    # Process detections
    for box in results[0].boxes:

        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        # Only vehicles
        if class_name not in vehicle_classes:
            continue

        # Tracking ID
        if box.id is None:
            continue

        track_id = int(box.id[0])

        # Bounding box
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Center of vehicle
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        # Draw bounding box
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        # Draw center point
        cv2.circle(
            frame,
            (center_x, center_y),
            5,
            (255, 0, 0),
            -1
        )

        # Display vehicle name and ID
        cv2.putText(
            frame,
            f"{class_name} ID:{track_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        # Check whether vehicle crossed the line
        if center_y > line_y and track_id not in counted_ids:

            counted_ids.add(track_id)
            total_count += 1

    # Display total count
    cv2.putText(
        frame,
        f"Vehicles Passed: {total_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 255),
        2
    )

    # Display instructions
    cv2.putText(
        frame,
        "Vehicle must cross the red line",
        (20, height - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # Show frame
    cv2.imshow(
        "Vehicle Flow Counting",
        frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()