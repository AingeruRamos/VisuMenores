import pandas as pd
from datetime import datetime, date
from dateutil import relativedelta
import math

# PLANTILLAS

basicInfoTemplate = [['Nombre','???'], ['Apellidos','??? ???'],
                     ['Sexo',''], ['Fecha Nacimiento',''], 
                     ['Edad',''], ['Origen','XXX'], 
                     ['Minusvalía','']]

stateInfoTemplate = [['Tipo Acogimiento',''], ['Fecha Inicio',''], 
                     ['Responsable del Caso','???']]

def loadBasicInfo(childData):
    aux = basicInfoTemplate.copy()
    aux[2][1] = list(childData['SEXO'])[0]
    aux[3][1] = list(childData['FNACIMIENTO'])[0]
    aux[6][1] = ('No' if list(childData['MINUSVALIDOS'])[0] == 'N' else 'Si')

    start_date = datetime.strptime(aux[3][1], "%Y-%m-%d")

    delta = relativedelta.relativedelta(date.today(), start_date)
    aux[4][1] = f'{delta.years} años'

    return aux

def loadStateInfo(stateData):
    aux = stateInfoTemplate.copy()

    stateData = stateData.sort_values('FECHAINI', ascending=False)
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

# INFORMACIÓN DEL MENOR
basicInfo = loadBasicInfo(table_menores)
stateInfo = loadStateInfo(table_acog)

# INFORMACIÓN RECIENTE

def getAyudasPeriodicasRecientes():
    actual_year = int(str(date.today())[0:4])

    init_filter_year = str(actual_year)
    end_filter_year = str(actual_year+1)
    table = table_ayudas.query("FECSOLIC >= @init_filter_year and FECSOLIC < @end_filter_year")
    table = table.query("TIPO=='P'")
    ayudas = []
    for _, row in table.iterrows():
        concep = row['CONCEPTO']
        cuantia = str(row['TOTAL'])+'€'
        mensual = str(row['TOTALMES'])+'€'

        ayudas.append([concep, cuantia, mensual])
    
    return ayudas

def getAyudasNonPeriodicasRecientes():
    actual_year = int(str(date.today())[0:4])

    init_filter_year = str(actual_year)
    end_filter_year = str(actual_year+1)
    table = table_ayudas.query("FECSOLIC >= @init_filter_year and FECSOLIC < @end_filter_year")
    table = table.query("TIPO=='N'")
    ayudas = []
    for _, row in table.iterrows():
        concep = row['CONCEPTO']
        cuantia = str(row['TOTAL'])+'€'

        ayudas.append([concep, cuantia])
    
    return ayudas

def getNotificacionesRecientes():
    actual_year = int(str(date.today())[0:4])

    init_filter_year = str(actual_year)
    end_filter_year = str(actual_year+1)
    table = table_notif.query("FECNOTIF >= @init_filter_year and FECNOTIF < @end_filter_year")
    
    notifs = []
    for _, row in table.iterrows():
        tipo = row['TIPO']
        if 'O' in tipo:
            tipo = 'Ordinaria'
        elif 'I' in tipo:
            tipo = 'Infractor'
        elif 'E' in tipo:
            tipo = 'Extranjero'

        fecha = row['FECNOTIF']

        notifs.append([tipo, fecha])
    
    return notifs

def getAcogimientosRecientes():
    actual_year = int(str(date.today())[0:4])

    init_filter_year = str(actual_year)
    end_filter_year = str(actual_year+1)
 
    table = table_acog[(table_acog['FECHAFIN'].isna()) | (table_acog['FECHAFIN'] == actual_year)]
    
    acogs = []
    for _, row in table.iterrows():
        tipo = row['TIPOACOG']
        if 'F' in tipo:
            tipo = 'Familiar'
        elif 'R' in tipo:
            tipo = 'Residencial'

        fecha_ini = row['FECHAINI']

        fecha_fin = row['FECHAFIN']

        acogs.append([tipo, fecha_ini, fecha_fin])
    
    return acogs

def getMedidasRecientes():
    actual_year = int(str(date.today())[0:4])
    
    init_filter_year = str(actual_year)
    end_filter_year = str(actual_year+1)

    table = table_medidas[(table_medidas['FECFIN'].isna()) | (table_medidas['FECFIN'] == actual_year)]
    medidas = []
    for _, row in table.iterrows():
        tipo = row['MEDIDA']
        fecha_res = row['FECRES']
        fecha_fin = row['FECFIN']

        medidas.append([tipo, fecha_res, fecha_fin])
    
    return medidas