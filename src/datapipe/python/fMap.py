import folium

cord2 =(1.28967,103.85007)
cord = (1.3264301001450307, 103.80014894530179)
m = folium.Map(cord, zoom_start=12)
folium.Marker(location=[cord2[0],cord2[1]], fill_color = '#43d9de', radius = 8 ).add_to(m)

m.save('map.html')
