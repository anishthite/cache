from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import time, os
ts = TimeSeries(key='LE8ABWBMWK8PZ0T4', output_format='pandas', indexing_type='date')
checktime = time.time() + 12

symbol = os.sys.argv[1]

while True:
    data, meta_data = ts.get_intraday(symbol=symbol.upper(),interval='1min', outputsize='full')
    print(data.tail(1))
    # if data['Volume'][-1] > data['Volume'][]
    time.sleep(60)