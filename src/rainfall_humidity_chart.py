import csv
from pathlib import Path
import matplotlib.pyplot as plt

# Find project folder and CSV file
project_dir = Path(__file__).resolve().parent.parent
csv_file = project_dir / "data" / "weather.csv"

# Read data
dates = []
rainfall = []
humidity = []

with csv_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        dates.append(row["date"])
        rainfall.append(float(row["rainfall"]))
        humidity.append(float(row["humidity"]))

# Create figure with 2 subplots (Rainfall bar chart & Humidity trend line chart)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Plot 1: Daily Rainfall Bar Chart
ax1.bar(dates, rainfall, color="skyblue", edgecolor="navy", alpha=0.8, label="Rainfall (mm)")
ax1.set_title("Daily Rainfall Trends", fontsize=14, fontweight="bold")
ax1.set_ylabel("Rainfall (mm)", fontsize=12)
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="upper left")

# Plot 2: Daily Humidity Trend Line Chart
ax2.plot(dates, humidity, color="teal", marker="o", linewidth=2, label="Humidity (%)")
ax2.set_title("Daily Humidity Trends", fontsize=14, fontweight="bold")
ax2.set_xlabel("Date", fontsize=12)
ax2.set_ylabel("Humidity (%)", fontsize=12)
ax2.tick_params(axis="x", rotation=45)
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper left")

plt.tight_layout()

# Save visualization
output_file = project_dir / "visualizations" / "rainfall_humidity_chart.png"
output_file.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_file, dpi=150)
print(f"Rainfall & Humidity chart successfully saved to: {output_file}")

# Display the chart window on screen
plt.show()
