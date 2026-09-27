from ultralytics import YOLO
import cv2
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# SMART TRAFFIC MONITORING SYSTEM
# IMPROVED MAIN PROGRAM
# ============================================================

print("\n")
print("======================================================")
print("        SMART TRAFFIC MONITORING SYSTEM")
print("======================================================")
print("Starting system...")
print("")


# ============================================================
# SETTINGS
# ============================================================

VIDEO_FILE = "traffic_video.mp4"
MODEL_FILE = "yolo11n.pt"
CSV_FILE = "traffic_flow_data.csv"

vehicle_classes = [
    "car",
    "motorcycle",
    "bus",
    "truck"
]


# ============================================================
# LOAD YOLO MODEL
# ============================================================

print("Loading YOLO model...")

model = YOLO(MODEL_FILE)

print("YOLO model loaded successfully!")


# ============================================================
# OPEN VIDEO
# ============================================================

cap = cv2.VideoCapture(VIDEO_FILE)

if not cap.isOpened():

    print("ERROR: Could not open traffic video.")

    exit()


print("Traffic video opened successfully!")
print("")
print("Starting vehicle detection...")
print("Press Q to stop the video.")
print("")


# ============================================================
# CSV FILE
# ============================================================

csv_file = open(
    CSV_FILE,
    "w",
    newline=""
)

csv_writer = csv.writer(csv_file)

csv_writer.writerow([
    "Time",
    "Cars",
    "Motorcycles",
    "Buses",
    "Trucks",
    "Total"
])


# ============================================================
# VARIABLES
# ============================================================

# IDs of vehicles already counted
counted_ids = set()

# Store previous Y position of each vehicle
previous_positions = {}

# Vehicle counts
car_count = 0
motorcycle_count = 0
bus_count = 0
truck_count = 0
total_count = 0

# Save CSV every second
last_save_time = time.time()


# ============================================================
# MAIN VIDEO LOOP
# ============================================================

