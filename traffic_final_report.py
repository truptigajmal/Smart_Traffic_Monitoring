import pandas as pd

# Read traffic flow data
df = pd.read_csv("traffic_flow_data.csv")


# -------------------------------
# TOTAL VEHICLES PASSED
# -------------------------------

final_cars = df["Cars"].iloc[-1]
final_motorcycles = df["Motorcycles"].iloc[-1]
final_buses = df["Buses"].iloc[-1]
final_trucks = df["Trucks"].iloc[-1]
final_total = df["Total"].iloc[-1]


# -------------------------------
# AVERAGE VEHICLES
# -------------------------------

average_total = df["Total"].mean()


# -------------------------------
# MAXIMUM VEHICLES
# -------------------------------

maximum_total = df["Total"].max()


# -------------------------------
# VEHICLE TYPE WITH HIGHEST COUNT
# -------------------------------

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


# -------------------------------
# TRAFFIC DENSITY
# -------------------------------

def get_density(vehicle_count):

    if vehicle_count <= 5:
        return "LOW"

    elif vehicle_count <= 15:
        return "MEDIUM"

    else:
        return "HIGH"


df["Density"] = df["Total"].apply(get_density)


density_counts = df["Density"].value_counts()

most_common_density = df["Density"].mode()[0]


# -------------------------------
# FINAL REPORT
# -------------------------------

print("\n")
print("================================================")
print("          SMART TRAFFIC MONITORING")
print("             FINAL TRAFFIC REPORT")
print("================================================")


print("\nVEHICLE FLOW SUMMARY")
print("-----------------------------------------------")

print("Cars Passed        :", final_cars)
print("Motorcycles Passed :", final_motorcycles)
print("Buses Passed       :", final_buses)
print("Trucks Passed      :", final_trucks)

print("TOTAL VEHICLES     :", final_total)


print("\nTRAFFIC STATISTICS")
print("-----------------------------------------------")

print(
    "Average Vehicles   :",
    round(average_total, 2)
)

print(
    "Maximum Vehicles   :",
    maximum_total
)


print("\nMOST COMMON VEHICLE")
print("-----------------------------------------------")

print(
    "Vehicle Type       :",
    most_common_vehicle
)


print("\nTRAFFIC DENSITY")
print("-----------------------------------------------")

print(
    "Most Common Level  :",
    most_common_density
)


print("\nDENSITY DISTRIBUTION")
print("-----------------------------------------------")

print(density_counts)


print("\n================================================")
print("             REPORT COMPLETE")
print("================================================")