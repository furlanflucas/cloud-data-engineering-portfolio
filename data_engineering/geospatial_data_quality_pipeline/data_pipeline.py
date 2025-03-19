import os
import geopandas as gpd
import folium
import osmnx as ox
import streamlit as st
from shapely.geometry import LineString
from streamlit_folium import folium_static  

# 1. Create Data Directory
os.makedirs("data", exist_ok=True)

# 2. Download Road Data from OpenStreetMap
def fetch_osm_data(place="Austin, Texas"):
    print(f"Fetching road network data for {place}...")
    graph = ox.graph_from_place(place, network_type="drive")
    gdf = ox.graph_to_gdfs(graph, nodes=False, edges=True)
    gdf.to_file("data/road_data.geojson", driver="GeoJSON")
    return gdf

# 3. Validate Data: Detect Roads with Missing Speed Limits
def detect_anomalies(gdf):
    # Print available columns for debugging
    print("Available columns:", gdf.columns)

    # Check if 'maxspeed' exists in the dataset
    if "maxspeed" not in gdf.columns:
        print("Warning: 'maxspeed' column is missing in the dataset. No anomalies detected.")
        return gdf  

    # Print unique values in 'maxspeed' column
    print("Unique values in 'maxspeed':", gdf["maxspeed"].unique())

    # Identify roads with missing speed limits
    anomalies = gdf[gdf["maxspeed"].isnull()]
    
    return anomalies


# 4. Visualize Data Issues on a Map
def plot_anomalies(anomalies):
    m = folium.Map(location=[30.2672, -97.7431], zoom_start=12)  

    if "highway" not in anomalies.columns:
        anomalies["highway"] = "Unknown Road Type"

    for _, row in anomalies.iterrows():
        if isinstance(row.geometry, LineString):
            folium.PolyLine(
                locations=[(pt[1], pt[0]) for pt in row.geometry.coords], 
                color='red', 
                tooltip=f"{row['highway']} - (Missing Speed Limit)"
            ).add_to(m)
    
    return m

# 5. Build Streamlit Dashboard
def main():
    st.title("Geospatial Data Quality Monitor")
    st.info(" This is a **mock project** inspired by my work at Cruise. The data is simulated, but the methodology reflects real-world geospatial data validation workflows.")

    
    if st.button("Fetch & Process Data"):
        gdf = fetch_osm_data()
        st.success("Data has been fetched and saved!")

    if st.button("Detect Anomalies"):
        gdf = gpd.read_file("data/road_data.geojson")
        anomalies = detect_anomalies(gdf)
        st.write(f"Found {len(anomalies)} roads with missing speed limits.")

        m = plot_anomalies(anomalies)
        
        # ✅ Use folium_static to properly render the map
        folium_static(m)  

if __name__ == "__main__":
    main()

