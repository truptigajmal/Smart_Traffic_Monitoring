# 🚦 Smart Traffic Monitoring System

A Computer Vision and Data Science project that automatically detects, tracks, counts, and analyzes vehicles from traffic video using **YOLO, OpenCV, ByteTrack, Pandas, Matplotlib, and Streamlit**.

## 📌 Project Overview

The Smart Traffic Monitoring System analyzes traffic video and provides useful information such as:

* Number of cars
* Number of motorcycles
* Number of buses
* Number of trucks
* Total vehicles passed
* Traffic flow over time
* Traffic density
* Vehicle type distribution
* Vehicle percentages
* Automated traffic reports
* Interactive web dashboard

## 🎯 Objectives

1. Detect vehicles automatically using YOLO.
2. Track vehicles using ByteTrack.
3. Count vehicles crossing a predefined traffic line.
4. Identify different vehicle types.
5. Analyze traffic flow over time.
6. Classify traffic density as LOW, MEDIUM, or HIGH.
7. Generate traffic reports automatically.
8. Visualize traffic information through graphs.
9. Provide an interactive Streamlit dashboard.

## 🛠️ Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Main programming language |
| YOLO       | Vehicle detection         |
| OpenCV     | Video processing          |
| ByteTrack  | Vehicle tracking          |
| Pandas     | Data analysis             |
| Matplotlib | Data visualization        |
| Streamlit  | Interactive dashboard     |
| CSV        | Data storage              |

## 🚗 Vehicle Classes

The system detects four main vehicle categories:

* 🚗 Car
* 🏍️ Motorcycle
* 🚌 Bus
* 🚚 Truck

## 🔄 Project Workflow

```text
Traffic Video
      ↓
YOLO Vehicle Detection
      ↓
ByteTrack Vehicle Tracking
      ↓
Line-Crossing Detection
      ↓
Vehicle Counting
      ↓
Traffic Density Analysis
      ↓
CSV Data Storage
      ↓
Pandas Data Analysis
      ↓
Data Visualization
      ↓
Streamlit Dashboard
```

## 🚦 Traffic Density

The project uses the following demo thresholds:

| Vehicles | Density |
| -------: | ------- |
|      0–5 | LOW     |
|     6–15 | MEDIUM  |
|      16+ | HIGH    |

These thresholds are project/demo thresholds and are not official traffic-management standards.

## 📊 Data Analysis

The system performs:

* Total vehicle counting
* Average vehicle analysis
* Maximum vehicle analysis
* Vehicle type analysis
* Vehicle percentage analysis
* Traffic density analysis
* Traffic flow analysis
* Hourly traffic analysis

## 📈 Visualizations

The project generates:

* Vehicle type distribution
* Traffic flow over time
* Traffic density distribution
* Vehicle percentage pie chart
* Hourly traffic analysis

## 🌐 Streamlit Dashboard

The project includes an interactive web dashboard.

Run:

```bash
py -3.10 -m streamlit run traffic_dashboard_app.py
```

Then open:

```text
http://localhost:8501
```

The dashboard provides:

* Traffic summary
* Vehicle type summary
* Traffic density status
* Vehicle distribution
* Vehicle percentage chart
* Traffic flow graph
* Density breakdown
* Raw traffic data
* CSV download
* Project objectives
* Project workflow
* System status
* Last updated time

## 📁 Important Project Files

```text
Smart_Traffic_Monitoring/
│
├── main.py
├── traffic_dashboard_app.py
├── yolo11n.pt
├── traffic_video.mp4
│
├── traffic_flow_data.csv
├── traffic_density_report.csv
├── complete_traffic_report.csv
├── master_traffic_report.csv
├── hourly_traffic_report.csv
├── vehicle_type_report.csv
└── vehicle_percentage_report.csv
```

## ▶️ How to Run the Project

### 1. Open the project folder

```bash
cd "C:\Users\gajma\OneDrive\Desktop\Smart_Traffic_Monitoring"
```

### 2. Run the main traffic monitoring system

```bash
py -3.10 main.py
```

This performs:

* Vehicle detection
* Vehicle tracking
