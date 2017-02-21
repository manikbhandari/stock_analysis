from datetime import datetime as dt
import pandas_datareader.data as web

#Ending date
today = dt.today()

#Starting date
start = today.year - 3

#Dataframe containing the stock values
'''Arguments :
    StockName (Eg. GOOG)
    Source (Eg. Google Finance/ Yahoo Finance)
    Starting date
    Ending date
'''
df = web.DataReader('MSFT', "google", start, today)

#Printing the dataframe contents (5 rows by default if nothing is passed)
print(df.head())

#Saving it to a CSV File
df.to_csv('MSFT14_17.csv')