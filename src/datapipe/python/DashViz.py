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
import pickle
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
import numpy as np


'''             Directly Load the data in dataframe, chek and reload to make sure its there      '''



from API import get_all

#df  = get_all()
df = pd.read_csv('resale_flat_prices.csv')
#print(df.tail())
#print(df.head())

#town = df.town.unique()
#street = df.street_name.unique()
print(df.flat_model.unique())
df['town'] = le.fit_transform(df['town'])
df['flat_type'] = le.fit_transform(df['flat_type'])
df['storey_range'] = le.fit_transform(df['storey_range'])
df['flat_model'] = le.fit_transform(df['flat_model'])
print(df.flat_model.unique())

##Init model
filename = 'model1.h5'
infile = open(filename,'rb')
modelPred = pickle.load(infile)
infile.close()












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



## Flat type ##

@app.callback(
        Output("flat_type","children"),
        [Input("town_id", "value")]
)
def active(value):

        return  html.Div(  children=[
        html.Label('Select Flat type: ', style={'color':"#FFFFFF"}),
        dcc.Dropdown(id='ft',
                options = [{'label':'1 Room',               'value':'0'},
                            {'label':'2 Room',              'value':'1'},
                            {'label':'3 Room',              'value':'2'},
                            {'label':'4 Room',              'value':'3'},
                            {'label':'5 Room',              'value':'4'},
                            {'label':'Multi Generation',    'value':'6'},
                            {'label':'Executive',           'value':'5'},]
                            )
                            ])

# 'town', 'storey_range', 'flat_type', 'flat_model', 'floor_area_sqm', 'lease_commence_date', 'age'

@app.callback(
    Output("flat_model","children"),
    [Input("town_id","value")]
)

def activeModel(value):
    print(value)
    return  html.Div(  children=[
    html.Label('Select Flat model: ', style={'color':"#FFFFFF"}),
    dcc.Dropdown(id='fm',
            options = [{'label':'Improved',                 'value':'8'},
                        {'label':'New Generation',          'value':'20'},
                        {'label':'DBSS',                    'value':'5'},
                        {'label':'Standard',                'value':'29'},
                        {'label':'Apartment',               'value':'4'},
                        {'label':'Simplified',              'value':'28'},
                        {'label':'Model A',                 'value':'15'},
                        {'label':'Maisonette',              'value':'14'},
                        {'label':'Premium Apartment',       'value':'22'},
                        {'label':'Adjoined flat',           'value':'3'},
                        {'label':'Model A-Maisonette',      'value':'16'},
                        {'label':'Type S1',                 'value':'32'},
                        {'label':'Type S2',                 'value':'33'},
                        {'label':'Model A2',                'value':'17'},
                        {'label':'Terrace',                 'value':'31'},
                        {'label':'Improved-Maisonette',     'value':'9'},
                        {'label':'Premium Maisonette',      'value':'25'},
                        {'label':'Multi Generation',        'value':'18'},
                        {'label':'Premium Apartment Loft',  'value':'23'},
                        {'label':'Premium Apartment',       'value':'24'},
                        {'label':'2-room',                  'value':'1'},


                        ])
                        ])

@app.callback(
        Output("storey_range","children"),
        [Input("town_id", "value")]
)

