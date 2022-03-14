from operator import index
import numpy as np
import pandas as pd


df=pd.DataFrame(
    {'a':[4,5,6,4],
     'b':[7,8,9,9],
     'c':[10,11,12,10]},
    
# index 를 지정해주지 않으면 자동으로 0으로 시작해서 매핑된다.
    index=[1,2,3,4]
) 
print(df)

print(df["a"])
print(df[["a"]])

print(df[df["a"]>4])

print(df[["a","b"]])

print(df["a"].value_counts())

print(len(df))

print(df["a"].sort_values())

print()
print(df.sort_values("a",ascending=False))

print()
print(df.drop(["c"],axis=1))
df=df.drop(["c"],axis=1)

print()

print(df.groupby(['a'])["b"].agg(['mean',"sum",'count']))

print(df.groupby(['a'])['b'].describe())

print(pd.pivot_table(df, index="a", values='b', aggfunc="sum"))

print()

print(df.plot())

print(True=='1')

print(pd.read_csv("data/도로교통공단_서울시 도로별 교통사고 위험도지수(EPDO) 정보_20161231.csv", encoding='cp949'))
