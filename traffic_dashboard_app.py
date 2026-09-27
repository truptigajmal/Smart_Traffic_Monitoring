import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Smart Traffic Monitoring",
    page_icon="🚦",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🚦 Smart Traffic Monitoring System")
st.caption(
    "Last updated: "
    + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
)

# ============================================================
# SYSTEM STATUS
# ============================================================

st.success("🟢 System Status: Active")

st.write(
    "YOLO-based vehicle detection, tracking, traffic flow "
    "and density analysis"
)

# ============================================================
# REFRESH BUTTON
# ============================================================

if st.button("🔄 Refresh Data"):
    st.rerun()

# ============================================================
# LOAD DATA
# ============================================================

try:
    df = pd.read_csv("traffic_flow_data.csv")
except FileNotFoundError:
    st.error(
        "traffic_flow_data.csv not found. "
        "Please run main.py first."
    )
    st.stop()


# ============================================================
# VEHICLE COUNTS
# ============================================================

cars = int(df["Cars"].iloc[-1])
motorcycles = int(df["Motorcycles"].iloc[-1])
buses = int(df["Buses"].iloc[-1])
trucks = int(df["Trucks"].iloc[-1])

total_vehicles = (
    cars
    + motorcycles
    + buses
    + trucks
)


# ============================================================
# TRAFFIC STATISTICS
# ============================================================

average_vehicles = round(
    df["Total"].mean(),
    2
)

maximum_vehicles = int(
    df["Total"].max()
)


# ============================================================
# TRAFFIC DENSITY
# ============================================================

def get_density(vehicle_count):

    if vehicle_count <= 5:
        return "LOW"

    elif vehicle_count <= 15:
        return "MEDIUM"

    else:
        return "HIGH"


df["Density"] = df["Total"].apply(
    get_density
)

most_common_density = df["Density"].mode()[0]

# ============================================================
# TRAFFIC DENSITY STATUS
# ============================================================

if most_common_density == "LOW":
    st.success("🟢 Traffic Density: LOW")

elif most_common_density == "MEDIUM":
    st.warning("🟡 Traffic Density: MEDIUM")

else:
    st.error("🔴 Traffic Density: HIGH")

# ============================================================
# DASHBOARD METRICS
# ============================================================

st.subheader("📊 Traffic Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Vehicles",
        total_vehicles
    )

with col2:
    st.metric(
        "Average Vehicles",
        average_vehicles
    )

with col3:
    st.metric(
        "Maximum Vehicles",
        maximum_vehicles
    )

with col4:
    st.metric(
        "Traffic Density",
        most_common_density
    )


# ============================================================
# VEHICLE TYPE SUMMARY
# ============================================================

st.subheader("🚗 Vehicle Type Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Cars",
        cars
    )

with col2:
    st.metric(
        "Motorcycles",
        motorcycles
    )

with col3:
    st.metric(
        "Buses",
        buses
    )

with col4:
    st.metric(
        "Trucks",
        trucks
    )


# ============================================================
# VEHICLE DISTRIBUTION
# ============================================================

st.subheader("📈 Vehicle Type Distribution")

# ============================================================
# VEHICLE PERCENTAGES
# ============================================================

if total_vehicles > 0:

    percentage_data = pd.DataFrame({
        "Vehicle Type": [
            "Cars",
            "Motorcycles",
            "Buses",
            "Trucks"
        ],

        "Percentage": [
            round((cars / total_vehicles) * 100, 2),
            round((motorcycles / total_vehicles) * 100, 2),
            round((buses / total_vehicles) * 100, 2),
            round((trucks / total_vehicles) * 100, 2)
        ]
    })

    st.write("### Vehicle Percentage")

    st.dataframe(
        percentage_data,
        width="stretch"
    )

# ============================================================
# VEHICLE PERCENTAGE PIE CHART
# ============================================================

st.write("### Vehicle Type Percentage Chart")

plt.figure(figsize=(7, 7))

