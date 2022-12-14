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
