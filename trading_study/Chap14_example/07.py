# zipline 초기 투자 금액 설정
import pandas_datareader.data as web
import fix_yahoo_finance as yf
from zipline.api import order, record, symbol
from zipline.algorithm import TradingAlgorithm
from zipline.finance import commission
from zipline.utils.factory import create_simulation_parameters
import pandas as pd
pd.set_option('display.float_format','{:.3f}'.format)

yf.pdr_override()
data = web.get_data_yahoo("078930.KS",start = "2019-01-02",end="2019-01-25")

data = data[['Adj Close']]
data.columns = ['GS']
data = data.tz_localize('UTC')

def initialize(context):
    context.i = 0
    context.sym = symbol('GS')
    context.set_commission(commission.PerDollar(cost=0.00165))

def handle_data(context, data):
    order(context.sym,1)

# capital_base = 10^8
algo = TradingAlgorithm(sim_params = create_simulation_parameters(capital_base = 100000000), initialize=initialize, handle_data=handle_data)
result = algo.run(data)

print(result[['starting_cash','ending_cash','ending_value']])
# 실행시 starting_cash, ending_cash 가 10^8 로 설정된다.(초기값) 이후 날짜는 알고리즘에 따라 투자