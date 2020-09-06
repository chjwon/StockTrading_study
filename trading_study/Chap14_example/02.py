# 일일 매수 알고리즘에 대한 백테스팅
import pandas_datareader.data as web
import fix_yahoo_finance as yf
import matplotlib.pyplot as plt

# order : 백테스팅 주문 함수
# symbol : 참조할 데이터에 대한 심볼을 등록하는 함수
from zipline.api import order, symbol
# TradingAlgorithm : 클래스의 인스턴스
from zipline.algorithm import TradingAlgorithm


yf.pdr_override()
data = web.get_data_yahoo("AAPL",start="2010-01-01", end="2019-01-01")
# data.head()


# data 부분
data = data[['Adj Close']]
# data.head()
data.columns = ["AAPL"]
# data.head()
data = data.tz_localize("UTC")
# data.head()



def initialize(context):
    pass

def handle_data(context,data):
    order(symbol('AAPL'),1)



algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)

# result.head()

# result[['starting_cash','ending_cash','ending_value']].head()


plt.plot(result.index, result.portfolio_value)
plt.show()






