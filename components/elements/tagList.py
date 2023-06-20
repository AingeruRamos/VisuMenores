from dash import html
import styles as stl

def BasicTag(item):
    return html.Div(children=[
            html.Label(item[0], style={'fontWeight':'bold'}),
            html.Br(),
            html.Label(item[1])
           ], style={**stl.panel, **stl.tag})

def HelpTag(item):
    return html.Div(children=[
            html.Label(item[0], style={'fontWeight':'bold'}),
            html.Br(),
            html.Br(),
            html.Div(children=[
                html.Label(f'Total: {item[1]}'),
                html.Br(),
                html.Label(f'Mensual: {item[2]}')
            ])
           ], style={**stl.panel, **stl.tag})

def NotifTag(item):
    return html.Div(children=[
            html.Label(f'Notificación {item[0]}', style={'fontWeight':'bold'}),
            html.Br(),
            html.Br(),
            html.Label(item[1])
           ], style={**stl.panel, **stl.tag})

def AcogTag(item):
    return html.Div(children=[
            html.Label(f'Acogimiento {item[0]}', style={'fontWeight':'bold'}),
            html.Br(),
            html.Br(),
            html.Label(item[1]),
            html.Label(' | '),
            html.Label(item[2])
           ], style={**stl.panel, **stl.tag})

def MedidaTag(item):
    return html.Div(children=[
            html.Label(item[0], style={'fontWeight':'bold'}),
            html.Br(),
            html.Br(),
            html.Label(item[1]),
            html.Label(' | '),
            html.Label(item[2])
           ], style={**stl.panel, **stl.tag})

def MoreTag(item):
    return html.Div(id=item, children=[
        html.Label('···', style={'fontSize':'1.2em', 'fontWeight':'bold'})
    ],style={**stl.tag, **stl.recent_button})

def TagList(itemList, tag_f):
        return [tag_f(tag_info) for tag_info in itemList]
