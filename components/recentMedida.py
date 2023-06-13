from dash import html

import data
import components.elements.tagList as tags

def GetRecentMedida():
    medidas = data.getMedidasRecientes()
    content = tags.TagList(medidas, tags.MedidaTag) if len(medidas) != 0 else 'No hay medidas legales'
    return [html.H3('-Medidas Activas-'),
            html.Div(content)
            ]