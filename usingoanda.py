from os import sep
from pickle import FALSE
import numpy as np
import pandas as pd
from io import StringIO, BytesIO
import seaborn as sns
# data=('c1,c2,c3\n''x,y,6\n''a,b,9\n''c,d,11')
data=('c1,c2,c3\n''4,y,l\n''6,b,h\n''8,d,e')
# df= pd.DataFrame(np.arange(5,30).reshape(5,5),index=['r1','r2','r3','r4','r5'],columns=['c1','c2','c3','c4','c5'])
# print(df.head())
# a=df.loc['r1']
# print(type(a))
# b=df.loc[['r1','r2']]
# print(b)
# print(a)
# df.to_csv('commafile.csv')
# a=df['c2'].value_counts()
# a=df['c2']
# print(a)
# print(type(data))
# b=pd.read_csv(StringIO(data),index_col=1)
# b=pd.read_csv(StringIO(data),usecols=['c1','c2'])
# print(b)
# b.to_csv('test1.csv')
# d=pd.read_csv('test1.csv')
# print(d.head())
# pd.read_json()
df=sns.load_dataset("data")
print(df.head())


