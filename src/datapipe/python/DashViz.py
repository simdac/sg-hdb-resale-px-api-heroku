import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input,Output
import folium
import requests
from requests.models import PreparedRequest
import pandas as pd
from API import get_all
import geopandas as gpd
import OneMap



'''             Directly Load the data in dataframe, chek and reload to make sure its there      '''



from API import get_all

'''df  = get_all()
print(df.tail())
print(df.head())

town = df.town.unique()
street = df.street_name.unique()'''




mapApi = OneMap.MapAPI()
shapefile = 'MapData/MP14_PLNG_AREA_WEB_PL.shp'
geo_file = gpd.read_file(shapefile)
flatData = pd.read_csv('resale_flat_prices.csv')

external_stylesheets = ['https://codepen.io/chriddpy/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
app.config.suppress_callback_exceptions = True

app.layout = html.Div(children=[


        html.H1(children='Resale HDB Price App',
            style={
                'textAlign':'center'
            }
        ),



        dcc.Tabs(id='tabs',value='tab-1',children=[
           dcc.Tab(label='Map', value='tab-1'),
           dcc.Tab(label='Graph', value='tab-2'),

        ]),




        html.Div(id='tabs-content'),
        html.Div(id='map-update'),





], style={'padding-top':'50px'})



@app.callback(
        Output("flat_type,"children"),
        [Input("town_id", "value")]
)
def active(value):

    if value == 'Ang Mo Kio':
        return  html.Div(  children=[
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'1 Room',       'value':'1 Room'},
                            {'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},])])

    elif value =='Bedok':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},])
                            ])

    elif value =='Bishan':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [

                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            {'label':'Multi Generation',    'value':'Multi Generation'},

                            ])
                            ])
    elif value =='Bukit Batok':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},])
                            ])


    elif value =='Bukit Merah':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'1 Room',       'value':'1 Room'},
                            {'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            ])
                            ])


    elif value =='Bukit Panjang':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            ])
                            ])

    elif value =='Bukit Timah':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            ])
                            ])


    elif value =='Central Area':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            ])
                            ])


    elif value =='Choa Chu Kang':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            ])
                            ])

    elif value =='Clementi':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            ])
                            ])


    elif value =='Geylang':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            ])
                            ])


    elif value =='Hougang':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            ])
                            ])

    elif value =='Jurong East':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [ {'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            ])
                            ])


    elif value =='Jurong West':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            ])
                            ])


    elif value =='Kallang/Whampoa':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            ])
                            ])

    elif value =='Lim Chu Kang':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            ])
                            ])


    elif value =='Marine Parade':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            ])])


    elif value =='Pasir Ris':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},])])

    elif value =='Punggol':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),

        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},])])


    elif value =='Queenstown':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},])])


    elif value =='Sembawang':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},])])







    elif value =='Sengkang':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},])])


    elif value =='Serangoon':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},])])


    elif value =='Tampines':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            {'label':'Multi Generation',    'value':'Multi Generation'},])])

    elif value =='Toa Payoh':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},])
                            ])


    elif value =='Woodlands':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},])])


    elif value =='Yishun':
        return  html.Div(  children=  [
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(
                options = [{'label':'2 Room',       'value':'2 Room'},
                            {'label':'3 Room',       'value':'3 Room'},
                            {'label':'4 Room',       'value':'4 Room'},
                            {'label':'5 Room',       'value':'5 Room'},
                            {'label':'Executive',    'value':'Executive'},
                            {'label':'Multi Generation',    'value':'Multi Generation'},
                            ])
                            ])







@app.callback(
        Output("txt","children"),
        [Input("dd","value")]
        )

def update(value):

    return 'The  Value is: "{}"'.format(value),


@app.callback(
        Output("map","srcDoc"),
        [Input("dd","value")]
        )
