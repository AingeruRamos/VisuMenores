import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from collections import Counter
import numpy as np

import data

COLORS = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', 
          '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', 
          '#FF97FF', '#FECB52']

def updateLayout(fig, title=''):
    fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=0),
        title_text=title
    )

def getAyudasGraph():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "scatter"}]])

    estado_list = list(data.table_ayudas['ESTADO'])
    estado_count = Counter(estado_list)
    
    name = ['Denegado', 'Aprobado']
    count = [estado_count['D'], estado_count['A']]

    fig.add_trace(
        go.Pie(values=count, labels=name, hole=.3),
        row=1, col=1
    )

    anos = [str(ano) for ano in range(1980, 2023)]

    zero = [0 for _ in range(1980, 2024)]

    ayuda_A = zero.copy()
    ayuda_D = zero.copy()
    
    for _, row in data.table_ayudas.iterrows():
        ano_index = int(row['FECSOLIC'][0:4])-1980
        if row['ESTADO'] == 'A':
            ayuda_A[ano_index] += 1
        elif row['ESTADO'] == 'D':
            ayuda_D[ano_index] += 1

    fig.add_trace(go.Bar(name='Ordinario', x=anos, y=ayuda_A, 
                         offsetgroup=1, showlegend=False,
                         marker_color=COLORS[0]),
                  row=1, col=2)
    
    fig.add_trace(go.Bar(name='Infractor', x=anos, y=ayuda_D,
                         offsetgroup=1, base=ayuda_A, showlegend=False,
                         marker_color=COLORS[1]),
                  row=1, col=2)

    updateLayout(fig)
    return fig

def getNotifGraph():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "scatter"}]])
    
    notif = data.table_notif[['FECNOTIF', 'TIPO']]

    tipos_list = list(notif['TIPO'])
    tipos_count = Counter(tipos_list)
    
    name = ['Ordinario', 'Infractor', 'Extranjero']
    count = [tipos_count['O'], tipos_count['I'], tipos_count['E']]

    fig.add_trace(
        go.Pie(values=count, labels=name, hole=.3, 
               marker=dict(colors=COLORS)),
        row=1, col=1
    )

    anos = [str(ano) for ano in range(1980, 2023)]

    zero = [0 for _ in range(1980, 2023)]

    notif_O = zero.copy()
    notif_I = zero.copy()
    notif_E = zero.copy()
    aux = list(np.array(notif_O)+np.array(notif_I))
    
    for _, row in notif.iterrows():
        ano_index = int(row['FECNOTIF'][0:4])-1980
        if row['TIPO'] == 'O':
            notif_O[ano_index] += 1
        elif row['TIPO'] == 'I':
            notif_I[ano_index] += 1
        elif row['TIPO'] == 'E':
            notif_E[ano_index] += 1

    fig.add_trace(go.Bar(name='Ordinario', x=anos, y=notif_O, 
                         offsetgroup=1, showlegend=False, 
                         marker_color=COLORS[0]),
                  row=1, col=2)
    
    fig.add_trace(go.Bar(name='Infractor', x=anos, y=notif_I,
                         offsetgroup=1, base=notif_O, showlegend=False,
                         marker_color=COLORS[1]),
                  row=1, col=2)
    
    fig.add_trace(go.Bar(name='Extranjero', x=anos, y=notif_E,
                         offsetgroup=1, base=aux, showlegend=False,
                         marker_color=COLORS[2]),
                  row=1, col=2)

    updateLayout(fig)
    return fig

def getAcogGraph():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "bar"}]])

    acog = data.table_acog[['FECHAINI', 'TIPOACOG']]

    tipos_list = list(acog['TIPOACOG'])
    tipos_count = Counter(tipos_list)
    
    name = ['Familiar', 'Residencial']
    count = [tipos_count['F'], tipos_count['R']]

    fig.add_trace(
        go.Pie(values=count, labels=name, hole=.3, 
               marker=dict(colors=COLORS)),
        row=1, col=1
    )

    anos = [str(ano) for ano in range(1980, 2023)]

    zero = [0 for _ in range(1980, 2023)]

    acog_F = zero.copy()
    acog_R = zero.copy()
    
    for _, row in acog.iterrows():
        ano_index = int(row['FECHAINI'][0:4])-1980-1
        if row['TIPOACOG'] == 'F':
            acog_F[ano_index] += 1
        elif row['TIPOACOG'] == 'R':
            acog_R[ano_index] += 1

    fig.add_trace(go.Bar(name='Ordinario', x=anos, y=acog_F, 
                         offsetgroup=1, showlegend=False,
                         marker_color=COLORS[0]),
                  row=1, col=2)
    
    fig.add_trace(go.Bar(name='Infractor', x=anos, y=acog_R,
                         offsetgroup=1, base=acog_F, showlegend=False,
                         marker_color=COLORS[1]),
                  row=1, col=2)
    
    updateLayout(fig)
    return fig

