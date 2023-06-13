from dash import html

import data
import components.elements.tagList as tags

def GetRecentNotif():
    notifs = data.getNotificacionesRecientes()
    content = tags.TagList(notifs, tags.NotifTag) if len(notifs) != 0 else 'No hay notificaciones'
    return [html.H3('-Notificaciones Recientes-'),
            html.Div(content)
            ]