from dash import html
import styles as stl
from dash import dcc

from figures.tables import getAyudasTable, getAyudasPTable, getAyudasNTable, getNotifTable, getAcogimientosTable, getMedidasTable
from figures.extra import getAyudasGraph, getNotifGraph, getAcogGraph, getMedidasGraph, getAyudasPGraph, getAyudasNGraph

def createGraph(fig):
    return dcc.Graph(figure=fig, config={'staticPlot':True})

def FigContainer(data_type, fig_type):

    fig = None
    if fig_type == 0:
        if data_type == 0:
            fig = createGraph(getAyudasTable())
        elif data_type == 1:
            fig = createGraph(getNotifTable())
        elif data_type == 2:
            fig = createGraph(getAcogimientosTable())
        elif data_type == 3:
            fig = createGraph(getMedidasTable())
        elif data_type == 4:
            fig = createGraph(getAyudasPTable())
        elif data_type == 5:
            fig = createGraph(getAyudasNTable())
    else:
        if data_type == 0:
            fig = createGraph(getAyudasGraph())
        elif data_type == 1:
            fig = createGraph(getNotifGraph())
        elif data_type == 2:
            fig = createGraph(getAcogGraph())
        elif data_type == 3:
            fig = createGraph(getMedidasGraph())
        elif data_type == 4:
            fig = createGraph(getAyudasPGraph())
        elif data_type == 5:
            fig = createGraph(getAyudasNGraph())
    return fig