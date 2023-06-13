import data
import plotly.graph_objects as go

def buildTableFig(orig_data):
    table = [go.Table(
            header=dict(values=list(orig_data.columns),
                        fill_color='#004996',
                        font=dict(color='white')),
            cells=dict(values=orig_data.transpose().values.tolist())
            )]

    return go.Figure(data=table)

def updateLayout(fig):
    fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=0)
    )

def getAyudasTable():
    orig_data = data.table_ayudas

    fig = buildTableFig(orig_data)
    updateLayout(fig)
    return fig

def getAyudasPTable():
    orig_data = data.table_ayudas
    orig_data = orig_data.query("TIPO=='P'")

    fig = buildTableFig(orig_data)
    updateLayout(fig)
    return fig

def getAyudasNTable():
    orig_data = data.table_ayudas
    orig_data = orig_data.query("TIPO=='N'")

    fig = buildTableFig(orig_data)
    updateLayout(fig)
    return fig

def getNotifTable():
    orig_data = data.table_notif

    fig = buildTableFig(orig_data)
    updateLayout(fig)
    return fig

def getAcogimientosTable():
    orig_data = data.table_acog

    fig = buildTableFig(orig_data)
    updateLayout(fig)
    return fig

def getMedidasTable():
    orig_data = data.table_medidas

    fig = buildTableFig(orig_data)
    updateLayout(fig)
    return fig