import pandas as pd
import os
from FinMind.data import DataLoader

class Price():
    def __init__(self, USER_ID, PASSWORD, TYPES):
        self.USER_ID = USER_ID
        self.PASSWORD = PASSWORD
        self.TYPES = TYPES #　TYPES = [1:B/S, 2:I/S]
        self.stock_index = pd.read_csv('Stock_Index.csv',)

    def read_stock_index(self): # 股票清單整理
        Stock_Index = pd.read_csv('Stock_Index.csv', header=None)
        Stock_Index = Stock_Index.set_index(0)
        Stock_Index = Stock_Index.drop(['1101B', '1312A', '1522A', '2002A', '2348A', '2836A', '2838A', '2881A', '2881B', '2881C', '2882A', '2882B', '2883B', '2887E', '2887F', '2887Z1', '2888A', '2888B', '2891B', '2891C', '2897A', '3036A', '3702A', '5871A', '6592A', '8112A', '9941A'])
        Stock_Index = Stock_Index.reset_index()
        return Stock_Index

    def Catch(self):
        api = DataLoader()
        api.login(user_id=self.USER_ID, password=self.PASSWORD)
        Stock_Index = self.read_stock_index()
        # print(Stock_Index)
        try:
            if self.TYPES == 1: # 資產負債表抓取
                for CO_ID in Stock_Index[0]:
                    print(CO_ID)
                    data = api.taiwan_stock_balance_sheet(
                        stock_id=str(CO_ID),
                        start_date="2012-01-01",
                        end_date="2021-12-31"
                    )
                    df = pd.DataFrame(
                        data
                    )
                    df.to_csv('BS_' + CO_ID + '.csv', encoding='utf_8_sig', index=False)
                    print("資料寫入成功")

            if self.TYPES == 2: # 綜合損益表抓取
                for CO_ID in Stock_Index[0]:
                    print(CO_ID)
                    data = api.taiwan_stock_financial_statement(
                        stock_id=CO_ID,
                        start_date="2012-01-01",
                        end_date="2021-12-31"
                    )
                    df = pd.DataFrame(
                        data
                    )
                    df.to_csv('IS_' + CO_ID + '.csv', encoding='utf_8_sig', index=False)
                    print("資料寫入成功")
            if self.TYPES == 3: # 每日價格抓取
                for CO_ID in Stock_Index[0][0:50]:
                    if not os.path.exists('Price_' + CO_ID + '.csv'):
                        print(CO_ID)
                        data = api.taiwan_stock_daily(
                            stock_id=CO_ID,
                            start_date="2000-01-01",
                            end_date="2020-12-31"
                        )
                        df = pd.DataFrame(
                            data
                        )
                        df.to_csv('Price_' + CO_ID + '.csv', encoding='utf_8_sig', index=False)
                        # print("資料寫入成功")

        except:
            print("查無資料")

'''
x = 'koko635241@yahoo.com.tw'
y = 'Finmind072'
Get = Price(x, y, 3)
table = Get.Catch()'''

