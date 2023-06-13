from dash import html

import data
import components.elements.tagList as tags

def GetRecentHelps():
    ayudasPeriodic = data.getAyudasPeriodicasRecientes()
    content1 = tags.TagList(ayudasPeriodic, tags.HelpTag) if len(ayudasPeriodic) != 0 else ['No hay ayudas periódicas']
    
    ayudasNonPeriodic = data.getAyudasNonPeriodicasRecientes()
    content2 = tags.TagList(ayudasNonPeriodic, tags.BasicTag) if len(ayudasNonPeriodic) != 0 else ['No hay facturas']
    return [html.H3('-Ayudas Activas-'),
            html.Div(content1+[tags.MoreTag({'type':'more_b', 'index':0})]),
            html.Hr(),

            html.H3('-Facturas Recientes-'),
            html.Div(content2+[tags.MoreTag({'type':'more_b', 'index':1})])
            ]