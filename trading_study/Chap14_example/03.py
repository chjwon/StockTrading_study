# 이동평균선 알고리즘에 대한 백테스팅
import pandas_datareader.data as web
import fix_yahoo_finance as yf
import matplotlib.pyplot as plt
from zipline.api import order_target, record, symbol
from zipline.algorithm import TradingAlgorithm

yf.pdr_override()
data=web.get_data_yahoo("AAPL",start="2010-01-02",end="2019-01-01")

# plt.plot(data.index, data['Adj Close'])
# plt.show()

data = data[['Adj Close']]
data.columns = ['AAPL']
data=data.tz_localize('UTC')

# print(data.head())

def initialize(context):
    context.i = 0
    context.sym = symbol('AAPL')

def handle_data(context,data):
    context.i += 1
    if(context.i < 20):
        return
    ma5 = data.history(context.sym, 'price',5,'1d').mean()
    ma20 = data.history(context.sym, 'price',20,'1d').mean()

    if(ma5>ma20):
        # 1주 매수
        order_target(context.sym,1)
    else:
        # 1주 매도
        order_target(context.sym,-1)

    record(AAPL=data.current(context.sym,'price'),ma5=ma5,ma20=ma20)

algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)
