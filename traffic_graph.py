import pandas as pd
import matplotlib.pyplot as plt

# Read traffic data
df = pd.read_csv("traffic_data.csv")

# Convert time column to datetime
df["Time"] = pd.to_datetime(
    df["Time"],
    format="%H:%M:%S"
)

# Create graph
plt.figure(figsize=(10, 5))

plt.plot(
    df["Time"],
    df["Total"],
    marker="o"
)

# Graph title
plt.title("Traffic Volume Over Time")

# X-axis
plt.xlabel("Time")

# Y-axis
plt.ylabel("Number of Vehicles")

# Rotate time labels
plt.xticks(rotation=45)

# Add grid
plt.grid(True)

# Adjust layout
plt.tight_layout()

# Show graph
plt.show()