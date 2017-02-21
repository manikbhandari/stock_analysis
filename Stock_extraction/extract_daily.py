import schedule
import time
from datetime import datetime as dt
import pandas_datareader.data as web

def job():
    today = dt.today()
    yesterday = today.replace(day=today.day-1)
    df = web.DataReader('GOOG', "google", yesterday, today)
    print(df.head())

    #Assuming 'GOOG.csv' exists with atleast a header row in it.
    with open('GOOG.csv', 'a') as f:
        df.to_csv(f, header=False)

#schedule.every().hour.do(job)
schedule.every().day.at("00:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)