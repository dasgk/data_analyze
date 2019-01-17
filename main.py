from pandas import DataFrame,Series
import pandas as pd
path="D:\python\project\data_analyze\dlj_dlj_order.csv"
records=[]
f=open(path,'r', encoding='utf-8')
line=f.readline()
records.append(line)
while line:
    line=f.readline()
    records.append(line)
print(records)
