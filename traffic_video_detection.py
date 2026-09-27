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

while True:

    success, frame = cap.read()

    # Stop when video ends
    if not success:
        print("Video finished")
        break

    # YOLO detection
    results = model(frame)

    # Vehicle counters
    car_count = 0
    motorcycle_count = 0
    bus_count = 0
    truck_count = 0

    # Process detected objects
    for box in results[0].boxes:

        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        # Ignore non-vehicles
        if class_name not in vehicle_classes:
            continue

        if class_name == "car":
            car_count += 1

        elif class_name == "motorcycle":
            motorcycle_count += 1

        elif class_name == "bus":
            bus_count += 1

        elif class_name == "truck":
            truck_count += 1

    # Total vehicles
    total_count = (
        car_count
        + motorcycle_count
        + bus_count
        + truck_count
    )

    # Draw YOLO detections
    annotated_frame = results[0].plot()

    # Display car count
    cv2.putText(
        annotated_frame,
        f"Cars: {car_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # Display motorcycle count
    cv2.putText(
        annotated_frame,
        f"Motorcycles: {motorcycle_count}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # Display bus count
    cv2.putText(
        annotated_frame,
        f"Buses: {bus_count}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # Display truck count
    cv2.putText(
        annotated_frame,
        f"Trucks: {truck_count}",
        (20, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # Display total count
    cv2.putText(
        annotated_frame,
        f"Total Vehicles: {total_count}",
        (20, 170),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    # Show video
    cv2.imshow(
        "Smart Traffic Video Detection",
        annotated_frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()