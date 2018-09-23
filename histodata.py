import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')
start = dt.datetime(2000,10,1)
end = dt.datetime(2017,10,25)

df = web.DataReader('GOOG','yahoo',start,end)

#print(df.index.day)
above1050 = df[ df['Open'] >970]

# above1050['Open'].plot()
#df[['Open','Close','Volume']].plot()



