# This is d03.py
import pandas as pd
movies = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')
print(movies.head())
print(movies.describe())
print(movies.shape)
print(movies.dtypes)
print(type(movies))
print(movies.describe(include=['object']))