import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class plot:
    def __init__(self, COID,):
        Data = pd.read_csv('Price_' + COID + '.csv')
        self.data = Data[(Data['open'] != 0) & (Data['close'] != 0)]

    def close(self):
        # 確保數據有日期索引
        self.data['date'] = pd.to_datetime(self.data['date'])
        self.data.set_index('date', inplace=True)

        plt.figure(figsize=(15, 6))
        plt.plot(self.data['close'], label='Close Price')
        plt.title('Price Chart')
        plt.xlabel('date')
        plt.ylabel('Price')
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()








'''CO_ID = '1108'
Data = pd.read_csv('Price_' + CO_ID +'.csv')[['date', 'stock_id', 'open', 'max', 'min', 'close', 'spread']]
# 新增漲跌幅
Data['%_change'] = round((Data['spread'] / Data['open'])*100, 2)



# Plot histogram
sns.set_theme(style="darkgrid")
plt.figure(figsize=(10, 6))
sns.histplot(Data['%_change'], bins=35, kde=True)
plt.title('% Change Distribution')
plt.xlabel('% Change')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()'''