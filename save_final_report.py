import pandas as pd

# Read traffic flow data
df = pd.read_csv("traffic_flow_data.csv")


# Get final cumulative counts
final_cars = df["Cars"].iloc[-1]
final_motorcycles = df["Motorcycles"].iloc[-1]
final_buses = df["Buses"].iloc[-1]
final_trucks = df["Trucks"].iloc[-1]
final_total = df["Total"].iloc[-1]


# Calculate statistics
average_total = df["Total"].mean()
maximum_total = df["Total"].max()


# Find most common vehicle
vehicle_totals = {
    "Cars": final_cars,
    "Motorcycles": final_motorcycles,
    "Buses": final_buses,
    "Trucks": final_trucks
}

most_common_vehicle = max(
    vehicle_totals,
    key=vehicle_totals.get
)


# Traffic density function
def get_density(vehicle_count):

    if vehicle_count <= 5:
        return "LOW"

    elif vehicle_count <= 15:
        return "MEDIUM"

    else:
        return "HIGH"


# Add density column
df["Density"] = df["Total"].apply(get_density)


# Most common density
most_common_density = df["Density"].mode()[0]


# Create final report
report = pd.DataFrame({
    "Metric": [
        "Cars Passed",
        "Motorcycles Passed",
        "Buses Passed",
        "Trucks Passed",
        "Total Vehicles Passed",
        "Average Vehicles",
        "Maximum Vehicles",
        "Most Common Vehicle",
        "Most Common Traffic Density"
    ],

    "Value": [
        final_cars,
        final_motorcycles,
        final_buses,
        final_trucks,
        final_total,
        round(average_total, 2),
        maximum_total,
        most_common_vehicle,
        most_common_density
    ]
})


# Save report
report.to_csv(
    "final_traffic_report.csv",
    index=False
)


# Display report
print("\n==============================================")
print("       FINAL TRAFFIC REPORT")
print("==============================================")

print(report)

print("\n==============================================")
print("Report saved successfully!")
print("File: final_traffic_report.csv")
print("==============================================")