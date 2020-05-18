import folium
import pandas as pd


def index_of_danger(ind):
    if ind == 1:
        return colors[0]
    elif ind == 2:
        return colors[1]


html = """
%s
<img src='anyimage'>
"""
legend_html = '''
                <div style="position: fixed; 
                            bottom: 520px; left: 10px; width: 100px; height: 140px;  
                            border:2px solid grey; z-index:9999; font-size:14px; font-family:Avantgarde;
                            line-height:2;
                            "><b><font size=3>&nbsp; Легенда </b></font><br>
                              &nbsp; Kaif &nbsp<i class="fa fa-circle fa-1x" style="color:green"></i><br>
                              &nbsp; Mid &nbsp; <i class="fa fa-circle fa-1x" style="color:orange"></i><br>
                              &nbsp; Мусора &nbsp; <i class="fa fa-female fa-2x" style="color:red"></i><br>
                </div>
                '''

colors = ['green', 'orange', 'red', 'gray']
data = pd.read_csv('chill.txt', encoding='cp1251')
lat = list(data["LAT"])
lon = list(data["LON"])
desc = list(data["DESCRIPTION"])
dindex = list(data["DANGERINDEX"])


map = folium.Map(location=[53.860838, 27.443097], zoom_start=12, worldCopyJump=True, min_zoom=12)


fg = folium.FeatureGroup(name="Места культурного отдыха")
for lt, ln, dc, di in zip(lat, lon, desc, dindex):
    iframe = folium.IFrame(html=html % dc, width=310, height=413)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=8, popup=folium.Popup(iframe), fill_color=index_of_danger(di), color=colors[3], fill=True, fill_opacity=0.7))

fgv = folium.FeatureGroup(name="Стражи галактики")
fgv.add_child(folium.GeoJson(data=open('test.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor': '#FF0000', 'color': '#FF0000'}))

folium.TileLayer('cartodbdark_matter', name='Темная тема').add_to(map)
folium.TileLayer('cartodbpositron', name='Светлая тема').add_to(map)


map.get_root().html.add_child(folium.Element(legend_html))

map.add_child(fg)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save(r'templates\map1.html')
