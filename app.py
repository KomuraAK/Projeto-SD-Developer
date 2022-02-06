# Autor: Anthony Farias
# Run this app with `python app.py` and

# Módulos
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Função que ativa á lógica da tabela
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col)
                    for col in dataframe.columns], style={'color': 'gold'})
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ], style={'color': 'white'})
            for i in range(min(len(dataframe), max_rows))
        ])
    ], style={
        'font-family': 'Ubuntu',
        'font-size': '20px'
    })

# Variável que guarda a fonte da familia que está sendo usada na página
external_stylesheets = ['https://fonts.googleapis.com/css?family=Ubuntu']

# Início do sistema
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Lista de estilizações reutilizáveis
colors = {
    'background': '#2F3640',
    'text': '#3299D9',
    'DFtext': '#F2D22E'
}

# Dataframe do gráfico de torres
df = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
    "Qtd": [650000, 620000, 500000, 640000, 610000, 590000, 670000, 320000, 590000, 630000, 640000, 620000, 291269, 271269, 221269, 301269, 351269, 501269, 421269, 361269, 351269, 291269, 281269, 421269],
    "Dados": ["Ganho", "Ganho", "Ganho", "Ganho", "Ganho", "Ganho", "Ganho", "Ganho", "Ganho", "Ganho", "Ganho", "Ganho", "Despesa", "Despesa", "Despesa", "Despesa", "Despesa", "Despesa", "Despesa", "Despesa", "Despesa", "Despesa", "Despesa", "Despesa"]
})

fig = px.bar(df, x="Mês", y="Qtd", text_auto='.3s',
             color="Dados", barmode="group")
fig.update_traces(textfont_size=12, textangle=0,
                  textposition="outside", cliponaxis=False)

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['DFtext']
)

# GUI - "Graphical User Interface" dá página
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Br(),

    html.H1(
        children='Dashboard',
        style={
            'font-family': 'Ubuntu',
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Representação de gastos/ganhos mensais do Colégio Integrado XVI de Novembro', style={
        'font-family': 'Ubuntu',
        'textAlign': 'center',
        'color': colors['text'],
    }),

    html.Br(),

    html.Div(children = [generate_table(df)], style={'margin-left': '50px'}),

    html.Br(),

    dcc.Graph(
        id='graph',
        figure=fig,
    ),

    html.Br()
])

# Start do servidor
if __name__ == '__main__':
    app.run_server(debug=True) # preferência
