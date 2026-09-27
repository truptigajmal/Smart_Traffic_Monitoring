from ultralytics import YOLO
import cv2
import csv
import time
from datetime import datetime

# ==========================================
# 1. LOAD YOLO MODEL
# ==========================================

model = YOLO("yolo11n.pt")

# Vehicle classes
vehicle_classes = [
    "car",
    "motorcycle",
    "bus",
    "truck"
]

# ==========================================
# 2. OPEN CSV FILE
# ==========================================

csv_file = open(
    "vehicle_flow_data.csv",
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

# ==========================================
# 3. OPEN WEBCAM
# ==========================================

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if not ret:
    print("Could not open webcam")
    cap.release()
    csv_file.close()
    exit()

# Get frame dimensions
height, width = frame.shape[:2]

# ==========================================
# 4. COUNTING LINE
# ==========================================

line_y = height // 2

# IDs already counted
counted_ids = set()

# ==========================================
# 5. VEHICLE COUNTERS
# ==========================================

car_count = 0
motorcycle_count = 0
bus_count = 0
truck_count = 0

# Time of last CSV save
last_save_time = time.time()

# ==========================================
# 6. MAIN LOOP
# ==========================================

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

    # ======================================
    # DRAW COUNTING LINE
    # ======================================

    cv2.line(
        frame,
        (0, line_y),
        (width, line_y),
        (0, 0, 255),
        3
    )

    # ======================================
    # PROCESS VEHICLES
    # ======================================

    for box in results[0].boxes:

        class_id = int(box.cls[0])

        class_name = model.names[class_id]

        # Ignore non-vehicle objects
        if class_name not in vehicle_classes:
            continue

        # Get tracking ID
        if box.id is None:
            continue

        track_id = int(box.id[0])

        # Get bounding box
        x1, y1, x2, y2 = map(
            int,
            box.xyxy[0]
        )

        # Calculate center point
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        # ==================================
        # DRAW BOUNDING BOX
        # ==================================

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

        # Display vehicle type and ID
        cv2.putText(
            frame,
            f"{class_name} ID:{track_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        # ==================================
        # CHECK LINE CROSSING
        # ==================================

        if (
            center_y > line_y
            and track_id not in counted_ids
        ):

            # Remember this vehicle
            counted_ids.add(track_id)

            # Increase appropriate counter
            if class_name == "car":

                car_count += 1

            elif class_name == "motorcycle":

                motorcycle_count += 1

            elif class_name == "bus":

                bus_count += 1

            elif class_name == "truck":

                truck_count += 1

    # ======================================
    # TOTAL VEHICLES
    # ======================================

    total_count = (
        car_count
        + motorcycle_count
        + bus_count
        + truck_count
    )

    # ======================================
    # DISPLAY COUNTERS
    # ======================================

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
        f"Total Passed: {total_count}",
        (20, 170),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    # ======================================
    # INSTRUCTIONS
    # ======================================

    cv2.putText(
        frame,
        "Cross the red line to be counted",
        (20, height - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # ======================================
    # SAVE DATA EVERY SECOND
    # ======================================

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

        # Save immediately
        csv_file.flush()

        last_save_time = current_time_seconds

    # ======================================
    # SHOW VIDEO
    # ======================================

    cv2.imshow(
        "Vehicle Type Flow Counting",
        frame
    )

    # ======================================
    # PRESS Q TO EXIT
    # ======================================

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ==========================================
# 7. RELEASE RESOURCES
# ==========================================

cap.release()

csv_file.close()

cv2.destroyAllWindows()

print("\nVehicle flow data saved to:")
print("vehicle_flow_data.csv")