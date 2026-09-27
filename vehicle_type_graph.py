import pandas as pd
import matplotlib.pyplot as plt

# Read traffic data
df = pd.read_csv("traffic_data.csv")

# Calculate average number of each vehicle type
vehicle_types = [
    "Cars",
    "Motorcycles",
    "Buses",
    "Trucks"
]

average_counts = [
    df["Cars"].mean(),
    df["Motorcycles"].mean(),
    df["Buses"].mean(),
    df["Trucks"].mean()
]

# Create bar graph
plt.figure(figsize=(8, 5))

plt.bar(vehicle_types, average_counts)

plt.title("Average Vehicle Type Detection")
plt.xlabel("Vehicle Type")
plt.ylabel("Average Number of Vehicles")

plt.grid(axis="y")
plt.tight_layout()

plt.show()