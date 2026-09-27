import pandas as pd
import matplotlib.pyplot as plt

# Read traffic data
df = pd.read_csv("traffic_flow_data.csv")

# Get final vehicle counts
cars = df["Cars"].iloc[-1]
motorcycles = df["Motorcycles"].iloc[-1]
buses = df["Buses"].iloc[-1]
trucks = df["Trucks"].iloc[-1]

total = cars + motorcycles + buses + trucks

# Calculate average and maximum traffic
average_vehicles = df["Total"].mean()
maximum_vehicles = df["Total"].max()

# Vehicle data
vehicle_types = [
    "Cars",
    "Motorcycles",
    "Buses",
    "Trucks"
]

vehicle_counts = [
    cars,
    motorcycles,
    buses,
    trucks
]

# Density calculation
def get_density(vehicle_count):

    if vehicle_count <= 5:
        return "LOW"

    elif vehicle_count <= 15:
        return "MEDIUM"

    else:
        return "HIGH"


df["Density"] = df["Total"].apply(get_density)

most_common_density = df["Density"].mode()[0]

# Print dashboard summary
print("\n")
print("====================================================")
print("             SMART TRAFFIC DASHBOARD")
print("====================================================")

print("\nTRAFFIC SUMMARY")
print("----------------------------------------------------")
print("Total Vehicles Passed :", total)
print("Average Vehicles      :", round(average_vehicles, 2))
print("Maximum Vehicles      :", maximum_vehicles)
print("Traffic Density       :", most_common_density)

print("\nVEHICLE TYPE SUMMARY")
print("----------------------------------------------------")
print("Cars                  :", cars)
print("Motorcycles           :", motorcycles)
print("Buses                 :", buses)
print("Trucks                :", trucks)

print("\n====================================================")


# Create vehicle distribution graph
plt.figure(figsize=(8, 5))

plt.bar(
    vehicle_types,
    vehicle_counts
)

plt.title("Vehicle Type Distribution")

plt.xlabel("Vehicle Type")

plt.ylabel("Vehicles Passed")

plt.grid(axis="y")

plt.tight_layout()

plt.show()


# Create traffic trend graph
plt.figure(figsize=(10, 5))

plt.plot(
    df["Time"],
    df["Total"],
    marker="o"
)

plt.title("Traffic Flow Over Time")

plt.xlabel("Time")

plt.ylabel("Vehicles Passed")

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()

plt.show()


print("\nDashboard analysis completed successfully!")