import pandas as pd
import matplotlib.pyplot as plt

# Read traffic flow data
df = pd.read_csv("traffic_flow_data.csv")

# Function to determine traffic density
def get_density(vehicle_count):

    if vehicle_count <= 5:
        return "LOW"

    elif vehicle_count <= 15:
        return "MEDIUM"

    else:
        return "HIGH"


# Calculate density for each record
df["Density"] = df["Total"].apply(get_density)


# Display data
print("\n==========================================")
print("          TRAFFIC DENSITY ANALYSIS")
print("==========================================")

print("\nTraffic Data:")
print(df[["Time", "Total", "Density"]].head(20))


# Count density levels
density_counts = df["Density"].value_counts()

print("\nDENSITY SUMMARY")
print("------------------------------------------")
print(density_counts)


# Most common density
most_common_density = df["Density"].mode()[0]

print("\nMOST COMMON TRAFFIC DENSITY")
print("------------------------------------------")
print(most_common_density)


# Create density graph
plt.figure(figsize=(8, 5))

density_counts.plot(
    kind="bar"
)

plt.title("Traffic Density Distribution")

plt.xlabel("Traffic Density")

plt.ylabel("Number of Records")

plt.xticks(rotation=0)

plt.grid(axis="y")

plt.tight_layout()

plt.show()


print("\n==========================================")
print("        DENSITY ANALYSIS COMPLETE")
print("==========================================")