def activeStorey(value):
    return  html.Div(  children=[
    html.Label('Select Storey Range: ', style={'color':"#FFFFFF"}),
    dcc.Dropdown(id='sr',
            options = [{'label':'01 TO 03',         'value':'0'},
                        {'label':'01 TO 05',        'value':'1'},
                        {'label':'04 TO 06',        'value':'2'},
                        {'label':'06 TO 10',        'value':'3'},
                        {'label':'07 TO 09',        'value':'4'},
                        {'label':'10 TO 12',        'value':'5'},
                        {'label':'11 TO 15',        'value':'6'},
                        {'label':'13 TO 15',        'value':'7'},
                        {'label':'16 TO 18',        'value':'8'},
                        {'label':'16 TO 20',        'value':'9'},
                        {'label':'19 TO 21',        'value':'10'},
                        {'label':'21 TO 25',        'value':'11'},
                        {'label':'22 TO 24',        'value':'12'},
                        {'label':'25 TO 27',        'value':'13'},
                        {'label':'26 TO 30',        'value':'14'},
                        {'label':'28 TO 30',        'value':'15'},
                        {'label':'31 TO 33',        'value':'16'},
                        {'label':'31 TO 35',        'value':'17'},
                        {'label':'34 TO 36',        'value':'18'},
                        {'label':'36 TO 40',        'value':'29'},
                        {'label':'37 TO 39',        'value':'20'},
                        {'label':'40 TO 42',        'value':'21'},
                        {'label':'43 TO 45',        'value':'22'},
                        {'label':'46 TO 48' ,       'value':'23'},
                        {'label':'49 TO 51',        'value':'24'},


                        ])
                        ])




@app.callback(
        Output("lease_commence_date","children"),
        [Input("town_id", "value")]
)

