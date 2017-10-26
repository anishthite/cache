import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')
start = dt.datetime(2017,1,1)
end = dt.datetime(2017,6,27)

df = web.DataReader('TSLA','google',start,end,200)

df[['High','Low','Open','Close']].plot()
plt.show()