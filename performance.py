import pandas as pd
from dolar_mep_getter import *
from stock_price_getter import *

file = './my_current_stock.xlsx'

cedears_df = pd.read_excel(file)

### BUY DATE VALUES
#Add the MEP value at the buy date of each cedear.
cedears_df['Buy Date MEP value'] = cedears_df['Date'].apply(get_dolar_mep)
#Add the stock MEP value at the buy date of each cedear.
cedears_df['Buy Date stock MEP value'] = cedears_df['Unit price'] / cedears_df['Buy Date MEP value']

### CURRENT VALUES
#Get current MEP value
current_mep_value = get_dolar_mep_now()
#Add current stock pesos value of each cedear
cedears_df['Current stock ARS value'] = cedears_df['Ticker'].apply(get_current_pesos_stock_value)
#Add current stock MEP value of each cedear
cedears_df['Current stock MEP value'] = cedears_df['Current stock ARS value'] / current_mep_value

### PERFORMANCE
#Add performance in ARS
cedears_df['Performance ARS'] = 100 * ((cedears_df['Current stock ARS value'] / cedears_df['Unit price']) - 1)
cedears_df['Performance ARS'] = cedears_df['Performance ARS'].round(2)
#Add performance in MEP
cedears_df['Performance MEP'] = 100 * ((cedears_df['Current stock MEP value'] / cedears_df['Buy Date stock MEP value']) - 1)
cedears_df['Performance MEP'] = cedears_df['Performance MEP'].round(2)

export_excel = cedears_df.to_excel (r'./my_performance.xlsx', index = None, header=True)

print("Valor actual dolar mep: " + str(current_mep_value))
# print(cedears_df)