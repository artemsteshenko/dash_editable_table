import dash_bootstrap_components as dbc
from dash import dash_table, dcc, html


def create_layout(data):
    layout = html.Div([

        dbc.NavbarSimple(
            brand="Editable Database",
            brand_href="#",
            color="primary",
            dark=True,
        ),

        dash_table.DataTable(
            id='adding-rows-table',
            columns=[{
                'name': column,
                'id': column,
                'deletable': True,
                'renamable': True
            } for column in data.columns],
            data=data.to_dict('records'),
            editable=True,
            row_deletable=True
        ),

        dbc.Button('Add Row', id='editing-rows-button', n_clicks=0),

        dcc.Graph(id='adding-rows-graph')
    ],
        style={
            'margin': '30px'
        },
    )
    return layout