import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash
from dash.dependencies import Input, Output, State
from layout import create_layout
from connection import conn

data = pd.DataFrame(data=[[1, 78, 34, 30],
                          [2, 67, 42, 25],
                           [3, 66, 28, 50]],
                    columns=['id', 'weight', 'age', 'salary'])

table_name = 'test'
query = f'SELECT * FROM {table_name}'
data.to_sql(table_name, conn, if_exists='replace', index=False)
data = pd.read_sql(query, conn)

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = create_layout(data)

@app.callback(
    Output('adding-rows-table', 'data'),
    Input('editing-rows-button', 'n_clicks'),
    State('adding-rows-table', 'data'),
    State('adding-rows-table', 'columns'))
def add_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows


@app.callback(
    Output('adding-rows-graph', 'figure'),
    Input('adding-rows-table', 'data'),
    Input('adding-rows-table', 'columns'))
def display_output(rows, columns):
    data = pd.DataFrame(rows)
    data.to_sql(table_name, conn, if_exists='replace', index=False)
    app.layout = create_layout(data)
    return {
        'data': [{
            'type': 'heatmap',
            'z': [[row.get(c['id'], None) for c in columns] for row in rows],
            'x': [c['name'] for c in columns]
        }]
    }


if __name__ == '__main__':
    app.run_server(debug=False, host="0.0.0.0", port=4000)

