import pandas as pd

# Read traffic flow data
df = pd.read_csv("traffic_flow_data.csv")

# Convert Time column into datetime
df["Time"] = pd.to_datetime(
    df["Time"],
    format="%H:%M:%S"
)

# Extract hour
df["Hour"] = df["Time"].dt.hour

# Calculate average traffic for each hour
hourly_report = df.groupby("Hour").agg(
    Average_Vehicles=("Total", "mean"),
    Maximum_Vehicles=("Total", "max")
)

# Round values
hourly_report["Average_Vehicles"] = (
    hourly_report["Average_Vehicles"].round(2)
)

# Display report
print("\n==========================================")
print("          HOURLY TRAFFIC REPORT")
print("==========================================")

print(hourly_report)

print("\n==========================================")

# Save report to CSV
hourly_report.to_csv(
    "hourly_traffic_report.csv"
)

print("Hourly report saved successfully!")
print("File: hourly_traffic_report.csv")

print("==========================================")