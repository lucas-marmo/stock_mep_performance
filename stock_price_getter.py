import yfinance as yf
from datetime import datetime, timedelta

def get_current_pesos_stock_value(ticker):
    cedear = ticker + '.BA'
    fecha_inicio = datetime.now() - timedelta(days=4)
    fecha_fin = datetime.now() + timedelta(days=1)
    fecha_inicio = fecha_inicio.strftime('%Y-%m-%d')
    fecha_fin = fecha_fin.strftime('%Y-%m-%d')
    cedear = yf.download(cedear,fecha_inicio,fecha_fin, progress=False)
    return cedear.tail(1).iloc[0]['Close']