import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from PriceCrawler import Price
from Statistics import Statistic
from Strategy import Kelly
from Backtest import BT
from Plot import plot

# 資料抓取, 資料輸入, 統計圖表, 凱利方程計算, 市場回測

if __name__ == '__main__':

    # 資料庫建立
    User_ID = ''                                # FinMind 帳號
    Password = ''                               # FinMind 密碼
    Get = Price(User_ID, Password, 3).Catch()   # 抓取股價資料

    # 資料清洗
    StockID = Price(User_ID, Password, 3).read_stock_index()

    for CO_ID in StockID[0][0:50]: # 批量回測
        print(CO_ID)
        Data = Statistic(CO_ID).OutlierDrop()
        # print(Data.describe())
    
        # 回測公司價格走勢
        # plotter = plot('1101').price()
    
        # 凱利方程計算
        KE = Kelly(Data).Calc()
        print('Kelly = ', KE)
    
        # 市場回測
        if KE > 0: # 凱利方程需大於0才可回測
            KE = KE * 10
            backtester = BT(CO_ID, KE)
            backtester.backtest()
            backtester.summary()
        else:
            print('凱利方程需大於0才可回測')
        print('#################################################################')
