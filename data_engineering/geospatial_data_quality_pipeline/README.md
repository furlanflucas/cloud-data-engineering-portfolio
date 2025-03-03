# 🌍 Geospatial Data Quality Monitor  

## 📌 Overview  
This project **simulates a geospatial data quality pipeline** designed to ensure **high-accuracy mapping datasets**. It fetches **road network data from OpenStreetMap (OSM)**, detects **roads with missing speed limits**, and visualizes **anomalies** using **Folium maps** within a **Streamlit dashboard**.  

🚀 **Industry Relevance:**  
This project mirrors **real-world geospatial data validation workflows** I contributed to at **Cruise**, where ensuring high-quality, labeled map data was critical for **autonomous vehicle (AV) operations**. The methodology used here can be extended to **automated QA workflows**, similar to the **MapChecker AutoQA** system and other **ETL optimizations** I worked on.  

---

## ✅ Features  
- 🔍 **Fetch road network data** for a given location using OpenStreetMap (OSM).  
- ⚠️ **Detect missing speed limits**, identifying potential data quality issues.  
- 🗺 **Visualize geospatial anomalies** on an interactive Folium map.  
- 📊 **Streamlit dashboard** for real-time monitoring.  
- 🏎 **Optimized for large-scale geospatial analysis**, supporting automated validation workflows.  

---

## 🛠️ Technologies Used  
- 🐍 **Python** – Core scripting language  
- 🌍 **GeoPandas & OSMnx** – Geospatial data processing  
- 🗺 **Folium** – Map visualization  
- 🖥 **Streamlit** – Interactive dashboard  
- 🔷 **Shapely** – Geometry operations  
- 🛠 **SQL (for future integrations with PostGIS/BigQuery)**  

---

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
This project currently runs as a local simulation, but in a production setting, the following enhancements would improve scalability, automation, and cloud integration:

- ✅ Store processed data in a geospatial database (PostGIS, BigQuery, or Snowflake).
- ✅ Automate data validation workflows using Airflow or Prefect (similar to Cruise’s AV map update pipelines).
- ✅ Optimize ETL processes for batch and real-time anomaly detection at scale.
- ✅ Enhance speed limit validation accuracy with ML models deployed via AWS SageMaker.

## 🎯 Contributions
Pull requests are welcome! Feel free to contribute improvements or report issues.

---
## 👨‍💻 My Role & Industry Experience
At Cruise, my work focused on:
- ✅ Automating data validation workflows, integrating Python scripts and SQL-based anomaly detection.
- ✅ Building and optimizing geospatial data pipelines, ensuring 95%+ accuracy in labeled map data.
- ✅ Developing Looker dashboards to track data quality trends, leading to a 65% error reduction.
- ✅ Enhancing speed limit validation accuracy in ambiguous scenarios through ETL optimizations.
- ✅ Leading infrastructure improvements for geospatial data workflows, ensuring seamless AV map updates.

🚀 This project demonstrates my ability to automate data quality validation, process geospatial data at scale, and develop monitoring solutions for high-accuracy mapping systems.


🚀 **Developed by Lucas Furlan** | GitHub: [@furlanflucas](https://github.com/furlanflucas)


