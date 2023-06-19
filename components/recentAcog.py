from dash import html

import data
import components.elements.tagList as tags

def mapRawAcog(acogItem):
    if acogItem[0] == 'F': acogItem[0] = 'Familiar'
    else: acogItem[0] = 'Residencial'
    return acogItem

def GetRecentAcog():
    acogItemList = data.getAcogimientosRecientes()
    acogItemList = list(map(mapRawAcog, acogItemList))

    content = tags.TagList(acogItemList, tags.AcogTag) if len(acogItemList) != 0 else 'No hay acogimientos'
    return [html.H3('-Acogimientos Activos-'),
            html.Div(content)
            ]