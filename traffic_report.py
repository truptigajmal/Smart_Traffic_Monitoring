import pandas as pd

# ==========================================
# READ TRAFFIC DATA
# ==========================================

df = pd.read_csv("traffic_data.csv")

# ==========================================
# BASIC STATISTICS
# ==========================================

average_total = df["Total"].mean()
maximum_total = df["Total"].max()

average_cars = df["Cars"].mean()
average_motorcycles = df["Motorcycles"].mean()
average_buses = df["Buses"].mean()
average_trucks = df["Trucks"].mean()

# ==========================================
# VEHICLE TOTALS
# ==========================================

total_cars = df["Cars"].sum()
total_motorcycles = df["Motorcycles"].sum()
total_buses = df["Buses"].sum()
total_trucks = df["Trucks"].sum()

# ==========================================
# TRAFFIC LEVEL
# ==========================================

traffic_levels = df["Traffic"].value_counts()

most_common_traffic = df["Traffic"].mode()[0]

# ==========================================
# DISPLAY REPORT
# ==========================================

print("\n")
print("==========================================")
print("       SMART TRAFFIC MONITORING REPORT")
print("==========================================")

print("\nDATA SUMMARY")
print("------------------------------------------")

print("Total records:", len(df))

print(
    "Average vehicles detected:",
    round(average_total, 2)
)

print(
    "Maximum vehicles detected:",
    maximum_total
)

print("\nAVERAGE VEHICLES")
print("------------------------------------------")

print("Cars:", round(average_cars, 2))

print(
    "Motorcycles:",
    round(average_motorcycles, 2)
)

print("Buses:", round(average_buses, 2))

print("Trucks:", round(average_trucks, 2))

print("\nTOTAL DETECTIONS")
print("------------------------------------------")

print("Cars:", total_cars)

print("Motorcycles:", total_motorcycles)

print("Buses:", total_buses)

print("Trucks:", total_trucks)

print("\nTRAFFIC LEVEL")
print("------------------------------------------")

print(
    "Most common traffic level:",
    most_common_traffic
)

print("\nTRAFFIC LEVEL COUNTS")
print("------------------------------------------")

print(traffic_levels)

print("\n==========================================")
print("             REPORT COMPLETE")
print("==========================================")