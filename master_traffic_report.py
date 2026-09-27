import pandas as pd

# Read traffic flow data
df = pd.read_csv("traffic_flow_data.csv")


# -------------------------------
# VEHICLE COUNTS
# -------------------------------

cars = df["Cars"].iloc[-1]
motorcycles = df["Motorcycles"].iloc[-1]
buses = df["Buses"].iloc[-1]
trucks = df["Trucks"].iloc[-1]

total_vehicles = cars + motorcycles + buses + trucks


# -------------------------------
# TRAFFIC STATISTICS
# -------------------------------

average_vehicles = df["Total"].mean()
maximum_vehicles = df["Total"].max()


# -------------------------------
# VEHICLE PERCENTAGES
# -------------------------------

car_percentage = (cars / total_vehicles) * 100
motorcycle_percentage = (motorcycles / total_vehicles) * 100
bus_percentage = (buses / total_vehicles) * 100
truck_percentage = (trucks / total_vehicles) * 100


# -------------------------------
# TRAFFIC DENSITY
# -------------------------------

def get_density(vehicle_count):

    if vehicle_count <= 5:
        return "LOW"

    elif vehicle_count <= 15:
        return "MEDIUM"

    else:
        return "HIGH"


df["Density"] = df["Total"].apply(get_density)

most_common_density = df["Density"].mode()[0]


# -------------------------------
# MOST COMMON VEHICLE
# -------------------------------

vehicle_counts = {
    "Cars": cars,
    "Motorcycles": motorcycles,
    "Buses": buses,
    "Trucks": trucks
}

most_common_vehicle = max(
    vehicle_counts,
    key=vehicle_counts.get
)


# -------------------------------
# CREATE MASTER REPORT
# -------------------------------

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
        "Most Common Traffic Density"
    ],

    "Value": [

        cars,
        motorcycles,
        buses,
        trucks,

        total_vehicles,

        round(average_vehicles, 2),
        maximum_vehicles,

        round(car_percentage, 2),
        round(motorcycle_percentage, 2),
        round(bus_percentage, 2),
        round(truck_percentage, 2),

        most_common_vehicle,
        most_common_density
    ]
})


# -------------------------------
# DISPLAY REPORT
# -------------------------------

print("\n")
print("================================================")
print("          SMART TRAFFIC MONITORING")
print("              MASTER REPORT")
print("================================================")

print(report.to_string(index=False))

print("\n================================================")


# -------------------------------
# SAVE REPORT
# -------------------------------

report.to_csv(
    "master_traffic_report.csv",
    index=False
)

print("Master report saved successfully!")

print("File: master_traffic_report.csv")

print("================================================")