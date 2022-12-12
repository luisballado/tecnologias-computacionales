from flask import Flask
from dash import Dash,html,dcc
import plotly.express as px
import pandas as pd

server = Flask(__name__)

app = Dash(
    __name__,
    server=server,
    url_base_pathname='/dash/'
)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(
    children = [
        html.H1(children='Hola Dash'),
        html.Div(children='''
        Dash: A web application framework for your data.
        '''),
        
        dcc.Graph(
            id='example-graph',
            figure=fig
        )]
)

@server.route('/dash')
def principal():
    return app.index()

server.run(host='0.0.0.0', port=5000, debug=True)
