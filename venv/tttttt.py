import pandas as pd
from functools import reduce
from statistics import mean
x = pd.DataFrame({'x': [1, 2, 3], 'y': [7, 4, 4]})
m=x['y'].tolist()
avr_value = mean(m)
print(x)
print(m)
print(avr_value)
