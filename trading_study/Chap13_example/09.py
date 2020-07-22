from pandas import Series, DataFrame

daeshin = {'open':[11650,11100,11200,11100,11000],
           'high':[12100,11800,11200,11100,11150],
           'low':[11600,11050,10900,109050,10900],
           'close':[11900,11600,1000,11100,11050]
           }

date = ['16.02.29','16.02.26','16.02.25','16.02.24','16.02.23']

daeshin_day = DataFrame(daeshin,columns=['open','high','low','close'], index=date)
print(daeshin_day)