import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from Strategy import Kelly



class Statistic():
    def __init__(self, CO_ID):
        self.CO_ID = CO_ID

    def DataCleaning(self): # 只留 Date, Stock_ID, Open, Max, Min, Close, Spread
        Data = pd.read_csv('Price_' + self.CO_ID +'.csv')[['date', 'stock_id', 'open', 'max', 'min', 'close', 'spread']]
        Data['%_change'] = round((Data['spread'] / Data['open'])*100, 2)  # 新增漲跌幅
        Data = Data[(Data['open'] != 0) & (Data['close'] != 0)] # 去除錯誤資料
        # print(Data.describe())
        return Data # Date Columns -> Stock_ID, Open, Max, Min, Close, Spread, %_change

    def OutlierDrop(self): # IQR判斷離群值
        Data = self.DataCleaning()
        # print(Data['%_change'])
        # 計算IQR
        Q1 = Data['%_change'].quantile(0.25)
        Q3 = Data['%_change'].quantile(0.75)
        IQR = Q3 - Q1
        # 異常值上下界
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        print('Q1 =', Q1, 'Q3 =', Q3)
        print('IQR = ', IQR)
        print('正常值範圍：', lower_bound, '~', upper_bound)
        # 偵測異常值
        outliers = Data[(Data['%_change'] < lower_bound) | (Data['%_change'] > upper_bound)]
        # print(outliers)

        # 拋棄異常值
        Data_Clean = Data[(Data['%_change'] > lower_bound) & (Data['%_change'] < upper_bound)]
        # print(Data_Clean)
        return Data_Clean

'''
#　Example
CO_ID = '1101'
x = Statistic(CO_ID).OutlierDrop()
print(x)

kelly = Kelly(x).Calc()
print(kelly)
'''

