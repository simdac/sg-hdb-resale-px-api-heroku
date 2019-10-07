import geopandas as gpd
import folium

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



shapefile = 'MapVectors/MP14_PLNG_AREA_WEB_PL.shp'

#shapefile = 'MapVectors/electoral-boundary-2015/electoral-boundary-2015-geojson.geojson'
#shapefile = 'MapVectors/hdb-branches/hdb-branches-geojson.geojson'
file = 'myfile.geojson'
geo_file = gpd.read_file(shapefile)

flatData = pd.read_csv('resale_flat_prices.csv')

print(geo_file)
print(flatData.shape)


#cData.set_index('town',inplace=True)
'''Ang = data.loc[data.town == 'ANG MO KIO']
print(Ang.shape)

Ang = Ang.dropna()
print(Ang.head()'''


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
#folium.LayerControl().add_to(map)

map.save('map2.html')
