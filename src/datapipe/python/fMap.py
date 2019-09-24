import folium


cord = (1.3264301001450307,103.80014894530179)
m = folium.Map(cord, zoom_start=12)

m.save('map.html')
