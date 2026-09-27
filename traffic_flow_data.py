from ultralytics import YOLO
import cv2
import csv
import time
from datetime import datetime

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

# Open CSV file
csv_file = open(
    "traffic_flow_data.csv",
    "a",
    newline=""
)

csv_writer = csv.writer(csv_file)

# Write header if file is empty
if csv_file.tell() == 0:
    csv_writer.writerow([
        "Time",
        "Cars",
        "Motorcycles",
        "Buses",
        "Trucks",
        "Total"
    ])

# Store IDs of vehicles already counted
counted_ids = set()

# Vehicle counters
car_count = 0
motorcycle_count = 0
bus_count = 0
truck_count = 0
total_count = 0

# Save data once every second
last_save_time = time.time()

while True:

    success, frame = cap.read()

    # Stop when video ends
    if not success:
        print("Video finished")
        break

    # Get frame dimensions
    frame_height, frame_width = frame.shape[:2]

    # Virtual line
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

    # Process vehicles
    for box in results[0].boxes:

        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        # Ignore non-vehicles
        if class_name not in vehicle_classes:
            continue

        # Check tracking ID
        if box.id is None:
            continue

        track_id = int(box.id[0])

        # Bounding box
        x1, y1, x2, y2 = map(
            int,
            box.xyxy[0]
        )

        # Vehicle center
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        # Draw center
        cv2.circle(
            frame,
            (center_x, center_y),
            5,
            (0, 255, 255),
            -1
        )

        # Display vehicle ID
        cv2.putText(
            frame,
            f"{class_name} ID:{track_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        # Count vehicle crossing line
        if (
            center_y > line_y
            and track_id not in counted_ids
        ):

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

    # Save data once every second
    current_time_seconds = time.time()

    if current_time_seconds - last_save_time >= 1:

        current_time = datetime.now().strftime(
            "%H:%M:%S"
        )

        csv_writer.writerow([
            current_time,
            car_count,
            motorcycle_count,
            bus_count,
            truck_count,
            total_count
        ])

        csv_file.flush()

        last_save_time = current_time_seconds

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
        (255, 255, 255, 2)
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
        "Smart Traffic Flow Monitoring",
        frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
csv_file.close()
cv2.destroyAllWindows()

print("Traffic flow data saved to traffic_flow_data.csv")