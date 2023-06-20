from dash import Dash, html, Input, Output, ctx, callback_context, ALL
import flask

import data
import styles as stl

import components.elements.tagList as tags

from components.registers import Registers
from components.registers import FIGTYPE, FIGCONTENT

from components.recentAyuda import GetRecentAyuda
from components.recentNotif import GetRecentNotif
from components.recentAcog import GetRecentAcog
from components.recentMedida import GetRecentMedida

app = Dash(__name__)

###############################
# ESTRUCTURA DE LA APLICACIÓN #
###############################

app.layout = html.Div(children=[
    html.H1(children='TFM - Demo Técnica', style={**stl.panel, **{'marginTop':'0px'}}),
    html.Div(children=[
        
        ###############################################
        # CONTENEDOR DE 'ESTADO ACTUAL' Y 'REGISTROS' #
        ###############################################
        html.Div(children=[
            
            ###############################
            # INFORMACIÓN 'ESTADO ACTUAL' #
            ###############################
            html.Div(children=[
                html.H4('Información del Menor:'),
                html.Div(children=tags.TagList(data.getBasicInfo(), tags.BasicTag), style=stl.row),

                html.Hr(),

                html.Div(children=tags.TagList(data.getStateInfo(), tags.BasicTag), style=stl.row),
            ], style=stl.panel),
            
            ###########################
            # INFORMACIÓN 'REGISTROS' #
            ###########################
            html.Div(children=[
                html.Div(id='fig_menu', children=[
                    html.Div('Tabla', id='table_button', style=stl.fig_buttons),
                    html.Div('Gráfico', id='graph_button', style=stl.fig_buttons)
                    ], style=stl.fig_menu),

                # Aquí se visualiza la información, bein modo Tabla o en modo Gráfica.
                # Por defecto se muestra el modo Tabla.
                # La figura a mostrar es devuelta pro la función Registers en el fichero registers.py.
                # Existen eventos que modifican estas figuras.
                html.Div(id='registers')
            ]
            ,style={**stl.panel, **stl.fig_container})
            
        ],style=stl.info_container),
        
        ####################################
        # INFORMACIÓN 'ACTIVIDAD RECIENTE' #
        ####################################
        html.Div(children=[
            html.Div(children=[
                html.Div(id='gen_ayuda', children=['A'], style=stl.menu_button),
                html.Div(id='gen_notif', children=['N'], style=stl.menu_button),
                html.Div(id='gen_acog', children=['AC'], style=stl.menu_button),
                html.Div(id='gen_medida', children=['M'], style=stl.menu_button)
            ],style=stl.menu_container),

            html.Div(id='recent_acts', children=GetRecentAyuda(), style={**stl.ayudas_style})
        ],style={**stl.panel, 'padding':'0em'})
    ],style=stl.main_container),
], style=stl.body)

###########
# EVENTOS #
###########
#
# Las siguientes funciones controlan los eventos de la aplicación; 'click' de botones en nuestro caso.
#
# Cada función de evento tiene asignada previamente que botones tiene que atender y sobre que partes de la estructura tiene efecto.
# Esto se hace mediante los '@app.callback'. Las funciones de evento deben de devolver OBLIGATORIAMENTE todos los outputs que se le pidan.
#
# Plotly por defecto no permite que dos funciones de evento apunten a la misma salida, por lo que es necesario la instruccion 'allow_duplicate=True'
# para que no aparezcan errores.
#
# A la hora de cargar la aplicación todos los eventos son activados, la instrucción prevent_initial_call=True y el uso de 'cookies'
# como memoria de la aplicación sirven para evitar activaciones prematuras.

def setCookie(cookie_id, value):
    callback_context.response.set_cookie(cookie_id, value)

def getCookie(cookie_id):
    return dict(flask.request.cookies)[cookie_id]

# CLICK EN LOS BOTONES SUPERIORES DE 'ACTIVIDAD RECIENTE'
@app.callback(
    Output('registers', 'children'),
    Output('recent_acts', 'children'),

    Input('gen_ayuda', 'n_clicks'),
    Input('gen_notif', 'n_clicks'),
    Input('gen_acog', 'n_clicks'),
    Input('gen_medida', 'n_clicks')
)
def updateFigAndRecents(b1, b2, b3, b4):
    fig_content = FIGCONTENT.AYUDAS
    recent_panel = None
    if 'gen_ayuda' == ctx.triggered_id:
        fig_content = FIGCONTENT.AYUDAS
        recent_panel = GetRecentAyuda()
    elif 'gen_notif' == ctx.triggered_id:
        fig_content = FIGCONTENT.NOTIF
        recent_panel = GetRecentNotif()
    elif 'gen_acog' == ctx.triggered_id:
        fig_content = FIGCONTENT.ACOG
        recent_panel = GetRecentAcog()
    elif 'gen_medida' == ctx.triggered_id:
        fig_content = FIGCONTENT.MEDIDAS
        recent_panel = GetRecentMedida()
    else:
        recent_panel = GetRecentAyuda()

    setCookie('fig_content', str(fig_content.value))
    setCookie('spawn', str(1))
    return Registers(FIGTYPE.TABLE, fig_content.value), recent_panel

# CLICK EN LOS BOTONES DE MODO DE VISUALIZACIÓN 'REGISTROS'
@app.callback(
    Output('registers', 'children', allow_duplicate=True),

    Input('table_button', 'n_clicks'),
    Input('graph_button', 'n_clicks'),
    prevent_initial_call=True
)
def updateFig1(b1, b2):
    fig_type = FIGTYPE.TABLE
    if 'table_button' == ctx.triggered_id:
        fig_type = FIGTYPE.TABLE
    elif 'graph_button' == ctx.triggered_id:
        fig_type = FIGTYPE.GRAPH

    return Registers(fig_type, int(getCookie('fig_content')))

# CLICK EN LOS BOTONES DE MÁS INFORMACIÓN SOBRE AYUDAS EN 'ACTIVIDA RECIENTE'
@app.callback(
    Output('registers', 'children', allow_duplicate=True),
    Input({'type': 'more_b', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def updateFig2(values):
    fig_content = FIGCONTENT.AYUDAS_PERIO

    if(int(getCookie('spawn')) == 0):
        if 0 == ctx.triggered_id['index']:
            fig_content = FIGCONTENT.AYUDAS_PERIO
        elif 1 == ctx.triggered_id['index']:
            fig_content = FIGCONTENT.AYUDAS_NOPERIO

    setCookie('fig_content', str(fig_content.value))
    setCookie('spawn', str(0))
    return Registers(FIGTYPE.TABLE, fig_content.value)

###################
# FUNCION INICIAL #
###################
if __name__ == '__main__':
    app.run_server(debug=True)