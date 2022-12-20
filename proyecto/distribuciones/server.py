from dash import Dash,dcc,html
from dash import Input,Output,State
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc
from textos_distribuciones import texto
from distribuciones import *

# Importar Estilos de Bootstrap ['https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css']
external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP]

# Arreglo de los nombres de las distribuciones
distribuciones = ['Binomial','Poisson','Geometrica','Exponencial','Normal']

# Objeto Dash
app = Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=external_stylesheets,
    title="Distribuciones"
)

# Poner un favicon
app._favicon = ("assets/favicon.ico")

# Se inicializa objeto abstracto de las distribuciones
d = DistribucionFactory()

# Bloque del dropdown
type_distribution = html.Div(
    [
        dbc.Label("Distribución -"),
        html.I(className="bi bi-info-circle-fill me-2", id="distribucion_tooltip"),
        dcc.Dropdown(
            id="tipo_distribucion",
            options=[
                {"label": col, "value": col} for col in distribuciones
            ],
            value="Binomial",
        ),
        dbc.Tooltip("Selecciona un tipo de distribucion", target="distribucion_tooltip")
    ]
)

# Bloque del switch
switches = html.Div(
    [
        dbc.Label("Acumulada -"),
        html.I(className="bi bi-info-circle-fill me-2", id="acumulada_tooltip"),
        dbc.Switch(
            id="acumulada_switch",
            value=False,
        ),
        dbc.Tooltip("Calcular la versión de probabilidad acumulada", target="acumulada_tooltip")
    ]
)

# Bloque de los parametros
parameters_binomial = html.Div(
    [
        dbc.Label("Parámetros"),
        dbc.Input(id="binom_valor_n", placeholder="número de pruebas", type="number"),
        html.Br(),
        dbc.Input(id="binom_valor_p", placeholder="probabilidad de éxitos [0-1]", type="number"),
        html.Br(),
        html.Hr(),
        dbc.Label("Generar Valores para Graficar"),
        dbc.Input(id="binom_valor_x", placeholder="cardinalidad", type="number"),
    ], style= {'display': 'none'}, id='parameters_binomial'
)

# Bloque de parametros poisson
parameters_poisson = html.Div(
    [
        dbc.Label("Parámetros"),
        dbc.Input(id="pois_valor_mu", placeholder="número de ocurrencias esperadas > 0", type="number"),
        html.Br(),
        html.Hr(),
        dbc.Label("Generar Valores para Graficar"),
        dbc.Input(id="pois_valor_x", placeholder="cardinalidad", type="number")
    ], style= {'display': 'none'}, id='parameters_poisson'
)

# Bloque de parametros geometrica
parameters_geometrica = html.Div(
    [
        dbc.Label("Parámetros"),
        dbc.Input(id="geom_valor_p", placeholder="probabilidad de éxito [0-1]", type="number"),
        html.Br(),
        html.Hr(),
        dbc.Label("Generar Valores para Graficar"),
        dbc.Input(id="geom_valor_x", placeholder="cardinalidad", type="number")
    ], style= {'display': 'none'}, id='parameters_geometrica'
)

# Bloque de parametros exponencial
parameters_exponencial = html.Div(
    [
        dbc.Label("Parámetros"),
        dbc.Input(id="exp_valor_alpha", placeholder="tasa de ocurrencia del evento > 0", type="number"),
        html.Br(),
        html.Hr(),
        dbc.Label("Generar Valores para Graficar"),
        dbc.Input(id="exp_valor_x", placeholder="cardinalidad", type="number")
    ], style= {'display': 'none'}, id='parameters_exponencial'
)

# Bloque de parametros normal
parameters_normal = html.Div(
    [
        dbc.Label("Parámetros"),
        dbc.Input(id="norm_valor_mu", placeholder="media de distribución", type="number"),
        html.Br(),
        dbc.Input(id="norm_valor_sigma", placeholder="desviación estándar de la distribución > 0", type="number"),
        html.Br(),
        html.Hr(),
        dbc.Label("Generar Valores para Graficar"),
        dbc.Input(id="norm_valor_x", placeholder="cardinalidad", type="number")
    ], style= {'display': 'none'}, id='parameters_normal'
)

# Bloque de botones
actions_buttons = html.Div(
    [
        dbc.Button("CANCELAR", id="cancel_btn", color="danger", className="me-1", n_clicks=0),
        dbc.Button("ACEPTAR", id="aceptar_btn", color="success", className="me-1", n_clicks=0),
        html.Span(id="example-output", style={"verticalAlign": "middle","display":"none"}),
    ],
    className="d-grid gap-2 d-md-flex justify-content-md-center",
)

# Tarjeta con todos los elementos
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

# Grafica
generate_graph = dcc.Graph(
    id='distribution-graph',
    mathjax=True
)

# Bloque de texto
_latex_ = dcc.Markdown(
    children = ''' ''',
    mathjax=True,id='latex_text'
)

# Contenedor principal
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
        html.Hr(),
        html.Br(),
        _latex_
    ],
    fluid=True,
)

