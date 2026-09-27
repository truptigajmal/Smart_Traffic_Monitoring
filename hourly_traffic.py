import pandas as pd
import matplotlib.pyplot as plt

# Read traffic data
df = pd.read_csv("traffic_data.csv")

# Convert Time into datetime
df["Time"] = pd.to_datetime(
    df["Time"],
    format="%H:%M:%S"
)

# Extract hour
df["Hour"] = df["Time"].dt.hour

# Calculate average vehicles for each hour
hourly_data = df.groupby("Hour")["Total"].mean()

print("\n========== HOURLY TRAFFIC ==========\n")

print(hourly_data)

print("\n====================================")

# Create graph
plt.figure(figsize=(10, 5))

plt.plot(
    hourly_data.index,
    hourly_data.values,
    marker="o"
)

plt.title("Average Traffic by Hour")
plt.xlabel("Hour")
plt.ylabel("Average Number of Vehicles")

plt.grid(True)
plt.xticks(hourly_data.index)

plt.tight_layout()

plt.show()