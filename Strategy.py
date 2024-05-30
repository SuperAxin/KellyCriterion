import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 策略統一在這邊調整

class Kelly:
    def __init__(self, Data):
        self.Data = Data

    def Calc(self):
        mean = self.Data['%_change'].mean()
        print('mean', mean)
        var = self.Data['%_change'].var()
        Kelly = mean / (mean + var)
        # print(Kelly)
        return Kelly

