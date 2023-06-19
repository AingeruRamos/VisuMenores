import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

import data

COLORS = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', 
          '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', 
          '#FF97FF', '#FECB52']

def addCumulativeBarPlot(fig, position, x_axis, y_axises, names, colors):
    row, col = position
    offset = np.zeros(len(x_axis))

    for i, y_axis in enumerate(y_axises): 
        fig.add_trace(go.Bar(name=names[i], x=x_axis, y=y_axis, 
                            offsetgroup=1, base=offset, showlegend=False,
                            marker_color=colors[i]),
                    row=row, col=col)
        offset += y_axis

def getAyudasGraph():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "scatter"}]])

    x_axis = [str(ano) for ano in range(1980, 2024)]

    ayuda_A = np.zeros(len(x_axis))
    ayuda_D = np.zeros(len(x_axis))
    
    for _, row in data.table_ayudas.iterrows():
        ano_index = int(row['FECSOLIC'][0:4])-1980
        if row['ESTADO'] == 'A':
            ayuda_A[ano_index] += 1
        elif row['ESTADO'] == 'D':
            ayuda_D[ano_index] += 1

    count_A = np.sum(ayuda_A)
    count_D = np.sum(ayuda_D)

    fig.add_trace(
        go.Pie(values=[count_A, count_D], labels=['Aprobado', 'Denagado'], hole=.3),
        row=1, col=1
    )

    addCumulativeBarPlot(fig, (1, 2), x_axis, [ayuda_A, ayuda_D], 
                                                ['Aprobado', 'Denegado'], 
                                                [COLORS[0], COLORS[1]])
    
    return fig

def getNotifGraph():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "scatter"}]])
    
    notif = data.table_notif[['FECNOTIF', 'TIPO']]

    x_axis = [str(ano) for ano in range(1980, 2024)]

    notif_O = np.zeros(len(x_axis))
    notif_I = np.zeros(len(x_axis))
    notif_E = np.zeros(len(x_axis))
    
    for _, row in notif.iterrows():
        ano_index = int(row['FECNOTIF'][0:4])-1980
        if row['TIPO'] == 'O':
            notif_O[ano_index] += 1
        elif row['TIPO'] == 'I':
            notif_I[ano_index] += 1
        elif row['TIPO'] == 'E':
            notif_E[ano_index] += 1

    count_O = np.sum(notif_O)
    count_I = np.sum(notif_I)
    count_E = np.sum(notif_E)

    fig.add_trace(
        go.Pie(values=[count_O, count_I, count_E], labels=['Ordinario', 'Infractor', 'Extranjero'], hole=.3, 
               marker=dict(colors=COLORS)),
        row=1, col=1
    )

    addCumulativeBarPlot(fig, (1, 2), x_axis, [notif_O, notif_I, notif_E], 
                                                ['Ordinario', 'Infractor', 'Extranjero'], 
                                                [COLORS[0], COLORS[1], COLORS[2]])

    return fig

def getAcogGraph():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "bar"}]])

    acog = data.table_acog[['FECHAINI', 'TIPOACOG']]

    x_axis = [str(ano) for ano in range(1980, 2024)]

    acog_F = np.zeros(len(x_axis))
    acog_R = np.zeros(len(x_axis))
    
    for _, row in acog.iterrows():
        ano_index = int(row['FECHAINI'][0:4])-1980
        if row['TIPOACOG'] == 'F':
            acog_F[ano_index] += 1
        elif row['TIPOACOG'] == 'R':
            acog_R[ano_index] += 1

    count_F = np.sum(acog_F)
    count_R = np.sum(acog_R)

    fig.add_trace(
        go.Pie(values=[count_F, count_R], labels=['Familiar', 'Residencial'], hole=.3, 
               marker=dict(colors=COLORS)),
        row=1, col=1
    )

    addCumulativeBarPlot(fig, (1, 2), x_axis, [acog_F, acog_R], 
                                                ['Familiar', 'Residencial'], 
                                                [COLORS[0], COLORS[1]])

    return fig

def getMedidasGraph():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "bar"}]])

    medidas = data.table_medidas[['FECRES', 'TIPONOTIF']]

    x_axis = [str(ano) for ano in range(1980, 2024)]

    medida_O = np.zeros(len(x_axis))
    medida_I = np.zeros(len(x_axis))
    medida_E = np.zeros(len(x_axis))
    
    for _, row in medidas.iterrows():
        ano_index = int(row['FECRES'][0:4])-1980
        if row['TIPONOTIF'] == 'O':
            medida_O[ano_index] += 1
        elif row['TIPONOTIF'] == 'I':
            medida_I[ano_index] += 1
        elif row['TIPONOTIF'] == 'E':
            medida_E[ano_index] += 1

    count_O = np.sum(medida_O)
    count_I = np.sum(medida_I)
    count_E = np.sum(medida_E)

    fig.add_trace(
        go.Pie(values=[count_O, count_I, count_E], labels=['Ordinario', 'Infractor', 'Extranjero'], hole=.3,
               marker=dict(colors=COLORS)),
        row=1, col=1
    )

    addCumulativeBarPlot(fig, (1, 2), x_axis, [medida_O, medida_I, medida_E], 
                                                ['Ordinario', 'Infractor', 'Extranjero'], 
                                                [COLORS[0], COLORS[1], COLORS[2]])

    return fig

################################

def getAyudasPGraph():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "scatter"}]])

    aux_table = data.table_ayudas.query("TIPO=='P'")

    x_axis = [str(ano) for ano in range(1980, 2024)]

    ayuda_A = np.zeros(len(x_axis))
    ayuda_D = np.zeros(len(x_axis))
    
    for _, row in aux_table.iterrows():
        ano_index = int(row['FECSOLIC'][0:4])-1980
        if row['ESTADO'] == 'A':
            ayuda_A[ano_index] += 1
        elif row['ESTADO'] == 'D':
            ayuda_D[ano_index] += 1
    
    count_A = np.sum(ayuda_A)
    count_D = np.sum(ayuda_D)

    fig.add_trace(
        go.Pie(values=[count_A, count_D], labels=['Aprobado', 'Denegado'], hole=.3),
        row=1, col=1
    )

    addCumulativeBarPlot(fig, (1, 2), x_axis, [ayuda_A, ayuda_D], 
                                                ['Aprobado', 'Denegado'], 
                                                [COLORS[0], COLORS[1]])

    return fig

def getAyudasNGraph():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "scatter"}]])

    aux_table = data.table_ayudas.query("TIPO=='N'")

    x_axis = [str(ano) for ano in range(1980, 2024)]

    ayuda_A = np.zeros(len(x_axis))
    ayuda_D = np.zeros(len(x_axis))
    
    for _, row in aux_table.iterrows():
        ano_index = int(row['FECSOLIC'][0:4])-1980
        if row['ESTADO'] == 'A':
            ayuda_A[ano_index] += 1
        elif row['ESTADO'] == 'D':
            ayuda_D[ano_index] += 1

    count_A = np.sum(ayuda_A)
    count_D = np.sum(ayuda_D)

    fig.add_trace(
        go.Pie(values=[count_A, count_D], labels=['Aprobado', 'Denegado'], hole=.3),
        row=1, col=1
    )

    addCumulativeBarPlot(fig, (1, 2), x_axis, [ayuda_A, ayuda_D], 
                                                ['Aprobado', 'Denegado'], 
                                                [COLORS[0], COLORS[1]])

    return fig