def getMedidasGraph():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "bar"}]])

    medidas = data.table_medidas[['FECRES', 'TIPONOTIF']]

    tipos_list = list(medidas['TIPONOTIF'])
    tipos_count = Counter(tipos_list)
    
    name = ['Ordinario', 'Infractor', 'Extranjero']
    count = [tipos_count['O'], tipos_count['I'], tipos_count['E']]

    fig.add_trace(
        go.Pie(values=count, labels=name, hole=.3,
               marker=dict(colors=COLORS)),
        row=1, col=1
    )

    anos = [str(ano) for ano in range(1980, 2023)]

    zero = [0 for _ in range(1980, 2023)]

    medida_O = zero.copy()
    medida_I = zero.copy()
    medida_E = zero.copy()
    aux = list(np.array(medida_O)+np.array(medida_I))
    
    for _, row in medidas.iterrows():
        ano_index = int(row['FECRES'][0:4])-1980
        if row['TIPONOTIF'] == 'O':
            medida_O[ano_index] += 1
        elif row['TIPONOTIF'] == 'I':
            medida_I[ano_index] += 1
        elif row['TIPONOTIF'] == 'E':
            medida_E[ano_index] += 1

    fig.add_trace(go.Bar(name='Ordinario', x=anos, y=medida_O, 
                         offsetgroup=1, showlegend=False,
                         marker_color=COLORS[0]),
                  row=1, col=2)
    
    fig.add_trace(go.Bar(name='Infractor', x=anos, y=medida_I,
                         offsetgroup=1, base=medida_O, showlegend=False,
                         marker_color=COLORS[1]),
                  row=1, col=2)
    
    fig.add_trace(go.Bar(name='Extranjero', x=anos, y=medida_E,
                         offsetgroup=1, base=aux, showlegend=False,
                         marker_color=COLORS[2]),
                  row=1, col=2)

    updateLayout(fig)
    return fig

################################33

def getAyudasPGraph():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "scatter"}]])

    aux_table = data.table_ayudas.query("TIPO=='P'")
    estado_list = list(aux_table['ESTADO'])
    estado_count = Counter(estado_list)
    
    name = ['Denegado', 'Aprobado']
    count = [estado_count['D'], estado_count['A']]

    fig.add_trace(
        go.Pie(values=count, labels=name, hole=.3),
        row=1, col=1
    )

    anos = [str(ano) for ano in range(1980, 2023)]

    zero = [0 for _ in range(1980, 2024)]

    ayuda_A = zero.copy()
    ayuda_D = zero.copy()
    
    for _, row in aux_table.iterrows():
        ano_index = int(row['FECSOLIC'][0:4])-1980
        if row['ESTADO'] == 'A':
            ayuda_A[ano_index] += 1
        elif row['ESTADO'] == 'D':
            ayuda_D[ano_index] += 1

    fig.add_trace(go.Bar(name='Ordinario', x=anos, y=ayuda_A, 
                         offsetgroup=1, showlegend=False,
                         marker_color=COLORS[0]),
                  row=1, col=2)
    
    fig.add_trace(go.Bar(name='Infractor', x=anos, y=ayuda_D,
                         offsetgroup=1, base=ayuda_A, showlegend=False,
                         marker_color=COLORS[1]),
                  row=1, col=2)

    updateLayout(fig)
    return fig

def getAyudasNGraph():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "scatter"}]])

    aux_table = data.table_ayudas.query("TIPO=='N'")
    estado_list = list(aux_table['ESTADO'])
    estado_count = Counter(estado_list)
    
    name = ['Denegado', 'Aprobado']
    count = [estado_count['D'], estado_count['A']]

    fig.add_trace(
        go.Pie(values=count, labels=name, hole=.3),
        row=1, col=1
    )

    anos = [str(ano) for ano in range(1980, 2023)]

    zero = [0 for _ in range(1980, 2024)]

    ayuda_A = zero.copy()
    ayuda_D = zero.copy()
    
    for _, row in aux_table.iterrows():
        ano_index = int(row['FECSOLIC'][0:4])-1980
        if row['ESTADO'] == 'A':
            ayuda_A[ano_index] += 1
        elif row['ESTADO'] == 'D':
            ayuda_D[ano_index] += 1

    fig.add_trace(go.Bar(name='Ordinario', x=anos, y=ayuda_A, 
                         offsetgroup=1, showlegend=False,
                         marker_color=COLORS[0]),
                  row=1, col=2)
    
    fig.add_trace(go.Bar(name='Infractor', x=anos, y=ayuda_D,
                         offsetgroup=1, base=ayuda_A, showlegend=False,
                         marker_color=COLORS[1]),
                  row=1, col=2)

    updateLayout(fig)
    return fig