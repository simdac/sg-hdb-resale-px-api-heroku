import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input,Output
import folium
from DB_Use import *
import requests
from requests.models import PreparedRequest
import pandas as pd



#

'''        SET UP CONNECTION TO DATABASE           '''
req = PreparedRequest()
mysql = MYSQL()

def set_data():
    sql = mysql.head(10)

    sqlCmd = {"sql":sql}
    website = 'https://localhost/connection_mysqli.php';
    req.prepare_url(website,sqlCmd)
    line = requests.get(req.url, verify = False).text
    txt = line.split()

    df = pd.DataFrame(get_data(txt),columns = get_headers(txt))
    #df['resale_price'] = df['resale_price'].astype(int)
    #data = df['resale_price'] < 250000
    #print(df[data])
    #print(df)
    #print(df.info())






'''      MAKE A DASHBORD AND CONNECT DATA CALLING, Check box to set the limit value to display the number of data
                                                    Data points represented on the map?
                                                    A graph below the map showing the data stuff?'''




'''       BUILD WEBSITE      '''

#Starting cordinates for folium
cord = (1.3264301001450307,103.80014894530179)

external_stylesheets = ['https://codepen.io/chriddpy/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

app.layout = html.Div(children=[

    html.H1(children='Resale HDB Price App',
        style={
            'textAlign':'center'
        }
    ),



    dcc.Tabs(id='tabs',value='tab-1',children=[
        dcc.Tab(label='Tab 1', value='tab-1'),
        dcc.Tab(label='Tab 2', value='tab-2'),

    ]),




    html.Div(id='tabs-content'),



##### GRAPH + MAP  #####

    html.Div(id='graphic-container',children=[



        ## MAP ##


        html.Iframe(id='map', srcDoc=open('map.html','r').read(), width='100%',height='600px',

        style={
            'max-height':'50%',
            'position':'relative',
            'float':'right',

        }),


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
            'position':'relative',
            'float':'right',
            }

                ),

    ], style={
        'overflow':'auto',
        'max-width': '50%',
        'float':'right',
    }),











    html.Label('Dropdown'),

    dcc.Dropdown(id='dd',
        options = [



            {'label':'New York City', 'value':'NY'},
            {'label':'Bishun', 'value':'BIN'},
            {'label':'Hillview', 'value':'HV'},
            {'label':'Gelang', 'value':'Glng'},



        ],
        value='NY',
        style = {
        #'position':'absolute',
        'width':'50%',

        }
    ),








    html.Div( children=[
    dcc.Slider(

        min=0,
        max=10,
        marks={i: '{}'.format(i *10 ) for i in range(11)},
        value=5,
        ),
    ],
    style={
    'width':'25%',
    'padding':'10px'
    },

    ),
     html.Button('Click Me!', id='btn-1', n_clicks_timestamp=0),



], style={'padding-top':'50px'})












@app.callback(
    Output('tabs-content','children'),
    [Input('tabs','value')])




def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab =='tab-2':
        return html.Div([
            html.H3('Table content 2')
        ])

#def plot_data():


def get_dropdown_data():
    for i in range(0,len(df.columns)):
        print(df['town'].unique)

#def update_graph():



app.run_server(debug=True)
