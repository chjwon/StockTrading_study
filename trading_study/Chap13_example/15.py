import pandas_datareader.data as web
import matplotlib.pyplot as plt

#Get GS Data from Yahoo
gs = web.DataReader('078930.KS', 'yahoo', '2014-01-01', '2016-03-06')

#Moving average
ma5 = gs['Close'].rolling(window=5).mean()
ma20 = gs['Close'].rolling(window=20).mean()
ma60 = gs['Close'].rolling(window=60).mean()
ma120 = gs['Close'].rolling(window=120).mean()

gs['MA5'] = ma5
gs['MA20'] = ma20
gs['MA60'] = ma60
gs['MA120'] = ma120

plt.plot(gs.index, gs['Close'], label = 'Close')
plt.plot(gs.index, gs['MA5'], label = 'MA5')
plt.plot(gs.index, gs['MA20'], label = 'MA20')
plt.plot(gs.index, gs['MA60'], label = 'MA60')
plt.plot(gs.index, gs['MA120'], label = 'MA120')

plt.legend(loc = "best")
plt.grid()
plt.show()
plt.show()