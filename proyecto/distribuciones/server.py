from dash import Dash,dcc,html,Input,Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

external_stylesheets = ['https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css']

app = Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=external_stylesheets
)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

distribuciones = ['Binomial','Geometrica','Normal']

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

type_distrobution = html.Div(
    [
        dbc.Label("Distribución"),
        #para la accion del dropdown se deben de pedir los parametros
        dcc.Dropdown(
            id="tipo_distribucion",
            options=[
                {"label": col, "value": col} for col in distribuciones
            ],
            value="Binomial",
        ),
    ]
)

switches = html.Div(
    [
        dbc.Label("Acumulada"),
        dbc.Switch(
            id="acumulada_switch",
            value=False,
        ),
    ]
)

parameters = html.Div(
    [
        dbc.Label("Parámetros"),
        dbc.Input(id="valor_n", placeholder="valor n", type="number", value=3),
        dbc.Input(id="valor_p", placeholder="valor p", type="number", value=3),
        dbc.Input(id="valor_x", placeholder="valor x", type="number", value=3)
    ]
)

actions_buttons = html.Div(
    [
        dbc.Button("CANCELAR", id="cancel_btn", color="danger", className="me-1", n_clicks=0),
        dbc.Button("ACEPTAR", id="aceptar_btn", color="success", className="me-1", n_clicks=0),
        html.Span(id="example-output", style={"verticalAlign": "middle"}),
    ],
    className="d-grid gap-2 d-md-block",
)

#Tarjeta con todos los elementos
controls = dbc.Card(
    [
        type_distrobution,
        html.Br(),
        switches,
        html.Br(),
        parameters,
        html.Br(),
        actions_buttons
    ],
    body=True,
)


generate_graph = dcc.Graph(
    id='example-graph',
    figure=fig
)

#contenedor principal
app.layout = dbc.Container(
    [
        html.H1("Distribuciones"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(
                    generate_graph
                    , md=8),
            ],
            align="center",
        ),
    ],
    fluid=True,
)

#Callback del boton CANCELAR
@app.callback(
    Output('acumulada_switch','value'),
    Output('valor_n','value'),
    Output('valor_p','value'),
    Output('valor_x','value'),
    [Input('cancel_btn', 'n_clicks')]
    
)
def on_cancel_click(n):
    if n is None:
        return "Not clicked."
    else:
        return False,'','',''

#Callback del buton ACEPTAR
@app.callback(
    Output('example-output', 'children'),
    [
        Input('aceptar_btn', 'n_clicks'),
        Input('valor_n','value'),
        Input('valor_p','value'),
        Input('valor_x','value')
     ]
)
def on_accept_click(n,valor_n,valor_p,valor_x):
    if n is None:
        return "Not clicked."
    else:
        print(valor_n)
        print(valor_p)
        print(valor_x)
        return f"Clicked {n} times."
    
app.run(host='0.0.0.0', port=8080, debug=True)
