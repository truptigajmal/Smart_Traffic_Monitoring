import pandas as pd

# Read master report
df = pd.read_csv("master_traffic_report.csv")

print("\n")
print("======================================================")
print("        SMART TRAFFIC MONITORING SYSTEM")
print("              FINAL PROJECT SUMMARY")
print("======================================================")

print("\nPROJECT FEATURES")
print("------------------------------------------------------")

print("1. Vehicle Detection")
print("2. Vehicle Tracking")
print("3. Vehicle Counting")
print("4. Vehicle Flow Monitoring")
print("5. Traffic Density Detection")
print("6. Vehicle Type Analysis")
print("7. Traffic Statistics")
print("8. Hourly Traffic Analysis")
print("9. Data Visualization")
print("10. Automated Traffic Reports")

print("\n------------------------------------------------------")
print("             TRAFFIC RESULTS")
print("------------------------------------------------------")

for index, row in df.iterrows():

    metric = row["Metric"]
    value = row["Value"]

    print(f"{metric:<30}: {value}")

print("\n------------------------------------------------------")
print("             TECHNOLOGIES USED")
print("------------------------------------------------------")

print("Python")
print("YOLO")
print("OpenCV")
print("Pandas")
print("Matplotlib")
print("ByteTrack")

print("\n------------------------------------------------------")
print("              PROJECT OUTPUTS")
print("------------------------------------------------------")

print("traffic_flow_data.csv")
print("final_traffic_report.csv")
print("hourly_traffic_report.csv")
print("vehicle_type_report.csv")
print("vehicle_percentage_report.csv")
print("master_traffic_report.csv")

print("\n======================================================")
print("       SMART TRAFFIC MONITORING SYSTEM")
print("             PROJECT COMPLETED")
print("======================================================")