import pandas as pd
import matplotlib as plt
import numpy as nd
import seaborn as sns
df=pd.read_csv("commafile.csv")
print(df.head())
print(sns.displot(df['c2']))

