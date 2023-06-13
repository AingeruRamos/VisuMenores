from dash import html
import styles as stl

def BasicTag(info):
    return html.Div(children=[
            html.Label(info[0], style={'fontWeight':'bold'}),
            html.Br(),
            html.Label(info[1])
           ], style={**stl.panel, **stl.tag})

def HelpTag(info):
    return html.Div(children=[
            html.Label(info[0], style={'fontWeight':'bold'}),
            html.Br(),
            html.Br(),
            html.Div(children=[
                html.Label(f'Total: {info[1]}'),
                html.Br(),
                html.Label(f'Mensual: {info[2]}')
            ])
           ], style={**stl.panel, **stl.tag})

def NotifTag(info):
    return html.Div(children=[
            html.Label(f'Notificación {info[0]}', style={'fontWeight':'bold'}),
            html.Br(),
            html.Br(),
            html.Label(info[1])
           ], style={**stl.panel, **stl.tag})

def AcogTag(info):
    return html.Div(children=[
            html.Label(f'Acogimiento {info[0]}', style={'fontWeight':'bold'}),
            html.Br(),
            html.Br(),
            html.Label(info[1]),
            html.Label(' | '),
            html.Label(info[2])
           ], style={**stl.panel, **stl.tag})

def MedidaTag(info):
    return html.Div(children=[
            html.Label(info[0], style={'fontWeight':'bold'}),
            html.Br(),
            html.Br(),
            html.Label(info[1]),
            html.Label(' | '),
            html.Label(info[2])
           ], style={**stl.panel, **stl.tag})

def MoreTag(info):
    return html.Div(id=info, children=[
        html.Label('···', style={'fontSize':'1.2em', 'fontWeight':'bold'})
    ],style={**stl.tag, **stl.recent_button})

def TagList(data, tag_f):
        return [tag_f(tag_info) for tag_info in data]
