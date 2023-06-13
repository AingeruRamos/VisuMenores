from dash import html

import data
import components.elements.tagList as tags

def GetRecentAcog():
    acogs = data.getAcogimientosRecientes()
    content = tags.TagList(acogs, tags.AcogTag) if len(acogs) != 0 else 'No hay acogimientos'
    return [html.H3('-Acogimientos Activos-'),
            html.Div(content)
            ]