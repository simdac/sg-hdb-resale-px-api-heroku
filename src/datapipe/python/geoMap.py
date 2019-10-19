import geopandas as gpd
import folium

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



shapefile = 'MapData/MP14_PLNG_AREA_WEB_PL.shp'


geo_file = gpd.read_file(shapefile)
flatData = pd.read_csv('resale_flat_prices.csv')

print(geo_file)
print(flatData.shape)



cord = (1.3264301001450307,103.80014894530179)
map = folium.Map(location=cord, zoom_start=12)
folium.Choropleth(  geo_data = geo_file,
                    fill_color='RdBu',
                    fill_opacity=0.7,
                    line_opacity=0.5,
                    data = flatData,
                    key_on = 'feature.properties.PLN_AREA_N',
                    columns = ['town','resale_price']
                    ).add_to(map)

map.save('map2.html')
