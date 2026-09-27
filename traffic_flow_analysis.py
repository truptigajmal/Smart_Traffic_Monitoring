import pandas as pd

# Read CSV file
df = pd.read_csv("traffic_flow_data.csv")

print("\n==========================================")
print("       VEHICLE FLOW DATA ANALYSIS")
print("==========================================")

# Show first 5 records
print("\nFirst 5 records:")
print(df.head())

# Total number of records
print("\nTotal records:", len(df))

# Get final cumulative counts
final_cars = df["Cars"].iloc[-1]
final_motorcycles = df["Motorcycles"].iloc[-1]
final_buses = df["Buses"].iloc[-1]
final_trucks = df["Trucks"].iloc[-1]
final_total = df["Total"].iloc[-1]

# Display total vehicles passed
print("\nTOTAL VEHICLES PASSED")
print("------------------------------------------")
print("Cars:", final_cars)
print("Motorcycles:", final_motorcycles)
print("Buses:", final_buses)
print("Trucks:", final_trucks)
print("Total vehicles:", final_total)

# Average cumulative count
average_total = df["Total"].mean()

print("\nAVERAGE RECORDED TOTAL")
print("------------------------------------------")
print("Average:", round(average_total, 2))

# Vehicle type with highest count
vehicle_totals = {
    "Cars": final_cars,
    "Motorcycles": final_motorcycles,
    "Buses": final_buses,
    "Trucks": final_trucks
}

most_common_vehicle = max(
    vehicle_totals,
    key=vehicle_totals.get
)

print("\nMOST COMMON VEHICLE TYPE")
print("------------------------------------------")
print(most_common_vehicle)

print("\n==========================================")
print("             ANALYSIS COMPLETE")
print("==========================================")