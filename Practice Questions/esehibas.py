# # import pandas as pd
# # import matplotlib as plt
# # import numpy as nd
# # import seaborn as sns
# # df=pd.read_csv("commafile.csv")
# # print(df.head())
# # print(sns.displot(df['c2']))
# n=int(input())
# sum=0
# for i in range(1,n):
#     sum+=i*i
#     print(f"{i*i} + ",end="")
# print(f"{n*n} = {sum}")
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()
tu=(2,4,6)
t1=(3,7,45,65,34)
l1={i:j for i in t1 for j in tu}
print(l1)
