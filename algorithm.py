'''
    作者：周建业
    时间：2019-01-18
    描述：数据源是构造函数的路径，里面是处理好的数据
'''
import numpy as np
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from pandas import DataFrame, Series


class Algorithm():
    def __init__(self, path):
        self.file_path = path

    '''
        多项式朴素贝叶斯算法,is_special_day 是否是特殊节假日    week 是否是周末   天气如何量化成一个因素？？
        思考：风向，暂时不考虑，关于天气和温度，想下应该怎么量化
              温度暂时不考虑，大家都知道怎么穿衣服，只看天气状况
    '''

    def bayes_formutiple(self):
        data_df = pd.read_csv("tzzs_data2.csv")
        X_data_df =data_df.loc[:,['week','is_special_day','weather_quantization']]
        X = X_data_df.values
        y = data_df.loc[:,'order_count']
        clf = MultinomialNB(alpha=2.0)
        clf.fit(X, y)
        print(clf.class_log_prior_)
