import pandas as pd
import matplotlib.pyplot as plt

# Read vehicle percentage report
df = pd.read_csv("vehicle_percentage_report.csv")

# Get data
vehicle_types = df["Vehicle Type"]
percentages = df["Percentage"]

# Create pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    percentages,
    labels=vehicle_types,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Vehicle Type Distribution")

plt.tight_layout()

plt.show()