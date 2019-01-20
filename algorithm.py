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

