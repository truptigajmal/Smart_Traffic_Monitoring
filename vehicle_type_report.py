import pandas as pd

# Read traffic flow data
df = pd.read_csv("traffic_flow_data.csv")

# Get final cumulative counts
cars = df["Cars"].iloc[-1]
motorcycles = df["Motorcycles"].iloc[-1]
buses = df["Buses"].iloc[-1]
trucks = df["Trucks"].iloc[-1]

total = cars + motorcycles + buses + trucks

# Create vehicle type report
report = pd.DataFrame({
    "Vehicle Type": [
        "Cars",
        "Motorcycles",
        "Buses",
        "Trucks",
        "Total"
    ],
    "Vehicles Passed": [
        cars,
        motorcycles,
        buses,
        trucks,
        total
    ]
})

# Display report
print("\n==========================================")
print("        VEHICLE TYPE REPORT")
print("==========================================")

print(report)

print("\n==========================================")

# Save report
report.to_csv(
    "vehicle_type_report.csv",
    index=False
)

print("Vehicle type report saved successfully!")
print("File: vehicle_type_report.csv")

print("==========================================")