#Callback del dropdown
#oculta los inputs de las distribuciones
#que no fueron elegidos
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

# Callback del boton CANCELAR
# Limpia todos los inputs
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

# Callback del buton ACEPTAR
# El output es la grafica
@app.callback(
    Output('distribution-graph', 'figure'),
    Output('latex_text', 'children'),
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
        # Crear un grafico vacio
        text = ''''''
        return go.Figure(go.Scatter(x=[0], y=[0], fill="toself")),text
    
    else:
        
        # en acumulada se deben de sumar la prob actual mas la anterior
        
        if tipo_distribucion == 'Binomial':
            
            datos = {}
            datos['n'] = binom_valor_n
            datos['p'] = binom_valor_p
            datos['x'] = binom_valor_x
            datos['acumulada'] = acumulada_switch

            binomial = d.getDistribution("Binomial",datos)

            x_axis = "Numero de pruebas"
            y_axis = "Probabilidad de exito"
            
            # Crear DataFrame
            if not acumulada_switch:
                df = pd.DataFrame(binomial.get_sample(binom_valor_x),columns=['n_gen'])
                df['pdf'] = df['n_gen'].apply(lambda x: binomial.get_probability(x))
            else:
                df = pd.DataFrame(binomial.get_sample(binom_valor_x),columns=['n_gen'])
                df['pdf'] = df['n_gen'].apply(lambda x: binomial.get_probability_cdf(x))
                                
        elif tipo_distribucion == 'Poisson':
            
            datos = {}
            datos['mu'] = pois_valor_mu
            datos['x'] = pois_valor_x
            datos['acumulada'] = acumulada_switch
            
            poisson = d.getDistribution("Poisson",datos)

            x_axis = "Numero de ocurrencias"
            y_axis = "Probabilidad de exito"
            
            # Crear DataFrame
            if not acumulada_switch:
                df = pd.DataFrame(poisson.get_sample(pois_valor_x),columns=['n_gen'])
                df['pdf'] = df['n_gen'].apply(lambda x: poisson.get_probability(x))
            else:
                df = pd.DataFrame(poisson.get_sample(pois_valor_x),columns=['n_gen'])
                df['pdf'] = df['n_gen'].apply(lambda x: poisson.get_probability_cdf(x))
                                
        elif tipo_distribucion == 'Geometrica':

            datos = {}
            datos['p'] = geom_valor_p
            datos['x'] = geom_valor_x
            datos['acumulada'] = acumulada_switch
            
            geometrica = d.getDistribution("Geometrica",datos)

            x_axis = "Numero de fallas"
            y_axis = "Probabilidad de exito"
            
            # Crear DataFrame
            if not acumulada_switch:
                df = pd.DataFrame(geometrica.get_sample(geom_valor_x),columns=['n_gen'])
                df['pdf'] = df['n_gen'].apply(lambda x: geometrica.get_probability(x))
                
            else:
                df = pd.DataFrame(geometrica.get_sample(geom_valor_x),columns=['n_gen'])
                df['pdf'] = df['n_gen'].apply(lambda x: geometrica.get_probability_cdf(x))
                                
        elif tipo_distribucion == 'Exponencial':

            datos = {}
            datos['alpha'] = exp_valor_alpha
            datos['x'] = exp_valor_x
            datos['acumulada'] = acumulada_switch
            
            exponencial = d.getDistribution("Exponencial",datos)

            x_axis = "x"
            y_axis = "Probabilidad"
            
            if not acumulada_switch:
                df = pd.DataFrame(exponencial.get_sample(exp_valor_x),columns=['n_gen'])
                df['pdf'] = df['n_gen'].apply(lambda x: exponencial.get_probability(x))
            else:
                df = pd.DataFrame(exponencial.get_sample(exp_valor_x),columns=['n_gen'])
                df['pdf'] = df['n_gen'].apply(lambda x: exponencial.get_probability_cdf(x))
        else:

            datos = {}
            datos['mu'] = float(norm_valor_mu)
            datos['sigma'] = float(norm_valor_sigma)
            datos['acumulada'] = acumulada_switch
            
            # Crear objeto distribucion normal
            normal = d.getDistribution("Normal",datos)

            x_axis = "x"
            y_axis = "Probabilidad"
            
            if not acumulada_switch:
                df = pd.DataFrame(normal.get_sample(norm_valor_x),columns=['n_gen'])
                df['pdf'] = df['n_gen'].apply(lambda x: normal.get_probability(x))
                
            else:
                df = pd.DataFrame(normal.get_sample(norm_valor_x),columns=['n_gen'])
                df['pdf'] = df['n_gen'].apply(lambda x: normal.get_probability_cdf(x))
                                
        # Regresar grafico de respuesta
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df['n_gen'],
            y=df['pdf'],
            mode="markers"
        ))

        fig.update_layout(
            title=tipo_distribucion,
            xaxis_title = x_axis,
            yaxis_title = y_axis
        )
        
        return fig,texto(tipo_distribucion,acumulada_switch)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
