from dash import html

import data
import components.elements.tagList as tags

def GetRecentMedida():
    medidaItemList = data.getMedidasRecientes()
    content = tags.TagList(medidaItemList, tags.MedidaTag) if len(medidaItemList) != 0 else 'No hay medidas legales'
    return [html.H3('-Medidas Activas-'),
            html.Div(content)
            ]