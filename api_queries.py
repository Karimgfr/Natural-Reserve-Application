import requests
import geopandas as gpd


# J'ai un problème que je n'ai pas su régler au niveau des fonctions query_natura2000, query_znieff ...

def query_api(latitude, longitude, radius, endpoint):
    url = f"http://127.0.0.1:8000/{endpoint}"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "radius_m": radius
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for bad responses
    return response.json()

def query_natura2000(latitude, longitude, radius):
    response_json = query_api(latitude, longitude, radius, "natura2000")
    return response_json

def query_znieff1(latitude, longitude, radius):
    response_json = query_api(latitude, longitude, radius, "znieff1")
    return gpd.GeoDataFrame.from_features(response_json["features"])

def query_znieff2(latitude, longitude, radius):
    response_json = query_api(latitude, longitude, radius, "znieff2")
    return gpd.GeoDataFrame.from_features(response_json["features"])