def activeDate(value):
    return  html.Div(  children=[
    html.Label('Select Lease Commence Date: ', style={'color':"#FFFFFF"}),
    dcc.Dropdown(id='lc',
            options = [ {'label':'1966',        'value':'1966'},
                        {'label':'1967',        'value':'1967'},
                        {'label':'1968',        'value':'1968'},
                        {'label':'1969',        'value':'1969'},
                        {'label':'1970',        'value':'1970'},
                        {'label':'1971',        'value':'1971'},
                        {'label':'1972',        'value':'1972'},
                        {'label':'1973',        'value':'1973'},
                        {'label':'1974',        'value':'1974'},
                        {'label':'1975',        'value':'1975'},
                        {'label':'1976',        'value':'1976'},
                        {'label':'1977',        'value':'1977'},
                        {'label':'1978',        'value':'1978'},
                        {'label':'1979',        'value':'1979'},
                        {'label':'1980',        'value':'1980'},
                        {'label':'1981',        'value':'1981'},
                        {'label':'1982',        'value':'1982'},
                        {'label':'1983',        'value':'1983'},
                        {'label':'1984',        'value':'1984'},
                        {'label':'1985',        'value':'1985'},
                        {'label':'1986',        'value':'1986'},
                        {'label':'1987',        'value':'1987'},
                        {'label':'1988',        'value':'1988'},
                        {'label':'1989' ,       'value':'1989'},
                        {'label':'1990',        'value':'1990'},
                        {'label':'1991',        'value':'1991'},
                        {'label':'1992',        'value':'1992'},
                        {'label':'1993',        'value':'1993'},
                        {'label':'1994',        'value':'1994'},
                        {'label':'1995',        'value':'1995'},
                        {'label':'1996',        'value':'1996'},
                        {'label':'1997',        'value':'1997'},
                        {'label':'1998',        'value':'1998'},
                        {'label':'1999',        'value':'1999'},
                        {'label':'2000' ,       'value':'2000'},
                        {'label':'2001',        'value':'2001'},
                        {'label':'2002',        'value':'2002'},
                        {'label':'2003',        'value':'2003'},
                        {'label':'2004',        'value':'2004'},
                        {'label':'2005',        'value':'2005'},
                        {'label':'2006',        'value':'2006'},
                        {'label':'2007' ,       'value':'2007'},
                        {'label':'2008',        'value':'2008'},
                        {'label':'2009',        'value':'2009'},
                        {'label':'2010',        'value':'2010'},
                        {'label':'2011',        'value':'2011'},
                        {'label':'2012',        'value':'2012'},
                        {'label':'2013',        'value':'2013'},
                        {'label':'2014',        'value':'2014'},
                        {'label':'2015',       'value':'2015'},
                        {'label':'2016',       'value':'2016'},

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


##BUTTON ->
@app.callback(
    Output('container-button-basic', 'children'),
    [
    Input('button','n_clicks'),
    Input('town_id','value'),
    Input('sr','value'),
    Input('ft','value'),
    Input('fm','value'),
    #floor area sqm - 0
    Input('lc','value'),
    # age - 0
    ],

)

def update_output(n_clicks,value, value1, value2, value3,value4):
    if n_clicks is not None:
        town = int(value)
        storey = int(value1)
        type = int(value2)
        model = int(value3)
        floor = 50
        lease = int(value4)
        age = 50


        arr = np.array([[town, storey, type, model, floor, lease, age]])
        arr.reshape(-1,1)
        prediction = modelPred.predict(arr)

        print('click: {} , Value: {} {} {} {} {} , Prediction: {}'.format(
            n_clicks,
            town,
            value1,
            value2,
            value3,
            value4,
            prediction
        ))


        return 'The Real price is:  {}'.format(prediction)




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
                            'margin':'5px 5px 10px 5px',


                        },className = "six columns"),

        ],className="row"  ),







    elif tab =='tab-2':
        return html.Div([
            html.H3('Tab content 2'),


            html.Div([

                html.Div([


                    html.Label('Select an area: ', style={'color':"#FFFFFF",'margin':'10px 20px 10px 10px'}),

                    dcc.Dropdown(id='town_id', options = [
                    {'label':'Ang Mo Kio',      'value':'0'},
                    {'label':'Bedok',           'value':'1'},
                    {'label':'Bishan',          'value':'2'},
                    {'label':'Bukit Batok',     'value':'3'},
                    {'label':'Bukit Merah',     'value':'4'},
                    {'label':'Bukit Panjang',   'value':'5'},
                    {'label':'Bukit Timah',     'value':'6'},
                    {'label':'Central Area',    'value':'7'},
                    {'label':'Choa Chu Kang',   'value':'8'},
                    {'label':'Clementi',        'value':'9'},
                    {'label':'Geylang',         'value':'10'},
                    {'label':'Hougang',         'value':'11'},
                    {'label':'Jurong East',     'value':'12'},
                    {'label':'Jurong West',     'value':'13'},
                    {'label':'Kallang/Whampoa', 'value':'14'},
                    {'label':'Lim Chu Kang',    'value':'15'},
                    {'label':'Marine Parade',   'value':'16'},
                    {'label':'Pasir Ris',       'value':'17'},
                    {'label':'Punggol',         'value':'18'},
                    {'label':'Queenstown',      'value':'19'},
                    {'label':'Sembawang',       'value':'20'},
                    {'label':'Sengkang',        'value':'21'},
                    {'label':'Serangoon',       'value':'22'},
                    {'label':'Tampines',        'value':'23'},
                    {'label':'Toa Payoh',       'value':'24'},
                    {'label':'Woodlands',       'value':'25'},
                    {'label':'Yishun',          'value':'26'},]
                    ,
                    style = {
                    #'position':'absolute',
                    'width':'50%',
                    'margin':'10px 5px 10px 5px'

                    }
                    ),





                    html.Div(id='storey_range',style={'width':'25%','margin':'30px 5px 10px 5px'}),

                    html.Div(id = 'flat_type',style={'width':'25%','margin':'30px 5px 10px 5px','float':'right','display': 'inline-block',}),

                    html.Div(id='flat_model',style={'width':'25%','margin':'30px 5px 10px 5px','display': 'inline-block',}),

                    html.Div(id = 'lease_commence_date',style={'width':'25%','margin':'30px 5px 10px 5px','float':'right','display': 'inline-block',}),

                    html.Button('Submit',id='button',style={'background-color': '#FFFFFF','margin':'30px 5px 10px 5px','float':'right','display': 'inline-block',}),

                    html.Div(id='container-button-basic',
                    children='Enter a value and press submit',style={'background-color': '#FFFFFF','margin':'30px 5px 10px 5px','float':'right','display': 'inline-block',}),



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





app.run_server(debug=True)
