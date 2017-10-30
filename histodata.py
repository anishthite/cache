import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')
start = dt.datetime(2017,10,1)
end = dt.datetime(2017,10,25)

df = web.DataReader('AMZN','yahoo',start,end)

df[['High','Low','Open','Close','Volume','Adj Close']].plot()
plt.show()