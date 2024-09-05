import streamlit as st
import folium
from streamlit_folium import folium_static
import geopandas as gpd
from api_queries import query_natura2000, query_znieff1, query_znieff2
from TP3 import generate_folium_map

# Titre de l'application
st.title("Carte des Réserves Naturelles en France")

# Affichage des paramètres utilisateur sur le côté
st.sidebar.header("Paramètres de la carte")
latitude = st.sidebar.number_input("Entrez la latitude", value=48.8566)
longitude = st.sidebar.number_input("Entrez la longitude", value=2.3522)
radius_m = st.sidebar.number_input("Entrez le rayon (en mètres)", value=1000)

# Sélection multiple des types de réserves
reserve_types = st.sidebar.multiselect("Choisissez les types de réserves", ["natura2000", "znieff1", "znieff2"], default=["natura2000"])

# Bouton pour soumettre
if st.sidebar.button("Afficher la carte"):
    gdf_dict = {}
    
    # Appel de l'API pour chaque type de réserve sélectionné
    if "natura2000" in reserve_types:
        gdf_dict["natura2000"] = gpd.GeoDataFrame.from_features(query_natura2000(latitude, longitude, radius_m)['features'])
    if "znieff1" in reserve_types:
        gdf_dict["znieff1"] = query_znieff1(latitude, longitude, radius_m)
    if "znieff2" in reserve_types:
        gdf_dict["znieff2"] = query_znieff2(latitude, longitude, radius_m)

    # Générer la carte avec plusieurs réserves colorées
    if gdf_dict:
        folium_map = generate_folium_map(latitude, longitude, gdf_dict)
        # Agrandir la carte pour occuper toute la largeur
        folium_static(folium_map, width=1200, height=800)
    else:
        st.error("Aucune réserve trouvée dans la zone spécifiée.")