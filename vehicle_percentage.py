import pandas as pd

# Read traffic flow data
df = pd.read_csv("traffic_flow_data.csv")

# Get final vehicle counts
cars = df["Cars"].iloc[-1]
motorcycles = df["Motorcycles"].iloc[-1]
buses = df["Buses"].iloc[-1]
trucks = df["Trucks"].iloc[-1]

# Calculate total vehicles
total = cars + motorcycles + buses + trucks

# Avoid division by zero
if total == 0:
    print("No vehicles detected.")
    exit()

# Calculate percentages
car_percentage = (cars / total) * 100
motorcycle_percentage = (motorcycles / total) * 100
bus_percentage = (buses / total) * 100
truck_percentage = (trucks / total) * 100

# Create report
report = pd.DataFrame({
    "Vehicle Type": [
        "Cars",
        "Motorcycles",
        "Buses",
        "Trucks"
    ],
    "Count": [
        cars,
        motorcycles,
        buses,
        trucks
    ],
    "Percentage": [
        round(car_percentage, 2),
        round(motorcycle_percentage, 2),
        round(bus_percentage, 2),
        round(truck_percentage, 2)
    ]
})

# Display report
print("\n==========================================")
print("       VEHICLE PERCENTAGE ANALYSIS")
print("==========================================")

print(report.to_string(index=False))

print("\nTotal Vehicles:", total)

print("\n==========================================")

# Save report
report.to_csv(
    "vehicle_percentage_report.csv",
    index=False
)

print("Percentage report saved successfully!")
print("File: vehicle_percentage_report.csv")

print("==========================================")