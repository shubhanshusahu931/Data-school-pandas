import pandas as pd
data = pd.read_table("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/chipotle.tsv")
print(data)
user_cols = ['user_id','age','gender','occupation','zipcode']
mdata=pd.read_table("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/u.user",sep="|",header=None,names=user_cols)
print(mdata)