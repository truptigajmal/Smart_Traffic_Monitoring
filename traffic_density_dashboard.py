import pandas as pd
import matplotlib.pyplot as plt

# Read traffic flow data
df = pd.read_csv("traffic_flow_data.csv")


# Function to classify traffic density
def get_density(vehicle_count):

    if vehicle_count <= 5:
        return "LOW"

    elif vehicle_count <= 15:
        return "MEDIUM"

    else:
        return "HIGH"


# Create density column
df["Density"] = df["Total"].apply(get_density)


# Keep density order fixed
density_order = [
    "LOW",
    "MEDIUM",
    "HIGH"
]


# Count density levels
density_counts = (
    df["Density"]
    .value_counts()
    .reindex(
        density_order,
        fill_value=0
    )
)


# Display dashboard information
print("\n")
print("==============================================")
print("        TRAFFIC DENSITY DASHBOARD")
print("==============================================")

print("\nTRAFFIC DENSITY SUMMARY")
print("----------------------------------------------")

print("LOW     :", density_counts["LOW"])
print("MEDIUM  :", density_counts["MEDIUM"])
print("HIGH    :", density_counts["HIGH"])

print("\nMost Common Density:",
      df["Density"].mode()[0])

print("\n==============================================")


# Create density graph
plt.figure(figsize=(8, 5))

plt.bar(
    density_counts.index,
    density_counts.values
)

plt.title(
    "Traffic Density Distribution"
)

plt.xlabel(
    "Traffic Density"
)

plt.ylabel(
    "Number of Records"
)

plt.grid(
    axis="y"
)

plt.tight_layout()

plt.show()


print("\nTraffic density dashboard completed!")