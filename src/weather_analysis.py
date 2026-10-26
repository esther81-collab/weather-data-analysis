
import csv
from pathlib import Path
from statistics import mean

# Find the weather CSV file
project_dir = Path(__file__).resolve().parent.parent
csv_file = project_dir / "data" / "weather.csv"

# Read the weather data
with csv_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    weather_data = list(reader)

# Check that data exists
if not weather_data:
    print("No weather data found.")
else:
    temperatures = [
        float(row["temperature"])
        for row in weather_data
    ]

    rainfall = [
        float(row["rainfall"])
        for row in weather_data
    ]

    humidity = [
        float(row["humidity"])
        for row in weather_data
    ]

    print("WEATHER DATA ANALYSIS")
    print("---------------------")
    print(f"Total records: {len(weather_data)}")
    print(f"Average temperature: {mean(temperatures):.2f} °C")
    print(f"Highest temperature: {max(temperatures):.2f} °C")
    print(f"Lowest temperature: {min(temperatures):.2f} °C")
    print(f"Average humidity: {mean(humidity):.2f}%")
    print(f"Total rainfall: {sum(rainfall):.2f} mm")
