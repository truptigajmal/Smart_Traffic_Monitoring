from ultralytics import YOLO
import cv2
import csv
from datetime import datetime
import time

# Load YOLO model
model = YOLO("yolo11n.pt")

# Vehicle classes
vehicle_classes = ["car", "motorcycle", "bus", "truck"]

# Open CSV file
csv_file = open("traffic_data.csv", "a", newline="")
csv_writer = csv.writer(csv_file)

# Write header if file is empty
if csv_file.tell() == 0:
    csv_writer.writerow([
        "Time",
        "Cars",
        "Motorcycles",
        "Buses",
        "Trucks",
        "Total",
        "Traffic"
    ])

# Open webcam
cap = cv2.VideoCapture(0)

# Time of last CSV save
last_save_time = time.time()

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

    # Vehicle counters
    car_count = 0
    motorcycle_count = 0
    bus_count = 0
    truck_count = 0

    # Process detected objects
    for box in results[0].boxes:

        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        # Only process vehicles
        if class_name not in vehicle_classes:
            continue

        # Count vehicles
        if class_name == "car":
            car_count += 1

        elif class_name == "motorcycle":
            motorcycle_count += 1

        elif class_name == "bus":
            bus_count += 1

        elif class_name == "truck":
            truck_count += 1

        # Get tracking ID
        if box.id is not None:
            track_id = int(box.id[0])
        else:
            track_id = 0

        # Draw bounding box
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"{class_name} ID:{track_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    # Total vehicles
    total_count = (
        car_count
        + motorcycle_count
        + bus_count
        + truck_count
    )

    # Traffic density
    if total_count <= 5:
        traffic_status = "LOW"

    elif total_count <= 15:
        traffic_status = "MEDIUM"

    else:
        traffic_status = "HIGH"

    # Display vehicle counts
    cv2.putText(
        frame,
        f"Cars: {car_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Motorcycles: {motorcycle_count}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Buses: {bus_count}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Trucks: {truck_count}",
        (20, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Total Vehicles: {total_count}",
        (20, 170),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Traffic: {traffic_status}",
        (20, 210),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    # Save data once every second
    current_time_seconds = time.time()

    if current_time_seconds - last_save_time >= 1:

        current_time = datetime.now().strftime("%H:%M:%S")

        csv_writer.writerow([
            current_time,
            car_count,
            motorcycle_count,
            bus_count,
            truck_count,
            total_count,
            traffic_status
        ])

        csv_file.flush()

        last_save_time = current_time_seconds

    # Show webcam
    cv2.imshow(
        "Smart Traffic Monitoring System",
        frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
csv_file.close()
cv2.destroyAllWindows()