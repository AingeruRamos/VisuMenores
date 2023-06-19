from dash import dcc
from enum import Enum
import data
import plotly.graph_objects as go

from figures import getAyudasGraph, getNotifGraph, getAcogGraph, getMedidasGraph, getAyudasPGraph, getAyudasNGraph

class FIGTYPE(Enum):
    TABLE=0 
    GRAPH=1

class FIGCONTENT(Enum):
    AYUDAS=0
    NOTIF=1
    ACOG=2
    MEDIDAS=3
    AYUDAS_PERIO=4
    AYUDAS_NOPERIO=5

def Registers(fig_type, fig_content):

    fig = None
    if fig_type == FIGTYPE.TABLE:
        table = None
        if fig_content == FIGCONTENT.AYUDAS.value:
            table = data.table_ayudas

        elif fig_content == FIGCONTENT.NOTIF.value:
            table = data.table_notif

        elif fig_content == FIGCONTENT.ACOG.value:
            table = data.table_acog

        elif fig_content == FIGCONTENT.MEDIDAS.value:
            table = data.table_medidas

        elif fig_content == FIGCONTENT.AYUDAS_PERIO.value:
            table = data.table_ayudas
            table = table.query("TIPO=='P'")

        elif fig_content == FIGCONTENT.AYUDAS_NOPERIO.value:
            table = data.table_ayudas
            table = table.query("TIPO=='N'")
    
        table_fig = [go.Table(header=dict(values=list(table.columns),
                                        fill_color='#004996',
                                        font=dict(color='white')),
                            cells=dict(values=table.transpose().values.tolist())
                    )]
        
        fig = go.Figure(data=table_fig)

    else:
        if fig_content == FIGCONTENT.AYUDAS.value:
            fig = getAyudasGraph()

        elif fig_content == FIGCONTENT.NOTIF.value:
            fig = getNotifGraph()

        elif fig_content == FIGCONTENT.ACOG.value:
            fig = getAcogGraph()

        elif fig_content == FIGCONTENT.MEDIDAS.value:
            fig = getMedidasGraph()

        elif fig_content == FIGCONTENT.AYUDAS_PERIO.value:
            fig = getAyudasPGraph()

        elif fig_content == FIGCONTENT.AYUDAS_NOPERIO.value:
            fig = getAyudasNGraph()

    fig.update_layout(
            margin=dict(l=0, r=0, t=20, b=0)
        )
    return dcc.Graph(figure=fig, config={'staticPlot':True})