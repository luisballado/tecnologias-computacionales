from dash import Dash,dcc,html,Input,Output,State
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc

from distribuciones import *

external_stylesheets = ['https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css']

distribuciones = ['Binomial','Poisson','Geometrica','Exponencial','Normal']

app = Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=external_stylesheets
)

d = DistribucionFactory()


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
    id='distribution-graph'
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
    Output('distribution-graph', 'figure'),
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
        #Crear un grafico vacio
        df = pd.DataFrame({})
        return go.Figure(df)
        
    else:
        print(tipo_distribucion)
        if tipo_distribucion == 'Binomial':
            print(acumulada_switch)
            print(binom_valor_n)
            print(binom_valor_p)
            print(binom_valor_x)

            datos = {}
            datos['n'] = binom_valor_n
            datos['p'] = binom_valor_p
            datos['x'] = binom_valor_x

            binomial = d.getDistribution("Binomial",datos)
            
            df = pd.DataFrame(binomial.get_sample(binom_valor_x),columns=['n_gen'])
            df['pdf'] = df['n_gen'].apply(lambda x: binomial.get_probability(x))

            return go.Figure(data=[go.Scatter(x=df['n_gen'],y=df['pdf'])])
            
            
        elif tipo_distribucion == 'Poisson':
            print(acumulada_switch)
            print(pois_valor_mu)
            print(pois_valor_x)
            
            datos = {}
            datos['mu'] = pois_valor_mu
            datos['x'] = pois_valor_x
            
            poisson = d.getDistribution("Poisson",datos)
            
            df = pd.DataFrame(poisson.get_sample(pois_valor_x),columns=['n_gen'])
            df['pdf'] = df['n_gen'].apply(lambda x: poisson.get_probability(x))

            return go.Figure(data=[go.Scatter(x=df['n_gen'],y=df['pdf'])])
            
        elif tipo_distribucion == 'Geometrica':
            print(geom_valor_p)
            print(geom_valor_x)

            datos = {}
            datos['p'] = geom_valor_p
            datos['x'] = geom_valor_x
            
            geometrica = d.getDistribution("Geometrica",datos)
            
            df = pd.DataFrame(geometrica.get_sample(geom_valor_x),columns=['n_gen'])
            df['pdf'] = df['n_gen'].apply(lambda x: geometrica.get_probability(x))

            return go.Figure(data=[go.Scatter(x=df['n_gen'],y=df['pdf'])])
            
        elif tipo_distribucion == 'Exponencial':
            print(exp_valor_alpha)
            print(exp_valor_x)

            datos = {}
            datos['alpha'] = exp_valor_alpha
            datos['x'] = exp_valor_x
            
            exponencial = d.getDistribution("Exponencial",datos)
            
            df = pd.DataFrame(exponencial.get_sample(exp_valor_x),columns=['n_gen'])
            df['pdf'] = df['n_gen'].apply(lambda x: exponencial.get_probability(x))

            return go.Figure(data=[go.Scatter(x=df['n_gen'],y=df['pdf'])])
            
        elif tipo_distribucion == 'Normal':
            print(norm_valor_mu)
            print(norm_valor_sigma)
            print(norm_valor_x)

            datos = {}
                        
            normal = d.getDistribution("Normal",datos)
            
            df = pd.DataFrame(normal.get_sample(norm_valor_x,norm_valor_mu,norm_valor_sigma),columns=['n_gen'])
            df['pdf'] = df['n_gen'].apply(lambda x: normal.get_distribution(x))

            return go.Figure(data=[go.Scatter(x=df['n_gen'],y=df['pdf'])])
            

        df = pd.DataFrame({
            "Fruit": ["CCC", "GGOranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 12, 10, 2, 4, 5],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
        })
        
        
        return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    
    #Regresar aqui el grafico
    #Regresar aqui el grafico
    #Regresar aqui el grafico
    
app.run(host='0.0.0.0', port=8080, debug=True)
