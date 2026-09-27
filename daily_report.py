import pandas as pd

# ==========================================
# READ TRAFFIC DATA
# ==========================================

df = pd.read_csv("traffic_data.csv")

# ==========================================
# CALCULATE STATISTICS
# ==========================================

average_vehicles = df["Total"].mean()
maximum_vehicles = df["Total"].max()

average_cars = df["Cars"].mean()
average_motorcycles = df["Motorcycles"].mean()
average_buses = df["Buses"].mean()
average_trucks = df["Trucks"].mean()

# ==========================================
# MOST COMMON TRAFFIC LEVEL
# ==========================================

most_common_traffic = df["Traffic"].mode()[0]

# ==========================================
# CREATE REPORT
# ==========================================

report = pd.DataFrame({
    "Metric": [
        "Total Records",
        "Average Vehicles",
        "Maximum Vehicles",
        "Average Cars",
        "Average Motorcycles",
        "Average Buses",
        "Average Trucks",
        "Most Common Traffic Level"
    ],

    "Value": [
        len(df),
        round(average_vehicles, 2),
        maximum_vehicles,
        round(average_cars, 2),
        round(average_motorcycles, 2),
        round(average_buses, 2),
        round(average_trucks, 2),
        most_common_traffic
    ]
})

# ==========================================
# SAVE REPORT
# ==========================================

report.to_csv(
    "daily_traffic_report.csv",
    index=False
)

# ==========================================
# DISPLAY REPORT
# ==========================================

print("\n======================================")
print("       DAILY TRAFFIC REPORT")
print("======================================\n")

print(report)

print("\n======================================")
print("Report saved as:")
print("daily_traffic_report.csv")
print("======================================")