plt.pie(
    percentage_data["Percentage"],
    labels=percentage_data["Vehicle Type"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Vehicle Type Percentage")

st.pyplot(plt)
plt.close()

vehicle_data = pd.DataFrame({
    "Vehicle Type": [
        "Cars",
        "Motorcycles",
        "Buses",
        "Trucks"
    ],

    "Vehicles": [
        cars,
        motorcycles,
        buses,
        trucks
    ]
})

st.bar_chart(
    vehicle_data.set_index("Vehicle Type")
)


# ============================================================
# TRAFFIC FLOW
# ============================================================

st.subheader("📊 Traffic Flow Over Time")

flow_data = df[
    ["Time", "Total"]
].copy()

flow_data = flow_data.set_index(
    "Time"
)

st.line_chart(
    flow_data
)


# ============================================================
# DENSITY SUMMARY
# ============================================================

st.subheader("🚦 Traffic Density Distribution")

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

density_data = pd.DataFrame({
    "Density": density_order,
    "Records": density_counts.values
})

st.bar_chart(
    density_data.set_index("Density")
)

# ============================================================
# DENSITY BREAKDOWN
# ============================================================

density_percentage = (
    density_counts / density_counts.sum() * 100
).round(2)

density_breakdown = pd.DataFrame({
    "Traffic Density": density_order,
    "Records": density_counts.values,
    "Percentage": density_percentage.values
})

st.dataframe(
    density_breakdown,
    width="stretch"
)


# ============================================================
# DATA TABLE
# ============================================================

st.subheader("📋 Traffic Data")

st.dataframe(
    df,
    width="stretch"
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.write(
    "Smart Traffic Monitoring System | "
    "Python + YOLO + OpenCV + Pandas + Streamlit"
)

# ============================================================
# DOWNLOAD TRAFFIC REPORT
# ============================================================

st.subheader("📥 Download Traffic Report")

report_data = df.to_csv(
    index=False
)

st.download_button(
    label="Download Traffic Data CSV",
    data=report_data,
    file_name="traffic_data_report.csv",
    mime="text/csv"
)

# ============================================================
# PROJECT INFORMATION
# ============================================================

st.subheader("ℹ️ About This Project")

st.write("""
### Smart Traffic Monitoring System

This project uses Computer Vision and Data Science techniques
to monitor traffic automatically.

**Technologies Used:**
- Python
- YOLO
- OpenCV
- Pandas
- Matplotlib
- Streamlit
- ByteTrack

**Main Features:**
- Vehicle detection
- Vehicle tracking
- Vehicle counting
- Traffic flow analysis
- Traffic density detection
- Vehicle type analysis
- Data visualization
- Automated traffic reports
- Interactive web dashboard
""")

# ============================================================
# PROJECT OBJECTIVES
# ============================================================

st.subheader("🎯 Project Objectives")

objectives = [
    "Detect vehicles automatically using YOLO.",
    "Track vehicles using ByteTrack.",
    "Count vehicles crossing a traffic line.",
    "Identify cars, motorcycles, buses and trucks.",
    "Analyze traffic flow over time.",
    "Classify traffic density as LOW, MEDIUM or HIGH.",
    "Generate traffic reports automatically.",
    "Present traffic information using an interactive dashboard."
]

for i, objective in enumerate(objectives, start=1):
    st.write(f"**{i}.** {objective}")

# ============================================================
# PROJECT WORKFLOW
# ============================================================

st.subheader("🔄 Project Workflow")

workflow = [
    "Traffic Video Input",
    "YOLO Vehicle Detection",
    "ByteTrack Vehicle Tracking",
    "Vehicle Line-Crossing Detection",
    "Vehicle Counting",
    "Traffic Density Analysis",
    "Data Storage using CSV",
    "Pandas Data Analysis",
    "Data Visualization",
    "Streamlit Dashboard"
]

for i, step in enumerate(workflow, start=1):

    if i < len(workflow):
        st.write(
            f"**{i}. {step}**  ➡️"
        )
    else:
        st.write(
            f"**{i}. {step}**"
        )    