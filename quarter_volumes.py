# -*- coding:utf-8 -*-

import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)
    i = pd.to_datetime(data['Date'].values)
    v = data['Volume'].values
    vol = pd.Series(v, index=i)
    result = vol.resample('Q').sum()
    p = result.sort_values()
    return p[-2]
    
if __name__ == '__main__':
   print(quarter_volume())
