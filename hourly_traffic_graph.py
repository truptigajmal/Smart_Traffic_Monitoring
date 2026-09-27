import pandas as pd
import matplotlib.pyplot as plt

# Read hourly traffic report
df = pd.read_csv("hourly_traffic_report.csv")

# Display data
print("\n==========================================")
print("        HOURLY TRAFFIC GRAPH")
print("==========================================")

print(df)

# Create graph
plt.figure(figsize=(10, 5))

plt.plot(
    df["Hour"],
    df["Average_Vehicles"],
    marker="o",
    label="Average Vehicles"
)

plt.plot(
    df["Hour"],
    df["Maximum_Vehicles"],
    marker="o",
    label="Maximum Vehicles"
)

plt.title("Hourly Traffic Analysis")

plt.xlabel("Hour")

plt.ylabel("Number of Vehicles")

plt.xticks(df["Hour"])

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()