# Geospatial Data Quality Monitor

## 📌 Overview
This project is a **Geospatial Data Quality Monitor** that fetches road network data from **OpenStreetMap (OSM)**, detects roads with **missing speed limits**, and visualizes anomalies using **Folium maps** within a **Streamlit dashboard**.

## 🚀 Features
- **Fetch road network data** for a given location.
- **Detect roads with missing speed limits**.
- **Display anomalies on an interactive map**.
- **Streamlit web app** for easy interaction.

## 🛠️ Technologies Used
- **Python** for scripting
- **GeoPandas & OSMnx** for geospatial data processing
- **Folium** for map visualization
- **Streamlit** for building the dashboard
- **Shapely** for geometry operations

## 📂 Project Structure
```
📂 geospatial_data_quality_pipeline
├── 📂 data                  # Directory for storing geospatial data
│   ├── road_data.geojson    # Processed OSM data (auto-generated)
├── data_pipeline.py         # Main script containing the Streamlit app
├── README.md                # Project documentation
```

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies
Make sure you have **Python 3.8+** installed. Then, install the required libraries:
```bash
pip install geopandas folium osmnx shapely streamlit
```

### 2️⃣ Run the Streamlit App
Navigate to the project folder and run:
```bash
streamlit run data_pipeline.py
```

### 3️⃣ Use the Dashboard
1. Click **"Fetch & Process Data"** to download road network data from OpenStreetMap.
2. Click **"Detect Anomalies"** to find roads **missing speed limits**.
3. View the **interactive Folium map** displaying problematic roads.

## 📝 How It Works
### **1. Fetch Data from OpenStreetMap**
- Uses `OSMnx` to fetch the road network for a given city.
- Converts it to a **GeoDataFrame** and saves it as **GeoJSON**.

### **2. Detect Anomalies (Missing Speed Limits)**
- Checks if the "maxspeed" attribute is missing from any roads.
- If missing, marks them as anomalies.

### **3. Visualize on an Interactive Map**
- Uses `Folium` to highlight problematic roads in **red**.
- Displays tooltips with the road type (`highway` attribute).

## 🛠 Future Improvements
- Store processed data in **SQLite/PostGIS** instead of GeoJSON.
- Add support for **more geospatial data quality checks**.
- Automate fetching and processing via **Airflow or Prefect**.

## 🎯 Contributions
Pull requests are welcome! Feel free to contribute improvements or report issues.

---

🚀 **Developed by Lucas Furlan** | GitHub: [@furlanflucas](https://github.com/furlanflucas)


