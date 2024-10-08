## Section 1


import geopandas as gpd
import pandas as pd
import random


France_shape = gpd.read_file('Europe/France_only.shp')


from shapely import geometry

def is_poi_in_france (latitude,longitude):
    point = geometry.Point(longitude,latitude)
    polygon_france = France_shape['geometry']
    return(polygon_france.contains(point).any())



Natura2000_shape = gpd.read_file('sic/sic.shp')
znieff1_shape = gpd.read_file('znieff1/znieff1.shp')
znieff2_shape = gpd.read_file('znieff2/znieff2.shp')


def natura2000_fonc(latitude, longitude, radius_m):
   if isinstance(radius_m, str):
       radius_m = float(radius_m)
   latitude, longitude, radius_m = float(latitude), float(longitude), int(radius_m)
   df_point = pd.DataFrame({"latitude": [latitude],
                            "longitude": [longitude]})
   gdf_point = gpd.GeoDataFrame(
       df_point,
       geometry=gpd.points_from_xy(df_point.longitude, df_point.latitude), crs="EPSG:4326"
   )
   gdf_point = gdf_point.to_crs("epsg:2154")
   gdf_point["geometry"] = gdf_point["geometry"].buffer(radius_m)
   gdf_natura2000_aoi = gpd.sjoin(Natura2000_shape, gdf_point, how="inner")
   gdf_natura2000_aoi = gdf_natura2000_aoi[['SITENAME', 'geometry']]
   gdf_natura2000_aoi = gdf_natura2000_aoi.to_crs("epsg: 4326")

   return gdf_natura2000_aoi


def znieff1_fonc(latitude, longitude, radius_m):
   if isinstance(radius_m, str):
       radius_m = float(radius_m)
   latitude, longitude, radius_m = float(latitude), float(longitude), int(radius_m)
   df_point = pd.DataFrame({"latitude": [latitude],
                            "longitude": [longitude]})
   gdf_point = gpd.GeoDataFrame(
       df_point,
       geometry=gpd.points_from_xy(df_point.longitude, df_point.latitude), crs="EPSG:4326"
   )
   gdf_point = gdf_point.to_crs("epsg:2154")
   gdf_point["geometry"] = gdf_point["geometry"].buffer(radius_m)
   gdf_znieff1_aoi = gpd.sjoin(znieff1_shape, gdf_point, how="inner")
   gdf_znieff1_aoi = gdf_znieff1_aoi[['NOM','geometry']]
   gdf_znieff1_aoi = gdf_znieff1_aoi.to_crs("epsg: 4326")
   return gdf_znieff1_aoi


def znieff2_fonc(latitude, longitude, radius_m):
   if isinstance(radius_m, str):
       radius_m = float(radius_m)
   latitude, longitude, radius_m = float(latitude), float(longitude), int(radius_m)
   df_point = pd.DataFrame({"latitude": [latitude],
                            "longitude": [longitude]})
   gdf_point = gpd.GeoDataFrame(
       df_point,
       geometry=gpd.points_from_xy(df_point.longitude, df_point.latitude), crs="EPSG:4326"
   )
   gdf_point = gdf_point.to_crs("epsg:2154")
   gdf_point["geometry"] = gdf_point["geometry"].buffer(radius_m)
   gdf_znieff2_aoi = gpd.sjoin(znieff2_shape, gdf_point, how="inner")
   gdf_znieff2_aoi = gdf_znieff2_aoi[['NOM', 'geometry']]
   gdf_znieff2_aoi = gdf_znieff2_aoi.to_crs("epsg: 4326")
   return gdf_znieff2_aoi

#gdf_natura2000 = natura2000_fonc(44.192944614238776, 5.943911753410677,10000)
#gdf_znieff1 = znieff1_fonc(44.192944614238776, 5.943911753410677,10000)
#gdf_znieff2 = znieff2_fonc(44.192944614238776, 5.943911753410677,10000)


import folium

def generate_folium_map(latitude, longitude, gdf_dict):
    # Créer la carte centrée sur le point spécifié, avec un zoom étendu
    m = folium.Map(location=[latitude, longitude], zoom_start=10, width='100%', height='100%')

    # Ajouter une épingle pour le Point d'Intérêt (POI) fourni par l'utilisateur
    folium.Marker(
        location=[latitude, longitude],
        icon=folium.Icon(icon="map-marker", color="red"),  # Utiliser une épingle rouge pour plus de clarté
        popup="Point d'Intérêt sélectionné"
    ).add_to(m)

    # Code couleur pour les différents types de réserves
    color_dict = {
        'natura2000': 'green',
        'znieff1': 'blue',
        'znieff2': 'purple'
    }

    # Ajouter les couches IGN
    ign = "https://wxs.ign.fr/an7nvfzojv5wa96dsga5nk8w/geoportail/wmts?" + \
          "SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=ORTHOIMAGERY.ORTHOPHOTOS" + \
          "&STYLE=normal&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}" + \
          "&FORMAT=image/jpeg"
    
    folium.TileLayer(
        tiles=ign,
        attr="IGN-F/Geoportail",
        name="IGN Orthophotos",
        overlay=True,
        control=False,
    ).add_to(m)

    # Pour chaque type de réserve sélectionnée, afficher les polygones avec des couleurs différentes
    for reserve_type, gdf in gdf_dict.items():
        if not gdf.empty:
            color = color_dict.get(reserve_type, "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))  # Couleur aléatoire si non définie
            for _, r in gdf.iterrows():
                sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                geo_j = sim_geo.to_json()
                geo_j = folium.GeoJson(data=geo_j, style_function=lambda x, color=color: {"fillColor": color, "color": color})
                
                # Ajouter des popups pour afficher les informations des sites
                site_name = r["SITENAME"] if "SITENAME" in r else r.get("NOM", "Site inconnu")
                folium.Popup(f"{reserve_type}: {site_name}").add_to(geo_j)
                
                geo_j.add_to(m)

    return m