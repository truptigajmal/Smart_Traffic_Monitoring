from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolo11n.pt")

# Vehicle classes
vehicle_classes = [
    "car",
    "motorcycle",
    "bus",
    "truck"
]

# Open traffic video
cap = cv2.VideoCapture("traffic_video.mp4")

if not cap.isOpened():
    print("Could not open traffic video")
    exit()

# Store IDs of vehicles already counted
counted_ids = set()

# Counters
car_count = 0
motorcycle_count = 0
bus_count = 0
truck_count = 0
total_count = 0

while True:

    success, frame = cap.read()

    # Stop when video ends
    if not success:
        print("Video finished")
        break

    # Get frame dimensions
    frame_height, frame_width = frame.shape[:2]

    # Create virtual line at the middle of the frame
    line_y = frame_height // 2

    # YOLO tracking
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml"
    )

    # Draw virtual line
    cv2.line(
        frame,
        (0, line_y),
        (frame_width, line_y),
        (0, 0, 255),
        3
    )

    # Process detected vehicles
    for box in results[0].boxes:

        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        # Ignore non-vehicles
        if class_name not in vehicle_classes:
            continue

        # Make sure tracking ID exists
        if box.id is None:
            continue

        track_id = int(box.id[0])

        # Get bounding box
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Calculate center of vehicle
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        # Draw center point
        cv2.circle(
            frame,
            (center_x, center_y),
            5,
            (0, 255, 255),
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

        # Count vehicle when it crosses the line
        if center_y > line_y and track_id not in counted_ids:

            counted_ids.add(track_id)

            total_count += 1

            if class_name == "car":
                car_count += 1

            elif class_name == "motorcycle":
                motorcycle_count += 1

            elif class_name == "bus":
                bus_count += 1

            elif class_name == "truck":
                truck_count += 1

    # Display counters
    cv2.putText(
        frame,
        f"Cars Passed: {car_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Motorcycles Passed: {motorcycle_count}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Buses Passed: {bus_count}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Trucks Passed: {truck_count}",
        (20, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"TOTAL PASSED: {total_count}",
        (20, 170),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    # Show video
    cv2.imshow(
        "Smart Traffic Line Counter",
        frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()