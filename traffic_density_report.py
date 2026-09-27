import pandas as pd

# Read traffic flow data
df = pd.read_csv("traffic_flow_data.csv")


# ============================================================
# TRAFFIC DENSITY FUNCTION
# ============================================================

def get_density(vehicle_count):

    if vehicle_count <= 5:
        return "LOW"

    elif vehicle_count <= 15:
        return "MEDIUM"

    else:
        return "HIGH"


# Create density column
df["Density"] = df["Total"].apply(get_density)


# ============================================================
# COUNT DENSITY LEVELS
# ============================================================

density_order = [
    "LOW",
    "MEDIUM",
    "HIGH"
]

density_counts = (
    df["Density"]
    .value_counts()
    .reindex(
        density_order,
        fill_value=0
    )
)


# ============================================================
# MOST COMMON DENSITY
# ============================================================

most_common_density = df["Density"].mode()[0]


# ============================================================
# CREATE REPORT
# ============================================================

report = pd.DataFrame({

    "Traffic Density": [
        "LOW",
        "MEDIUM",
        "HIGH",
        "Most Common Density"
    ],

    "Number of Records": [
        density_counts["LOW"],
        density_counts["MEDIUM"],
        density_counts["HIGH"],
        most_common_density
    ]

})


# ============================================================
# DISPLAY REPORT
# ============================================================

print("\n")
print("==============================================")
print("        TRAFFIC DENSITY REPORT")
print("==============================================")

print(
    report.to_string(
        index=False
    )
)

print("\n==============================================")


# ============================================================
# SAVE REPORT
# ============================================================

report.to_csv(
    "traffic_density_report.csv",
    index=False
)

print("Traffic density report saved successfully!")

print("File: traffic_density_report.csv")

print("==============================================")