while True:

    success, frame = cap.read()

    if not success:

        print("Video finished.")

        break


    # --------------------------------------------------------
    # FRAME INFORMATION
    # --------------------------------------------------------

    frame_height, frame_width = frame.shape[:2]

    # Horizontal counting line
    line_y = frame_height // 2


    # --------------------------------------------------------
    # YOLO TRACKING
    # --------------------------------------------------------

    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml"
    )


    # Draw counting line

    cv2.line(
        frame,
        (0, line_y),
        (frame_width, line_y),
        (0, 0, 255),
        3
    )


    # --------------------------------------------------------
    # PROCESS VEHICLES
    # --------------------------------------------------------

    for box in results[0].boxes:

        class_id = int(box.cls[0])

        class_name = model.names[class_id]


        # Ignore non-vehicle objects

        if class_name not in vehicle_classes:

            continue


        # Check tracking ID

        if box.id is None:

            continue


        track_id = int(box.id[0])


        # ----------------------------------------------------
        # BOUNDING BOX
        # ----------------------------------------------------

        x1, y1, x2, y2 = map(
            int,
            box.xyxy[0]
        )


        # Calculate center

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


        # Display vehicle and tracking ID

        cv2.putText(
            frame,
            f"{class_name} ID:{track_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )


        # ----------------------------------------------------
        # ACCURATE LINE CROSSING
        # ----------------------------------------------------

        if track_id in previous_positions:

            previous_y = previous_positions[track_id]


            # Vehicle was above the line
            # and is now below the line

            if (
                previous_y < line_y
                and center_y >= line_y
                and track_id not in counted_ids
            ):

                # Mark vehicle as counted

                counted_ids.add(track_id)

                total_count += 1


                # Count according to vehicle type

                if class_name == "car":

                    car_count += 1


                elif class_name == "motorcycle":

                    motorcycle_count += 1


                elif class_name == "bus":

                    bus_count += 1


                elif class_name == "truck":

                    truck_count += 1


        # Save current position
        # for the next frame

        previous_positions[track_id] = center_y


    # ========================================================
    # REMOVE OLD TRACKING IDs
    # ========================================================

    active_ids = set()

    for box in results[0].boxes:

        if box.id is not None:

            active_ids.add(
                int(box.id[0])
            )


    # Keep only active vehicle positions

    previous_positions = {

        track_id: position

        for track_id, position
        in previous_positions.items()

        if track_id in active_ids

    }


    # ========================================================
    # SAVE DATA EVERY SECOND
    # ========================================================

    current_time_seconds = time.time()


    if current_time_seconds - last_save_time >= 1:

        current_time = time.strftime(
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


    # ========================================================
    # TRAFFIC DENSITY
    # ========================================================

    if total_count <= 5:

        traffic_status = "LOW"


    elif total_count <= 15:

        traffic_status = "MEDIUM"


    else:

        traffic_status = "HIGH"


    # ========================================================
    # DISPLAY COUNTS
    # ========================================================

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
        (255, 255, 255, 255),
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


    cv2.putText(
        frame,
        f"DENSITY: {traffic_status}",
        (20, 210),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )


    # ========================================================
    # SHOW VIDEO
    # ========================================================

    cv2.imshow(
        "Smart Traffic Monitoring System",
        frame
    )


    # Press Q to stop

    if cv2.waitKey(1) & 0xFF == ord("q"):

        break


# ============================================================
# CLOSE VIDEO
# ============================================================

cap.release()

csv_file.close()

cv2.destroyAllWindows()


print("")
print("======================================================")
print("        VEHICLE DETECTION COMPLETED")
print("======================================================")

print("Cars Passed        :", car_count)
print("Motorcycles Passed :", motorcycle_count)
print("Buses Passed       :", bus_count)
print("Trucks Passed      :", truck_count)
print("Total Vehicles     :", total_count)

print("")


# ============================================================
# LOAD SAVED DATA
# ============================================================

df = pd.read_csv(CSV_FILE)


# ============================================================
# TRAFFIC STATISTICS
# ============================================================

if len(df) > 0:

    average_vehicles = df["Total"].mean()

    maximum_vehicles = df["Total"].max()

else:

    average_vehicles = 0

    maximum_vehicles = 0


# ============================================================
# VEHICLE PERCENTAGES
# ============================================================

if total_count > 0:

    car_percentage = (
        car_count / total_count
    ) * 100

    motorcycle_percentage = (
        motorcycle_count / total_count
    ) * 100

    bus_percentage = (
        bus_count / total_count
    ) * 100

    truck_percentage = (
        truck_count / total_count
    ) * 100

else:

    car_percentage = 0

    motorcycle_percentage = 0

    bus_percentage = 0

    truck_percentage = 0


# ============================================================
# MOST COMMON VEHICLE
# ============================================================

vehicle_counts = {

    "Cars": car_count,

    "Motorcycles": motorcycle_count,

    "Buses": bus_count,

    "Trucks": truck_count

}


most_common_vehicle = max(
    vehicle_counts,
    key=vehicle_counts.get
)


# ============================================================
# FINAL REPORT
# ============================================================

report = pd.DataFrame({

    "Metric": [

        "Cars Passed",
        "Motorcycles Passed",
        "Buses Passed",
        "Trucks Passed",

        "Total Vehicles Passed",

        "Average Vehicles",
        "Maximum Vehicles",

        "Cars Percentage",
        "Motorcycles Percentage",
        "Buses Percentage",
        "Trucks Percentage",

        "Most Common Vehicle",
        "Traffic Density"

    ],

    "Value": [

        car_count,
        motorcycle_count,
        bus_count,
        truck_count,

        total_count,

        round(
            average_vehicles,
            2
        ),

        maximum_vehicles,

        round(
            car_percentage,
            2
        ),

        round(
            motorcycle_percentage,
            2
        ),

        round(
            bus_percentage,
            2
        ),

        round(
            truck_percentage,
            2
        ),

        most_common_vehicle,

        traffic_status

    ]

})


# ============================================================
# SAVE FINAL REPORT
# ============================================================

report.to_csv(
    "complete_traffic_report.csv",
    index=False
)

# ============================================================
# TRAFFIC DENSITY FUNCTION
# ============================================================

def get_density(vehicle_count):

    if vehicle_count <= 5:
        return "LOW"

    elif vehicle_count <= 15:
        return "MEDIUM"

    else:
        return "HIGH"
    
# ============================================================
# CREATE TRAFFIC DENSITY REPORT
# ============================================================

density_order = [
    "LOW",
    "MEDIUM",
    "HIGH"
]

density_counts = (
    df["Total"]
    .apply(get_density)
    .value_counts()
    .reindex(
        density_order,
        fill_value=0
    )
)

density_report = pd.DataFrame({
    "Traffic Density": [
        "LOW",
        "MEDIUM",
        "HIGH"
    ],

    "Number of Records": [
        density_counts["LOW"],
        density_counts["MEDIUM"],
        density_counts["HIGH"]
    ]
})

density_report.to_csv(
    "traffic_density_report.csv",
    index=False
)

print("")
print("Traffic density report created successfully!")
print("File: traffic_density_report.csv")

# ============================================================
# DISPLAY REPORT
# ============================================================

print("")
print("======================================================")
print("             FINAL TRAFFIC REPORT")
print("======================================================")

print(
    report.to_string(
        index=False
    )
)


# ============================================================
# VEHICLE TYPE GRAPH
# ============================================================

plt.figure(
    figsize=(8, 5)
)

plt.bar(

    [
        "Cars",
        "Motorcycles",
        "Buses",
        "Trucks"
    ],

    [
        car_count,
        motorcycle_count,
        bus_count,
        truck_count
    ]

)

plt.title(
    "Vehicle Type Distribution"
)

plt.xlabel(
    "Vehicle Type"
)

plt.ylabel(
    "Vehicles Passed"
)

plt.grid(
    axis="y"
)

plt.tight_layout()

plt.show()


# ============================================================
# TRAFFIC FLOW GRAPH
# ============================================================

if len(df) > 0:

    plt.figure(
        figsize=(10, 5)
    )

    plt.plot(
        df["Time"],
        df["Total"],
        marker="o"
    )

    plt.title(
        "Traffic Flow Over Time"
    )

    plt.xlabel(
        "Time"
    )

    plt.ylabel(
        "Vehicles Passed"
    )

    plt.xticks(
        rotation=45
    )

    plt.grid(True)

    plt.tight_layout()

    plt.show()


# ============================================================
# COMPLETION MESSAGE
# ============================================================

print("")
print("======================================================")
print("       SMART TRAFFIC MONITORING COMPLETED")
print("======================================================")

print("")
print("Generated file:")
print("complete_traffic_report.csv")

print("")
print("Project execution completed successfully!")