def makeMap(value):
    val = value
    print(val)
    cord = mapApi.searchCord(val)
    print(cord)  #cordinates
    m = folium.Map(location=cord, zoom_start=15)
    folium.Choropleth(  geo_data = geo_file,
                        fill_color='BuPu',
                        fill_opacity=0.8,
                        line_opacity=0.5,
                        data = flatData,
                        key_on = 'feature.properties.PLN_AREA_N',
                        columns = ['town','resale_price']
                        ).add_to(m)

    #map.save('map2.html')
    folium.Marker(location=[cord[0],cord[1]], fill_color = '#43d9de', radius = 8 ).add_to(m)
    m.save('map.html')
    return open('map.html','r').read()
    #return html.Div()



@app.callback(
    Output('tabs-content','children'),
    [Input('tabs','value')])




def render_content(tab):
    if tab == 'tab-1':
        return html.Div([



                        html.H3('Tab content 1'),


                #################################################################
                #                  SELECTION OPTIONS                            #
                #################################################################


                    html.Div([

                                    html.Label('Select an area: ', style={'color':"#FFFFFF"}),

                                    dcc.Dropdown(id='dd',value='Ang Mo Kio',
                                        options = [

                                            #{'label':i, 'value':i} for i in town

                                            {'label':'Ang Mo Kio',      'value':'Ang Mo Kio'},
                                            {'label':'Bedok',           'value':'Bedok'},
                                            {'label':'Bishan',          'value':'Bishan'},
                                            {'label':'Bukit Batok',     'value':'Bukit Batok'},
                                            {'label':'Bukit Merah',     'value':'Bukit Merah'},
                                            {'label':'Bukit Panjang',   'value':'Bukit Panjang'},
                                            {'label':'Bukit Timah',     'value':'Bukit Timah'},
                                            {'label':'Central Area',    'value':'Central Area'},
                                            {'label':'Choa Chu Kang',   'value':'Choa Chu Kang'},
                                            {'label':'Clementi',        'value':'Clementi'},
                                            {'label':'Geylang',         'value':'Geylang'},
                                            {'label':'Hougang',         'value':'Hougang'},
                                            {'label':'Jurong East',     'value':'Jurong East'},
                                            {'label':'Jurong West',     'value':'Jurong West'},
                                            {'label':'Kallang/Whampoa', 'value':'Kallang/Whampoa'},
                                            {'label':'Lim Chu Kang',    'value':'Lim Chu Kang'},
                                            {'label':'Marine Parade',   'value':'Marine Parade'},
                                            {'label':'Pasir Ris',       'value':'Pasir Ris'},
                                            {'label':'Punggol',         'value':'Punggol'},
                                            {'label':'Queenstown',      'value':'Queenstown'},
                                            {'label':'Sembawang',       'value':'Sembawang'},
                                            {'label':'Sengkang',        'value':'Sengkang'},
                                            {'label':'Serangoon',       'value':'Serangoon'},
                                            {'label':'Tampines',        'value':'Tampines'},
                                            {'label':'Toa Payoh',       'value':'Toa Payoh'},
                                            {'label':'Woodlands',       'value':'Woodlands'},
                                            {'label':'Yishun',          'value':'Yishun'},




                                        ],
                                        style = {
                                        #'position':'absolute',
                                        'width':'50%',
                                        'margin':'30px 5px 10px 5px'

                                        }
                                    ),

                                    html.Div(id = "txt", style={'color':"#FFFFFF"}),


                                    html.Button('Click Me!', id='btn-1', n_clicks_timestamp=0, style={'margin':'20px 5px 5px 5px', }),



                                    '''html.Div( children=[
                                    dcc.Slider(

                                         id='my-slider',
                                        min=0,
                                        max=20,
                                        step=0.5,
                                        value=10,


                                        ),
                                    ],
                                    style={
                                    'width':'30%',
                                    'padding':'10px',
                                    'margin':'30px 5px 10px 5px'
                                    },

                                    ),'''





                    ],
                    style={
                    'background-color': '#000000',
                    'width':'49.7%',
                    'display': 'inline-block',
                    'float':'left',

                    #'vertical-align': 'middle'
                    },
                    className = "six columns"),




                        html.Div(id='map-container',children=[

                            ## MAP ##

                            html.Iframe(id='map', srcDoc=open('map.html','r').read(), width='90%',height='600px',

                            style={
                                'max-width': '50%',
                                #'overflow':'auto',
                                'float':'right',
                                #'position':'relative',
                                'display': 'inline-block',


                                }),



                        ], style={
                            #'max-width': '50%',
                            #'overflow':'auto',
                            #'float':'right',
                            'margin':'5px 5px 10px 5px',


                        },className = "six columns"),








        ],className="row"  ),







    elif tab =='tab-2':
        return html.Div([
            html.H3('Tab content 2'),


            html.Div([

                html.Div([


                    html.Label('Select an area: ', style={'color':"#FFFFFF"}),

                    dcc.Dropdown(id='town_id', options = [
                    {'label':'Ang Mo Kio',      'value':'Ang Mo Kio'},
                    {'label':'Bedok',           'value':'Bedok'},
                    {'label':'Bishan',          'value':'Bishan'},
                    {'label':'Bukit Batok',     'value':'Bukit Batok'},
                    {'label':'Bukit Merah',     'value':'Bukit Merah'},
                    {'label':'Bukit Panjang',   'value':'Bukit Panjang'},
                    {'label':'Bukit Timah',     'value':'Bukit Timah'},
                    {'label':'Central Area',    'value':'Central Area'},
                    {'label':'Choa Chu Kang',   'value':'Choa Chu Kang'},
                    {'label':'Clementi',        'value':'Clementi'},
                    {'label':'Geylang',         'value':'Geylang'},
                    {'label':'Hougang',         'value':'Hougang'},
                    {'label':'Jurong East',     'value':'Jurong East'},
                    {'label':'Jurong West',     'value':'Jurong West'},
                    {'label':'Kallang/Whampoa', 'value':'Kallang/Whampoa'},
                    {'label':'Lim Chu Kang',    'value':'Lim Chu Kang'},
                    {'label':'Marine Parade',   'value':'Marine Parade'},
                    {'label':'Pasir Ris',       'value':'Pasir Ris'},
                    {'label':'Punggol',         'value':'Punggol'},
                    {'label':'Queenstown',      'value':'Queenstown'},
                    {'label':'Sembawang',       'value':'Sembawang'},
                    {'label':'Sengkang',        'value':'Sengkang'},
                    {'label':'Serangoon',       'value':'Serangoon'},
                    {'label':'Tampines',        'value':'Tampines'},
                    {'label':'Toa Payoh',       'value':'Toa Payoh'},
                    {'label':'Woodlands',       'value':'Woodlands'},
                    {'label':'Yishun',          'value':'Yishun'},]
                    ,
                    style = {
                    #'position':'absolute',
                    'width':'50%',
                    'margin':'30px 5px 10px 5px'

                    }
                    ),





                    html.Div(id='storage_room'),

                    html.Div(id = 'flat_type'),

                    html.Div(id='flat_model'),








                    ], style={
                        'background-color': '#000000',
                        'width':'49.7%',
                        'display': 'inline-block',
                        'float':'left',

                    }),

        ##### GRAPH + MAP  #####

            html.Div(id='graphic-container',children=[



                ## GRAPH ##



                    dcc.Graph(
                        figure = go.Figure(
                            data=[
                                go.Bar(
                                    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                                   y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                                   350, 430, 474, 526, 488, 537, 500, 439],
                                   name='Rest of world',
                                   marker=go.bar.Marker(
                                    color='rgb(55, 83, 109)')

                                )
                            ],

                            layout=go.Layout(
                            title='US Export of Plastic Scrap',
                            showlegend=True,
                            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                        ),

                    ), style={
                    #'max-width': '50%',
                    #'overflow':'auto',
                    #'float':'right',
                    'position':'relative',
                    'display': 'inline-block',
                    }

                        ),

            ], style={
                'margin':'5px 5px 10px 5px',

            }, className = "six columns"),



    ],  className="row"),









        ])




def get_town_cordinates():
    ''





app.run_server(debug=True)
