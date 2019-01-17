import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import numpy as np
def test_dataframe():
    path="/Users/jianyezhou/PycharmProjects/data_analyze/dlj_dlj_order.csv"
    records=[]
    f=open(path,'r',encoding='utf-8' )
    line=f.readline()
    records.append(line)
    while line:
        line=f.readline()
        records.append(line)
    data_frame=DataFrame(records)
    order_status = data_frame[0].value_counts()
    order_status[:9].plot(kind="bar")
    plt.show()

def read_csv():
    sample = pd.read_csv('/Users/jianyezhou/PycharmProjects/data_analyze/dlj_dlj_order.csv')
#    print(sample.describe())
    # fillna 填补缺失值
    sample = sample.fillna('missing')
    renting_sample=sample.loc[sample['order_status']==2,['dorder_id','order_status','finish_time']].head(100)
    print(renting_sample)
#    renting_sample['finish_time'].value_counts().plot()

 #   renting_sample['finish_time'].value_counts().plot()
#    plt.show()
read_csv()
