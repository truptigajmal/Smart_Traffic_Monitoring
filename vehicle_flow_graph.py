import pandas as pd
import matplotlib.pyplot as plt

# Read vehicle flow data
df = pd.read_csv("traffic_flow_data.csv")

# Convert time column
df["Time"] = pd.to_datetime(
    df["Time"],
    format="%H:%M:%S"
)

# Create graph
plt.figure(figsize=(10, 5))

# Plot vehicle types
plt.plot(
    df["Time"],
    df["Cars"],
    label="Cars"
)

plt.plot(
    df["Time"],
    df["Motorcycles"],
    label="Motorcycles"
)

plt.plot(
    df["Time"],
    df["Buses"],
    label="Buses"
)

plt.plot(
    df["Time"],
    df["Trucks"],
    label="Trucks"
)

# Graph title and labels
plt.title("Vehicle Flow Over Time")

plt.xlabel("Time")

plt.ylabel("Vehicles Passed")

# Show legend
plt.legend()

# Show grid
plt.grid(True)

# Rotate time labels
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Display graph
plt.show()