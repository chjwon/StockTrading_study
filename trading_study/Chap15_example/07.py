# 범례를 이용한 동종 업종 주가 그래프
import pandas_datareader.data as web
import matplotlib.pyplot as plt

lg = web.DataReader('066570.KS','yahoo')
samsung = web.DataReader('005930.KS','yahoo')

plt.plot(lg.index, lg['Close'], label = 'Lg Elecronics')
plt.plot(samsung.index, samsung['Close'], label = 'Samsung Elecronics')

# 범례 출력 왼쪽 위에 ( 어떤 무슨 색인지 설명해주는 박스)
plt.legend(loc='upper left')
plt.show()

