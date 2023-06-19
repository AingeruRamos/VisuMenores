from dash import html

import data
import components.elements.tagList as tags

def mapRawNotif(notifItem):
    if notifItem[0] == 'O': notifItem[0] = 'Ordinario'
    elif notifItem[0] == 'I': notifItem[0] = 'Infractor'
    elif notifItem[0] == 'E': notifItem[0] = 'Extranjero'
    return notifItem

def GetRecentNotif():
    notifItemList = data.getNotificacionesRecientes()
    notifItemList = list(map(mapRawNotif, notifItemList))
    
    content = tags.TagList(notifItemList, tags.NotifTag) if len(notifItemList) != 0 else 'No hay notificaciones'
    return [html.H3('-Notificaciones Recientes-'),
            html.Div(content)
            ]