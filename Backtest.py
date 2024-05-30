import pandas as pd
import matplotlib.pyplot as plt

from Statistics import Statistic
from Plot import plot

class BT:
    def __init__(self, CO_ID, Kelly):
        Data = pd.read_csv('Price_' + CO_ID + '.csv')
        self.data = Data[(Data['open'] != 0) & (Data['close'] != 0)]
        self.cash = 1000000  # 初始資金
        self.kelly = Kelly
        self.position = 0  # 持倉
        self.cash_record = []
        self.trades = []  # 記錄交易

    def buy(self, date, price, quantity):
        total_cost = price * quantity
        if self.cash >= total_cost:
            # print('BUY !!', 'date', date, 'price', price, 'quantity', quantity)
            self.cash -= total_cost
            self.position += quantity
            self.trades.append({'date': date, 'type': 'BUY', 'price': price, 'quantity': quantity})
        else:
            print("資金不足，無法買入")

    def sell(self, date, price, quantity):
        if self.position >= quantity:
            # print('SELL !!', 'date', date, 'price', price, 'quantity', quantity)
            self.cash += price * quantity
            self.position -= quantity
            self.trades.append({'date': date, 'type': 'SELL', 'price': price, 'quantity': quantity})
        else:
            print("持倉不足，無法賣出")

    def backtest(self):
        for index, row in self.data.iterrows():
            date = row['date']
            price_open = row['open']
            price_close = row['close']
            # print('Today', date,'Cash', self.cash, 'Open Price is', price_open, 'Close Price is',price_close)
            self.cash_record.append({'date': date, 'cash': int(self.cash)})

            # 每天開盤投入 Kelly 比例的資金並在收盤時賣出
            Buy_In_Cash = self.cash * self.kelly # 投入資金
            Buy_In_Quantity = int(round(Buy_In_Cash / price_open, 0))
            # print(Buy_In_Cash, Buy_In_Quantity)
            self.buy(date, price_open, Buy_In_Quantity)  #
            self.sell(date, price_close, self.position)  # 當天全數賣出

    def summary(self):
        portfolio_value = self.cash + self.position * self.data.iloc[-1]['close']
        print(f'最終資金: {round(self.cash, 0)}')
        print(f'最終持倉: {self.position}')
        print(f'最終投資組合價值: {round(portfolio_value, 0)}')
        # print(f'交易記錄: {self.trades}')

        # 資金走向
        # print(pd.DataFrame(self.cash_record))
        df = pd.DataFrame(self.cash_record)
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)

        plt.figure(figsize=(15, 6))
        plt.plot(df['cash'], label='Cash')
        plt.title('Cash Chart')
        plt.xlabel('date')
        plt.ylabel('Price')
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()


# 使用範例

'''Kelly = 0.002
COID = '1101'
Data = x = Statistic(COID).DataCleaning()
print(Data)
backtester = BT(Data, COID, Kelly)
backtester.backtest()
backtester.summary()'''


