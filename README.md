# Natural-Reserve-Application

## 📍 Natural Reserves Mapping API

Welcome to the **Natural Reserves Mapping API** project! This project is an application that allows users to easily locate and display natural reserves across France.

### 🚀 Key Features

- **Advanced Geospatial Search**: Easily locate natural reserves such as Natura2000, ZNIEFF1, and ZNIEFF2 around a point of interest (POI) within a specified radius.
- **Interactive Maps**: Generate interactive maps using **Folium** to visualize natural reserves.
- **Powerful RESTful API**: Provides robust endpoints for querying and retrieving geospatial data via an API built with **FastAPI**.

### 🎯 Project Objective

The primary objective of this project is to offer users an easy and efficient way to search for and visualize natural reserves across France. By simply providing a latitude, longitude, and search radius, users can retrieve relevant geospatial data and view it on an interactive map. This project demonstrates proficiency in API development with **FastAPI** and geospatial data processing with **GeoPandas**.

### 📸 Demonstration

Below is a photo demonstration of the application in action:

1. Enter a latitude, longitude, and search radius.
2. Select a natural reserves database (Natura2000, ZNIEFF1, ZNIEFF2).
3. The application retrieves and displays relevant natural reserves on an interactive map.

![Application Demonstration](Streamlit_example.PNG)

### 🛠️ Technologies Used

- **Python 3.7+**
- **FastAPI**
- **GeoPandas**
- **Shapely**
- **Folium**
- **Uvicorn**
- **Streamlit** (for the web application)

### 🔧 What's Left to Do

- **Deployment**: Deploy the application to a cloud platform for public access.
- **Performance Optimization**: Optimize the API performance for handling larger datasets and more complex queries.
- **Additional API Endpoints**: Add more endpoints to support advanced queries, such as filtering by specific reserve characteristics.
- **Data Collection for Expansion**: Gather and integrate data for natural reserves in other countries to extend the application's coverage beyond France.
- **GBIF API Integration**: Add biodiversity observations around a POI using data from the **GBIF** API.

