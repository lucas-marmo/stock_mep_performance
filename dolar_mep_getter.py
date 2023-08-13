import requests
import json
import time
from datetime import datetime, timedelta

CEDEAR_INSTRUMENT = 'Cedears'
BOLETO = 'Boleto' 
COMPRA = 'COMPRA' 
VENTA = 'VENTA' 
TICKER = 'Ticker'
GD30 = 'GD30' 
MTCGO = 'MTCGO' 
ON = 'ON' 
EPOCH_DAY = 86400 # seconds in a day
DAYS_AGO = 4
# AMBITO_MEP_HIST_EJ = 'https://mercados.ambito.com//dolarrava/mep/historico-general/2023-06-22/2023-06-23'
AMBITO_MEP_HIST = 'https://mercados.ambito.com//dolarrava/mep/historico-general/{from_date}/{to_date}'
# https://www.reddit.com/r/merval/comments/npi3j8/api_con_informaci%C3%B3n_hist%C3%B3rica_de_cedears/
MERVAL_HIST = 'https://analisistecnico.com.ar/services/datafeed/history?symbol={cedear}%3ACEDEAR&resolution=D&from={from_date}&to={to_date}' # dates in epoch
HEADERS = {'Accept': 'application/json'}
payload = {}

#given a sting with comma decimal format ej: 1,5 -> float
def convert_to_float(string_number):
    correct_format_string_number = string_number.replace(",", ".")
    return float(correct_format_string_number)

def get_dolar_mep(date):
    anio, mes, dia = date.split("-")
    cotizacion = get_dolar_mep_request(anio, mes, dia)    
    return convert_to_float(cotizacion[-1])    

def get_dolar_mep_request(anio, mes, dia): # no discrimina si recibe '07' ó '7' 
    to_date = datetime(int(anio), int(mes), int(dia) + 1)
    # pedimos cotizacion de hoy a 4 dias atras porque el mep opera de lun-viernes no feriados
    from_date = getNDaysAgoDate(to_date, DAYS_AGO)    
    URL_MEP  = AMBITO_MEP_HIST.format(from_date = from_date, to_date = to_date.date()) 
    response = requests.get(URL_MEP, headers=HEADERS,  data=payload)
    
    if response.status_code == 200:
      cotizacion_list = response.text
    return json.loads(cotizacion_list)[1] #quedamos el 1 porque [["Fecha","Referencia"],["26\/07\/2023","503,90"],["25\/07\/2023","507,12"]

# def add_mep_value(ticker):
#     date_list = ticker['Date'].split("-")
#     mep_at_day = get_dolar_mep(date_list[0], date_list[1], date_list[2])    
#     ticker['mep_value'] =  ticker['Neto'] / mep_at_day
#     return ticker

def getEpochToday():
    return time.time()

def getStringToday():
    named_tuple = time.localtime() # get struct_time
    return time.strftime("%Y-%m-%d", named_tuple)

def getNDaysAgoDate(a_date, n): # datetime should be a datetime
    daysAgo = timedelta(days = n)
    return (a_date - daysAgo).date()

def get_dolar_mep_now():
    return get_dolar_mep(getStringToday())


