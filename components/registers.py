from dash import dcc
from enum import Enum
import data
import plotly.graph_objects as go

from graphs import getAyudasGraph, getNotifGraph, getAcogGraph, getMedidasGraph, getAyudasPGraph, getAyudasNGraph

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

def Registers(figType, figContent):
    """
    Devuelve la figura a mostrar en el apartado 'Registros'
    @param fig_type: Tipo de figura (Tabla o Gráfica)
    @param fig_content: Contenido de la figura
    @return: La figura a mostrar en 'Registros'
    """

    fig = None

    if figType == FIGTYPE.TABLE: # Modo Tabla
        table = None
        if figContent == FIGCONTENT.AYUDAS.value:
            table = data.table_ayudas

        elif figContent == FIGCONTENT.NOTIF.value:
            table = data.table_notif

        elif figContent == FIGCONTENT.ACOG.value:
            table = data.table_acog

        elif figContent == FIGCONTENT.MEDIDAS.value:
            table = data.table_medidas

        elif figContent == FIGCONTENT.AYUDAS_PERIO.value:
            table = data.table_ayudas
            table = table.query("TIPO=='P'")

        elif figContent == FIGCONTENT.AYUDAS_NOPERIO.value:
            table = data.table_ayudas
            table = table.query("TIPO=='N'")
    
        table_fig = [go.Table(header=dict(values=list(table.columns),
                                        fill_color='#004996',
                                        font=dict(color='white')),
                            cells=dict(values=table.transpose().values.tolist())
                    )]
        
        fig = go.Figure(data=table_fig)

    else: # Modo 'Gráfica'
        if figContent == FIGCONTENT.AYUDAS.value:
            fig = getAyudasGraph()

        elif figContent == FIGCONTENT.NOTIF.value:
            fig = getNotifGraph()

        elif figContent == FIGCONTENT.ACOG.value:
            fig = getAcogGraph()

        elif figContent == FIGCONTENT.MEDIDAS.value:
            fig = getMedidasGraph()

        elif figContent == FIGCONTENT.AYUDAS_PERIO.value:
            fig = getAyudasPGraph()

        elif figContent == FIGCONTENT.AYUDAS_NOPERIO.value:
            fig = getAyudasNGraph()

    fig.update_layout(
            margin=dict(l=0, r=0, t=20, b=0)
        )
    return dcc.Graph(figure=fig, config={'staticPlot':True})