import pandas as pd
from datetime import datetime, date
from dateutil import relativedelta
import math

# TABLAS
table_menores = pd.read_csv('./data/menores.csv')
table_ayudas = pd.read_csv('./data/ayudas.csv')
table_notif = pd.read_csv('./data/notificaciones.csv')
table_acog = pd.read_csv('./data/acogimientos.csv')
table_medidas = pd.read_csv('./data/medidas.csv')

##########################
altas = table_menores.query("SITUACION=='A'")
cods = list(altas['CODIGO'])
#SELECTED_COD = 'e530bdf24d6fb6dcbd21c41f97fc2da62a7d32302dcce656fac6307d52ee87b1'
SELECTED_COD = cods[563]
##########################

# TABLAS
table_menores = table_menores[table_menores['CODIGO'] == SELECTED_COD]
table_ayudas = table_ayudas[table_ayudas['CODIGO'] == SELECTED_COD]
table_notif = table_notif[table_notif['CODIGO'] == SELECTED_COD]
table_acog = table_acog[table_acog['COD'] == SELECTED_COD]
table_medidas = table_medidas[table_medidas['CODIGO'] == SELECTED_COD]

# TABLAS SIN CODIGO
table_menores = table_menores.iloc[: , 1:]
table_ayudas = table_ayudas.iloc[: , 1:]
table_notif = table_notif.iloc[: , 1:]
table_acog = table_acog.iloc[: , 1:]
table_medidas = table_medidas.iloc[: , 1:]

def getBasicInfo():
    aux = []
    aux.append(['Nombre', '???'])
    aux.append(['Apellidos', '??? ???'])
    aux.append(['Sexo', list(table_menores['SEXO'])[0]])
    aux.append(['Fecha Nacimiento', list(table_menores['FNACIMIENTO'])[0]])

    startDate = datetime.strptime(aux[len(aux)-1][1], "%Y-%m-%d")
    delta = relativedelta.relativedelta(date.today(), startDate)
    aux.append(['Edad', f'{delta.years} años'])

    aux.append(['Origen', 'XXX'])

    isMinusvalidoText = ('No' if list(table_menores['MINUSVALIDOS'])[0] == 'N' else 'Si')
    aux.append(['Minusvalía', isMinusvalidoText])

    return aux

def getStateInfo():
    stateData = table_acog.sort_values('FECHAINI', ascending=False)
    tipoAcog = list(stateData['TIPOACOG'])[0]
    fechaIni = list(stateData['FECHAINI'])[0]
    fechaFin = list(stateData['FECHAFIN'])[0]
    
    if math.isnan(fechaFin):
        if tipoAcog == 'F':
            aux = [['Tipo Acogimiento', 'Familiar'], ['Desde', fechaIni], 
               ['Familia Acogida', '???'], ['Responsable Caso', '???']]
        elif tipoAcog == 'R':
            aux = [['Tipo Acogimiento', 'Residencial'], ['Desde', fechaIni], 
               ['Centro Acogida', '???'], ['Responsable Caso', '???']]
    else:
        aux = [['Tipo Acogimiento', 'Familia Original'], ['Desde', fechaFin], 
               ['Responsable Caso', '???']]
    return aux

def getInstancesOfThisYear(table, columnId):
    actualYear = int(str(date.today())[0:4])
    initYear = str(actualYear)
    endYear = str(actualYear+1)
    return table.query(f"{columnId} >= @initYear and {columnId} < @endYear")

# INFORMACIÓN RECIENTE

def getAyudasPeriodicasRecientes():
    table = getInstancesOfThisYear(table_ayudas, 'FECSOLIC')
    table = table.query("TIPO=='P'")
    
    return [[row['CONCEPTO'], row['TOTAL'], row['TOTALMES']] for _, row in table.iterrows()]

def getAyudasNonPeriodicasRecientes():
    table = getInstancesOfThisYear(table_ayudas, 'FECSOLIC')
    table = table.query("TIPO=='N'")
    
    return [[row['CONCEPTO'], row['TOTAL']] for _, row in table.iterrows()]

def getNotificacionesRecientes():
    table = getInstancesOfThisYear(table_notif, 'FECNOTIF')
    
    return [[row['TIPO'], row['FECNOTIF']] for _, row in table.iterrows()]

def getAcogimientosRecientes():
    actual_year = int(str(date.today())[0:4])
    table = table_acog[(table_acog['FECHAFIN'].isna()) | (table_acog['FECHAFIN'] == actual_year)]

    return [[row['TIPOACOG'], row['FECHAINI'], row['FECHAFIN']] for _, row in table.iterrows()]

def getMedidasRecientes():
    actual_year = int(str(date.today())[0:4])
    table = table_medidas[(table_medidas['FECFIN'].isna()) | (table_medidas['FECFIN'] == actual_year)]
    
    return [[row['MEDIDA'], row['FECRES'], row['FECFIN']] for _, row in table.iterrows()]