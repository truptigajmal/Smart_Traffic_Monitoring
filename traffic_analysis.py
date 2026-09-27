import pandas as pd

# Read traffic data
df = pd.read_csv("traffic_data.csv")

print("\n========== TRAFFIC DATA ==========\n")

# Display first 5 records
print("First 5 records:")
print(df.head())

# Number of records
print("\nTotal records:", len(df))

# Average vehicles
average_vehicles = df["Total"].mean()

print(
    "Average vehicles detected:",
    round(average_vehicles, 2)
)

# Maximum vehicles
maximum_vehicles = df["Total"].max()

print(
    "Maximum vehicles detected:",
    maximum_vehicles
)

# Average vehicle types
print("\nAverage vehicle counts:")

print(
    "Cars:",
    round(df["Cars"].mean(), 2)
)

print(
    "Motorcycles:",
    round(df["Motorcycles"].mean(), 2)
)

print(
    "Buses:",
    round(df["Buses"].mean(), 2)
)

print(
    "Trucks:",
    round(df["Trucks"].mean(), 2)
)

# Most common traffic level
most_common_traffic = df["Traffic"].mode()[0]

print(
    "\nMost common traffic level:",
    most_common_traffic
)

print("\n==================================")