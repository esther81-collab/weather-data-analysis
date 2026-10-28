import csv
from collections import defaultdict
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
    temperatures = [float(row["temperature"]) for row in weather_data]
    rainfall = [float(row["rainfall"]) for row in weather_data]
    humidity = [float(row["humidity"]) for row in weather_data]

    print("WEATHER DATA ANALYSIS")
    print("---------------------")
    print(f"Total records: {len(weather_data)}")
    print(f"Average temperature: {mean(temperatures):.2f} °C")
    print(f"Highest temperature: {max(temperatures):.2f} °C")
    print(f"Lowest temperature: {min(temperatures):.2f} °C")
    print(f"Average humidity: {mean(humidity):.2f}%")
    print(f"Total rainfall: {sum(rainfall):.2f} mm\n")

    # Group weather data by condition (Sunny, Rainy, Cloudy)
    by_condition = defaultdict(list)
    for row in weather_data:
        condition = row["weather"]
        by_condition[condition].append({
            "temp": float(row["temperature"]),
            "humidity": float(row["humidity"]),
            "rainfall": float(row["rainfall"]),
        })

    print("SUMMARY BY WEATHER CONDITION")
    print("----------------------------")
    for condition, records in sorted(by_condition.items()):
        avg_temp = mean(r["temp"] for r in records)
        avg_hum = mean(r["humidity"] for r in records)
        tot_rain = sum(r["rainfall"] for r in records)
        count = len(records)
        print(f"• {condition} ({count} days):")
        print(f"    - Avg Temperature: {avg_temp:.2f} °C")
        print(f"    - Avg Humidity:    {avg_hum:.2f}%")
        print(f"    - Total Rainfall:  {tot_rain:.2f} mm")
