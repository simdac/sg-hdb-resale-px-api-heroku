import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input,Output



pd.set_option('display.max_columns', None)


#Read CSV data
df = pd.read_csv('resale_flat_prices.csv')


def clear_col():
    clear_cols = [(col.replace("_"," "))for col in df.columns]
    df.columns = clear_cols
    return df.columns

def generate_table(dataframe, max_rows =10):

    dataframe.columns = clear_col()
    print(df.head())


    return html.Table(

        #Header
        [html.Tr([html.Th(col)for col in dataframe.columns])] +

        [html.Tr([
                html.Td(dataframe.iloc[i][cols]) for cols in dataframe.columns
                ]) for i in range(min(len(dataframe),max_rows))],
        style={

        'border-spacing': '50px',
        'border-collapse': 'seperate',
        'table-layout': 'fixed',


        #'width': '100%',
        'margin': '20px auto',
        'text-align': 'left',
        'border-spacing': '50px 0'
        }



    )



#Set up dash
external_stylesheets = ['https://codepen.io/chriddpy/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

colors={
'background':'#111111',
'text':'#7FDBFF'
}

app.layout = html.Div(children=[
    html.H4(children='Resale Flat price',
        style={
            'textAlign':'center'
        }
    ),


    #generate_table(df),

    html.Label('Dropdown'),

    dcc.Dropdown(
        options = [
            {'label':'New York City', 'value':'NY'},
            {'label':'Bishun', 'value':'BIN'},
            {'label':'Hillview', 'value':'HV'},
            {'label':'Gelang', 'value':'Glng'},



        ],
        value='NY',
        style = {
        'width':'50%'
        }
    ),

    html.Label('Multi select Dropdown'),

    dcc.Dropdown(
        options = [

            {'label':'New York City', 'value':'NY'},
            {'label':'Bishun', 'value':'BIN'},
            {'label':'Hillview', 'value':'HV'},
            {'label':'Gelang', 'value':'Glng'},

        ],
        value='NY',
        multi = True,
        style = {
        'width':'50%'
        }
    ),

    html.Label('Checkboxes'),

    dcc.Checklist(
        options=[
        {'label':'New York City', 'value':'NY'},
        {'label':'Bishun', 'value':'BIN'},
        {'label':'Hillview', 'value':'HV'},
        {'label':'Gelang', 'value':'Glng'},
        ]
    ),

    html.Label('Radio Items'),

    dcc.RadioItems(
        options=[
        {'label':'New York City', 'value':'NY'},
        {'label':'Bishun', 'value':'BIN'},
        {'label':'Hillview', 'value':'HV'},
        {'label':'Gelang', 'value':'Glng'},
        ]

    ),


    html.Label('Text Input'),
    dcc.Input(id = 'input-id',value = 'NY', type='text'),
    html.Div(id = 'div-id'),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 0 else str(i) for i in range(0, 10)},
        value=5,


    ),



])

##Implement callback

@app.callback(
    Output(component_id='div-id', component_property = 'children'),
    [Input(component_id='input-id',component_property = 'value')]

)



def update_output(input_value):
    return 'You entered "{}"'.format(input_value)

app.run_server(debug=True)

'''dcc.Graph(
        id='live',
        figure={
            'data':[
                go.Scatter(
                    x    = df[df['town'] == i ] ['resale price'],
                    y    = df[df['town'] == i ] ['floor area sqm'],
                    text = df['town'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size':15,
                        'line': {'width':0.5, 'color':'white'}

                    },
                    name = i


                )for i in df.loc[0:10, 'town'].unique()
            ],
            'layout': go.Layout(
                xaxis={'title':'Resale Price'},
                yaxis={'title':'Floor Area Sqm'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'

            )

        }
    ),'''


'''app.layout = html.Div(children=[

                                html.H1(children='Resale Flat Prices',
                                style={
                                'textAlign':'center',
                                'color':colors['text']

                                }),


                                html.Div(children='Dash Application framework for python',
                                style={
                                'textAlign':'center',
                                'color':colors['text']

                                }

                                ),


                                dcc.Graph(
                                    id='example graph',
                                    figure={
                                        'data':[
                                            {'x':[1,2,4,3], 'y':[1,4,6,2], 'type': 'bar','name':'SF'},
                                            {'x':[23,5,12,6],'y':[12,3,12,4],'type':'bar','name':'Montereal'},

                                        ],
                                    'layout':{
                                        'title':'Dash vizual',
                                        'plot_bgcolor':colors['background'],
                                        'paper_bgcolor':colors['background'],
                                        'font':{
                                            'color':colors['text']

                                        }

                                    }

                            }
                    )














html.Label('Multi select Dropdown'),

dcc.Dropdown(id='dd2',
    options = [

        {'label':'New York City', 'value':'NY'},
        {'label':'Bishun', 'value':'BIN'},
        {'label':'Hillview', 'value':'HV'},
        {'label':'Gelang', 'value':'Glng'},

    ],
    value='NY',
    multi = True,
    style = {

    'width':'50%'
    }
),

html.Label('Checkboxes'),

dcc.Checklist(
    options=[
    {'label':'New York City', 'value':'NY'},
    {'label':'Bishun', 'value':'BIN'},
    {'label':'Hillview', 'value':'HV'},
    {'label':'Gelang', 'value':'Glng'},
    ]
),

html.Label('Radio Items'),

dcc.RadioItems(
    options=[
    {'label':'New York City', 'value':'NY'},
    {'label':'Bishun', 'value':'BIN'},
    {'label':'Hillview', 'value':'HV'},
    {'label':'Gelang', 'value':'Glng'},
    ]

),


html.Label('Text Input'),
dcc.Input(id = 'input-id',value = 'NY', type='text'),
html.Div(id = 'div-id'),


















             ])'''
