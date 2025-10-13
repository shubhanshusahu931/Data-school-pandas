# This is d02.py
import pandas as pd
ufo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')
print(type(ufo))
print(ufo.columns)
print(ufo['City'])
print(type(ufo['City']))
ufo['location'] = ufo.City + ',' + ufo.State
print(ufo.head)