from dash import Dash, html, Input, Output, ctx, callback_context, ALL
import flask

import data
import styles as stl

import components.elements.tagList as tags

from components.figContainer import FigContainer
from components.recentHelps import GetRecentHelps
from components.recentNotif import GetRecentNotif
from components.recentAcog import GetRecentAcog
from components.recentMedida import GetRecentMedida

app = Dash(__name__)

def setCookie(cookie_id, value):
    callback_context.response.set_cookie(cookie_id, value)

def getCookie(cookie_id):
    return dict(flask.request.cookies)[cookie_id]

app.layout = html.Div(children=[
    html.H1(children='TFM - Demo Técnica', style={**stl.panel, **{'marginTop':'0px'}}),
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.H4('Información del Menor:'),
                html.Div(children=tags.TagList(data.basicInfo, tags.BasicTag), style=stl.row),

                html.Hr(),

                html.Div(children=tags.TagList(data.stateInfo, tags.BasicTag), style=stl.row),
            ], style=stl.panel),
            
            html.Div(children=[
                html.Div(id='fig_menu', children=[
                    html.Div('Tabla', id='table_button', style=stl.fig_buttons),
                    html.Div('Gráfico', id='graph_button', style=stl.fig_buttons)
                    ], style=stl.fig_menu),

                html.Div(id='fig_container')
            ]
            ,style={**stl.panel, **stl.fig_container})
            
        ],style=stl.info_container),
        
        html.Div(children=[
            html.Div(children=[
                html.Div(id='gen_ayuda', children=['A'], style=stl.menu_button),
                html.Div(id='gen_notif', children=['N'], style=stl.menu_button),
                html.Div(id='gen_acog', children=['AC'], style=stl.menu_button),
                html.Div(id='gen_medida', children=['M'], style=stl.menu_button)
            ],style=stl.menu_container),

            html.Div(id='recent_acts', children=GetRecentHelps(), style={**stl.ayudas_style})
        ],style={**stl.panel, 'padding':'0em'})
    ],style=stl.main_container),
], style=stl.body)

@app.callback(
    Output('fig_container', 'children'),
    Output('recent_acts', 'children'),

    Input('gen_ayuda', 'n_clicks'),
    Input('gen_notif', 'n_clicks'),
    Input('gen_acog', 'n_clicks'),
    Input('gen_medida', 'n_clicks')
)
def updateFigAndRecents(b1, b2, b3, b4):
    data_type = 0
    recent_panel = None
    if 'gen_ayuda' == ctx.triggered_id:
        data_type = 0
        recent_panel = GetRecentHelps()
    elif 'gen_notif' == ctx.triggered_id:
        data_type = 1
        recent_panel = GetRecentNotif()
    elif 'gen_acog' == ctx.triggered_id:
        data_type = 2
        recent_panel = GetRecentAcog()
    elif 'gen_medida' == ctx.triggered_id:
        data_type = 3
        recent_panel = GetRecentMedida()
    else:
        recent_panel = GetRecentHelps()

    setCookie('data_type', str(data_type))
    setCookie('spawn', str(1))
    return FigContainer(data_type, 0), recent_panel

@app.callback(
    Output('fig_container', 'children', allow_duplicate=True),

    Input('table_button', 'n_clicks'),
    Input('graph_button', 'n_clicks'),
    prevent_initial_call=True
)
def updateFig1(b1, b2):
    fig_type = 0
    if 'table_button' == ctx.triggered_id:
        fig_type = 0
    elif 'graph_button' == ctx.triggered_id:
        fig_type = 1

    return FigContainer(int(getCookie('data_type')), fig_type)

@app.callback(
    Output('fig_container', 'children', allow_duplicate=True),
    Input({'type': 'more_b', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def updateFig2(values):
    data_type = 0

    if(int(getCookie('spawn')) == 0):
        if 0 == ctx.triggered_id['index']:
            data_type = 4
        elif 1 == ctx.triggered_id['index']:
            data_type = 5

    setCookie('data_type', str(data_type))
    setCookie('spawn', str(0))
    return FigContainer(data_type, 0)

if __name__ == '__main__':
    app.run_server(debug=True)