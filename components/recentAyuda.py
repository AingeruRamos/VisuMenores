from dash import html

import data
import components.elements.tagList as tags

def mapRawAyudaPerio(ayudaPerioItem):
    ayudaPerioItem[1] = str(ayudaPerioItem[1])+'€'
    ayudaPerioItem[2] = str(ayudaPerioItem[2])+'€'
    return ayudaPerioItem

def mapRawAyudaNoPerio(ayudaNoPerioItem):
    ayudaNoPerioItem[1] = str(ayudaNoPerioItem[1])+'€'
    return ayudaNoPerioItem

def GetRecentAyuda():
    ayudaPerioItemList = data.getAyudasPeriodicasRecientes()
    ayudaPerioItemList = list(map(mapRawAyudaPerio, ayudaPerioItemList))
    contentAyudasPerio = tags.TagList(ayudaPerioItemList, tags.HelpTag) if len(ayudaPerioItemList) != 0 else ['No hay ayudas periódicas']
    
    ayudaNoPerioItemList = data.getAyudasNonPeriodicasRecientes()
    ayudaNoPerioItemList = list(map(mapRawAyudaNoPerio, ayudaNoPerioItemList))
    contentAyudasNoPerio = tags.TagList(ayudaNoPerioItemList, tags.BasicTag) if len(ayudaNoPerioItemList) != 0 else ['No hay facturas']
    
    return [html.H3('-Ayudas Activas-'),
            html.Div(contentAyudasPerio+[tags.MoreTag({'type':'more_b', 'index':0})]),
            html.Hr(),

            html.H3('-Facturas Recientes-'),
            html.Div(contentAyudasNoPerio+[tags.MoreTag({'type':'more_b', 'index':1})])
            ]