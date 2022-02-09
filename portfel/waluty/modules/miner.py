

import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime as dt

class miner():

    def czytaj(self,cr):
        self.cr = cr
        title=self.cr

        start = dt.datetime(2021, 1, 1)
        end = dt.datetime.now()
        df = web.get_data_yahoo(title+'-usd', start,end)
        combined = df[['Close']].copy()
        plt.plot(combined)
        plt.title(title)
        plt.savefig("./waluty/static/"+title+".png")
