import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

############# Make changes here


app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('What is the best way to Visualize Your Data'),
    dcc.Graph(
        id='this_is_an_id',
        figure={
            'data': [
                {'x': ['Looker', 'Tableau', 'Russ Visualizations'], 'y': [2,3,4], 'type': 'bar', 'name': 'Style'},
                {'x': ['Looker', 'Tableau', 'Russ Visualizations'], 'y': [10, 3, 6], 'type': 'bar', 'name': 'Usability'},
            ],
            'layout': {
                'title': "Because friends don't let friends use Microsoft Powerpoint",
                'xaxis':{'title':'Choice of data visualization'},
                'yaxis':{'title':'Approval rating by average data scientist'},
            }
        }
    )]
)


###### Don't change anything here



if __name__ == '__main__':
    app.run_server()
