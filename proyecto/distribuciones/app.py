from flask import Flask
from dash import Dash,dcc,html,Input,Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from sklearn import datasets
from sklearn.cluster import KMeans
import plotly.graph_objs as go

external_stylesheets = ['https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css']

server = Flask(__name__)

app = Dash(
    __name__,
    server=server,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=external_stylesheets
)

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

distribuciones = ['Binomial','Geometrica','Normal']

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

switches = html.Div(
    [
        dbc.Label("Acumulada"),
        dbc.Checklist(
            options=[
                {"label": "Acumulada", "value": 1},
            ],
            value=[1],
            id="switches-input",
            switch=True,
        ),
    ]
)

controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("Distribución"),
                dcc.Dropdown(
                    id="x-variable",
                    options=[
                        {"label": col, "value": col} for col in distribuciones
                    ],
                    value="Binomial",
                ),
            ]
        ),
        html.Br(),
        switches,
        html.Br(),
        html.Div(
            [
                dbc.Label("Parámetros"),
                dbc.Input(id="n_value", placeholder="valor n", type="number", value=3),
                dbc.Input(id="p_value", placeholder="valor p", type="number", value=3),
                dbc.Input(id="x_value", placeholder="valor x", type="number", value=3)
            ]
        ),
        html.Br(),
        html.Div(
            [
                dbc.Button("CANCELAR", id="cancel_btn", color="danger", className="me-1", n_clicks=0),
                dbc.Button("ACEPTAR", id="aceptar_btn", color="success", className="me-1"),
            ],
            className="d-grid gap-2 d-md-block",
        )
    ],
    body=True,
)

app.layout = dbc.Container(
    [
        html.H1("Distribuciones"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(
                    dcc.Graph(
                        id='example-graph',
                        figure=fig
                    )
                    , md=8),
            ],
            align="center",
        ),
    ],
    fluid=True,
)

"""
app.layout = html.Div(
    children = [
        html.H6("Distribuciones"),

        html.Div([
            dcc.Dropdown(['Binomial', 'Normal', 'Exponencial', 'Trigonometrica'], placeholder="Selecciona una distribucion a calcular")
        ]),

        
        
        html.Div([
            "Input: ",
            dcc.Input(id='my-input', value='initial value', type='text')
        ]),
        html.Br(),
        html.Div(id='my-output'),        

        
        dcc.RadioItems(
            list(all_options.keys()),
            'America',
            id='countries-radio',
        ),
        
        html.Hr(),
        
        dcc.RadioItems(id='cities-radio'),
        
        html.Hr(),
        
        html.Div(id='display-selected-values'),

        html.Button(id='submit-button-state', n_clicks=0, children='ENTER'),

        
        
        dcc.Graph(
            id='example-graph',
            figure=fig
        )]
)
"""

"""

email_input = dbc.Row(
    [
        dbc.Label("Email", html_for="example-email-row", width=2),
        dbc.Col(
            dbc.Input(
                type="email", id="example-email-row", placeholder="Enter email"
            ),
            width=10,
        ),
    ],
    className="mb-3",
)

password_input = dbc.Row(
    [
        dbc.Label("Password", html_for="example-password-row", width=2),
        dbc.Col(
            dbc.Input(
                type="password",
                id="example-password-row",
                placeholder="Enter password",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)

radios_input = dbc.Row(
    [
        dbc.Label("Radios", html_for="example-radios-row", width=2),
        dbc.Col(
            dbc.RadioItems(
                id="example-radios-row",
                options=[
                    {"label": "First radio", "value": 1},
                    {"label": "Second radio", "value": 2},
                    {
                        "label": "Third disabled radio",
                        "value": 3,
                        "disabled": True,
                    },
                ],
            ),
            width=10,
        ),
    ],
    className="mb-3",
)



app.layout =  html.Div([
    dbc.Row([
        dbc.Card([
            dbc.CardBody([
                html.H2('Distribuciones')
            ])
        ], className='text-center')
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Dash Tabs component 1'),
                    html.Div([
                        dcc.Dropdown(['Binomial', 'Normal', 'Exponencial', 'Trigonometrica'], placeholder="Selecciona una distribucion a calcular")
                    ])
                ])
            ], className='text-center'),
            dbc.Form([email_input,password_input,radios_input])
        ], xs=4),
        dbc.Col([
            #hola
        ], xs=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Dash Tabs component 5')
                ], className='text-center')
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Dash Tabs component 6')
                        ], className='text-center')
                    ])
                ], xs=6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Dash Tabs component 7')
                        ], className='text-center')
                    ])
                ], xs=6)
            ], className='pt-1')
        ], xs=4)
    ], className='p-2 align-items-stretch'),
    # content
])
"""

@app.callback([Input("cancel_btn","n_clicks")])
def on_cancel_click(n):
    print(n)

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value'),
    Input('submit-button-state', 'n_clicks')
)
def update_output_div(input_value):
    print(input_value)
    print(input_value)
    print(input_value)
    return f'Output: {input_value}'

@app.callback(
    Output('cities-radio', 'options'),
    Input('countries-radio', 'value'))
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    Output('cities-radio', 'value'),
    Input('cities-radio', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value'))
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country,
    )

@server.route('/')
@server.route('/index')
def principal():
    return app.index()

server.run(host='0.0.0.0', port=5000, debug=True)
