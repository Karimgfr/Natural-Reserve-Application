import pandas as pd
import geopandas as gpd

from fastapi import FastAPI
from fastapi import Response,HTTPException

from TP3 import is_poi_in_france, natura2000_fonc, znieff1_fonc, znieff2_fonc

from uvicorn import run

Natura2000_shape = gpd.read_file('sic/sic.shp')
znieff1_shape = gpd.read_file('znieff1/znieff1.shp')
znieff2_shape = gpd.read_file('znieff2/znieff2.shp')



# Section 4
app = FastAPI()

@app.get("/natura2000")
async def natura2000(latitude, longitude, radius_m):
   if not is_poi_in_france(latitude, longitude):
        raise HTTPException(status_code=404, detail="Point is not in France")
   
   gdf_natura2000_around_aoi = natura2000_fonc(latitude,longitude,radius_m)
   return Response(content=gdf_natura2000_around_aoi.to_json(), media_type='application/json', status_code=200)

@app.get("/znieff1")
async def znieff1(latitude, longitude, radius_m):
   if not is_poi_in_france(latitude, longitude):
        raise HTTPException(status_code=404, detail="Point is not in France")
   
   gdf_znieff1_around_aoi = znieff1_fonc(latitude,longitude,radius_m)
   return Response(content=gdf_znieff1_around_aoi.to_json(), media_type='application/json', status_code=200)

@app.get("/znieff2")
async def znieff2(latitude, longitude, radius_m):
   if not is_poi_in_france(latitude, longitude):
        raise HTTPException(status_code=404, detail="Point is not in France")
   
   gdf_znieff2_around_aoi = znieff2_fonc(latitude,longitude,radius_m)
   return Response(content=gdf_znieff2_around_aoi.to_json(), media_type='application/json', status_code=200)



if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)



