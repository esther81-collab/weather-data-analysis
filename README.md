#  Weather Data Analysis

An exploratory data analysis (EDA) project for weather data written in Python and Jupyter Notebook.

---

##  Project Structure

```text
weather-data-analysis/
│
├── data/
│   └── weather.csv                 # Weather dataset (20 days)
│
├── notebooks/
│   └── weather_analysis.ipynb      # Interactive Jupyter notebook analysis
│
├── src/
│   ├── weather_analysis.py         # Summary statistics & condition grouping script
│   ├── temperature_chart.py        # Line chart script for daily temperature
│   └── rainfall_humidity_chart.py  # Bar & line chart script for rainfall & humidity
│
└── visualizations/
    ├── temperature_chart.png       # Daily temperature line chart plot
    └── rainfall_humidity_chart.png # Daily rainfall & humidity chart plot
```

---

##  Weather Analysis Overview

- **Dataset Size:** 20 daily records
- **Average Temperature:** `27.75 °C` (Range: `23.00 °C` to `33.00 °C`)
- **Average Humidity:** `68.95%`
- **Total Rainfall:** `103.00 mm`

### Breakdown by Weather Condition

| Weather Condition | Days Count | Avg Temperature | Avg Humidity | Total Rainfall |
| :--- | :---: | :---: | :---: | :---: |
|  **Sunny** | 9 | `30.33 °C` | `60.00%` | `3.30 mm` |
|  **Cloudy** | 4 | `27.00 °C` | `73.00%` | `19.70 mm` |
|  **Rainy** | 7 | `24.71 °C` | `81.71%` | `80.00 mm` |

---

## 🚀 How to Run

1. **Run Python Analysis Script:**
   ```bash
   python3 src/weather_analysis.py
   ```

2. **Generate Visualizations:**
   ```bash
   python3 src/temperature_chart.py
   python3 src/rainfall_humidity_chart.py
   ```

3. **Explore Jupyter Notebook:**
   ```bash
   jupyter notebook notebooks/weather_analysis.ipynb
   ```
