
import csv
from pathlib import Path
import matplotlib.pyplot as plt

# Find the project folder and CSV file
project_dir = Path(__file__).resolve().parent.parent
csv_file = project_dir / "data" / "weather.csv"

# Read dates and temperatures
dates = []
temperatures = []

with csv_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dates.append(row["date"])
        temperatures.append(float(row["temperature"]))

# Create the line chart
plt.figure(figsize=(12, 6))
plt.plot(dates, temperatures, marker="o", label="Temperature")

plt.title("Daily Temperature Analysis")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the chart
output_file = project_dir / "visualizations" / "temperature_chart.png"
output_file.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_file, dpi=150)

print(f"Chart saved to: {output_file}")
plt.show()

