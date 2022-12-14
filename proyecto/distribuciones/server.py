from dash import Dash,dcc,html,Input,Output,State
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

distribuciones = ['Binomial','Poisson','Geometrica','Exponencial','Normal']

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

type_distribution = html.Div(
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
        html.Div(id='distribucion_elegida')
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

parameters_binomial = html.Div(
    [
        dbc.Label("Parámetros"),
        dbc.Input(id="binom_valor_n", placeholder="valor n", type="number"),
        dbc.Input(id="binom_valor_p", placeholder="valor p", type="number"),
        dbc.Input(id="binom_valor_x", placeholder="valor x", type="number")
    ], style= {'display': 'none'}, id='parameters_binomial'
)

parameters_poisson = html.Div(
    [
        dbc.Label("Parámetros"),
        dbc.Input(id="pois_valor_mu", placeholder="valor mu", type="number"),
        dbc.Input(id="pois_valor_x", placeholder="valor x", type="number")
    ], style= {'display': 'none'}, id='parameters_poisson'
)

parameters_geometrica = html.Div(
    [
        dbc.Label("Parámetros"),
        dbc.Input(id="geom_valor_p", placeholder="valor p", type="number"),
        dbc.Input(id="geom_valor_x", placeholder="valor x", type="number")
    ], style= {'display': 'none'}, id='parameters_geometrica'
)

parameters_exponencial = html.Div(
    [
        dbc.Label("Parámetros"),
        dbc.Input(id="exp_valor_alpha", placeholder="valor alpha", type="number"),
        dbc.Input(id="exp_valor_x", placeholder="valor x", type="number")
    ], style= {'display': 'none'}, id='parameters_exponencial'
)

parameters_normal = html.Div(
    [
        dbc.Label("Parámetros"),
        dbc.Input(id="norm_valor_mu", placeholder="valor mu", type="number"),
        dbc.Input(id="norm_valor_sigma", placeholder="valor sigma", type="number"),
        dbc.Input(id="norm_valor_x", placeholder="valor x", type="number")
    ], style= {'display': 'none'}, id='parameters_normal'
)

actions_buttons = html.Div(
    [
        dbc.Button("CANCELAR", id="cancel_btn", color="danger", className="me-1", n_clicks=0),
        dbc.Button("ACEPTAR", id="aceptar_btn", color="success", className="me-1", n_clicks=0),
        html.Span(id="example-output", style={"verticalAlign": "middle","display":"none"}),
    ],
    className="d-grid gap-2 d-md-block",
)

#Tarjeta con todos los elementos
controls = dbc.Card(
    [
        type_distribution,
        html.Br(),
        switches,
        html.Br(),
        parameters_binomial,
        parameters_poisson,
        parameters_geometrica,
        parameters_exponencial,
        parameters_normal,
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

@app.callback(
    Output('parameters_binomial', 'style'),
    Output('parameters_poisson', 'style'),
    Output('parameters_geometrica', 'style'),
    Output('parameters_exponencial', 'style'),
    Output('parameters_normal', 'style'),
    [Input(component_id='tipo_distribucion', component_property='value')])
def show_hide_element(value):
    if value == 'Binomial':
        return {'display':'block'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'}
    elif value == 'Poisson':
        return {'display':'none'},{'display':'block'},{'display':'none'},{'display':'none'},{'display':'none'}
    elif value == 'Geometrica':
        return {'display':'none'},{'display':'none'},{'display':'block'},{'display':'none'},{'display':'none'}
    elif value == 'Exponencial':
        return {'display':'none'},{'display':'none'},{'display':'none'},{'display':'block'},{'display':'none'}
    elif value == 'Normal':
        return {'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'block'}
    else:
        return {'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'}

    

@app.callback(
    Output('distribucion_elegida', 'children'),
    Input('tipo_distribucion', 'value')
)
def update_output(value):
    return f'You have selected {value}'

#Callback del boton CANCELAR
@app.callback(
    Output('acumulada_switch','value'),
    Output('binom_valor_n','value'),
    Output('binom_valor_p','value'),
    Output('binom_valor_x','value'),
    Output('pois_valor_mu','value'),
    Output('pois_valor_x','value'),
    Output('geom_valor_p','value'),
    Output('geom_valor_x','value'),
    Output('exp_valor_alpha','value'),
    Output('exp_valor_x','value'),
    Output('norm_valor_mu','value'),
    Output('norm_valor_sigma','value'),
    Output('norm_valor_x','value'),
    [Input('cancel_btn', 'n_clicks')]
    
)
def on_cancel_click(n):
    if n is None:
        return "Not clicked."
    else:
        return False,'','','','','','','','','','','',''

#Callback del buton ACEPTAR
#El output debe ser la grafica
@app.callback(
    Output('example-output', 'children'),
    Input('aceptar_btn', 'n_clicks'),
    State('tipo_distribucion','value'),
    State('acumulada_switch', 'value'),
    State('binom_valor_n','value'),
    State('binom_valor_p','value'),
    State('binom_valor_x','value'),
    State('pois_valor_mu','value'),
    State('pois_valor_x','value'),
    State('geom_valor_p','value'),
    State('geom_valor_x','value'),
    State('exp_valor_alpha','value'),
    State('exp_valor_x','value'),
    State('norm_valor_mu','value'),
    State('norm_valor_sigma','value'),
    State('norm_valor_x','value'),
)
def on_accept_click(n,tipo_distribucion,acumulada_switch,
                    binom_valor_n,binom_valor_p,binom_valor_x,
                    pois_valor_mu,pois_valor_x,
                    geom_valor_p,geom_valor_x,
                    exp_valor_alpha,exp_valor_x,
                    norm_valor_mu,norm_valor_sigma,norm_valor_x
                    ):
    if n <= 0:
        return "Not clicked."
    else:
        print(tipo_distribucion)
        if tipo_distribucion == 'Binomial':
            print(acumulada_switch)
            print(binom_valor_n)
            print(binom_valor_p)
            print(binom_valor_x)
        elif tipo_distribucion == 'Poisson':
            print(acumulada_switch)
            print(pois_valor_mu)
            print(pois_valor_x)
        elif tipo_distribucion == 'Geometrica':
            print(geom_valor_p)
            print(geom_valor_x)
        elif tipo_distribucion == 'Exponencial':
            print(exp_valor_alpha)
            print(exp_valor_x)
        elif tipo_distribucion == 'Normal':
            print(norm_valor_mu)
            print(norm_valor_sigma)
            print(norm_valor_x)
        return None

    #Regresar aqui el grafico
    #Regresar aqui el grafico
    #Regresar aqui el grafico
    
app.run(host='0.0.0.0', port=8080, debug=True)
