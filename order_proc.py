import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import numpy as np
import datetime
import time


class OrderPredicts():
    def __init__(self):
        self.order_info = Series()
        self.museum_id = 5

    '''
        作者：周建业
        时间：2019-01-18
        描述：进行时间格式转换，输入和输出都是字符串，现阶段主要用于订单数据添加列
    '''

    def time_transfer(self, time_str):
        date_obj = datetime.datetime.strptime(time_str, "%Y/%m/%d %H:%M:%S")
        return date_obj.strftime("%Y-%m-%d")

    '''
        作者：周建业
        时间：2019-01-18
        描述：将日期转换为周格式
    '''

    def time_to_week(self, time_str):
        date_obj = datetime.datetime.strptime(time_str, "%Y-%m-%d")
        week = int(date_obj.strftime("%w"))
        return week

    def is_special_day(self, time_str):
        date_obj = datetime.datetime.strptime(time_str, "%Y-%m-%d")
        month = int(date_obj.strftime("%m"))
        day = int(date_obj.strftime("%d"))
        if month == 10:
            if day >= 1 and day <= 7:
                return 1
        return 0

    def date_order_counts(self, date='2018-09-20'):
        if len(self.order_info) == 0:
            order_df = pd.read_csv("dlj_dlj_order.csv")
            # 只获得特定博物馆的订单
            order_df = order_df.loc[order_df['rent_museum_id'] == self.museum_id]
            order_df = order_df.loc[order_df['order_status'] == 5]
            # order_df需要添加列，该列就是date
            order_df["date"] = order_df["pay_time"].map(self.time_transfer)

            date_count = order_df['date'].value_counts()
            self.order_info = date_count

        return self.order_info.get(date, 0)

    '''
     数据预处理，得到订单列表，其中包含天气信息
     只预测特定馆的，默认是牛首山的数据
    '''

    def data_preproc(self, museum_id=5):
        museum_df = pd.read_csv("dlj_museum.csv")
        museum_df = museum_df.loc[museum_df['museum_id'] == museum_id]
        if len(museum_df) == 0:
            # 没有找到对应博物馆，返回空
            return None
        museum_city_df = pd.read_csv("dlj_museum_to_city.csv")
        museum_city_df = museum_city_df.loc[museum_city_df['museum_id'] == museum_id]
        if len(museum_city_df) == 0:
            # 该博物馆没有找到对应的地址
            return None

        museum_city_df = pd.merge(museum_city_df, museum_df)
        museum_city_df = museum_city_df.loc[:, ['museum_id', 'address', 'museum_name']]
        if len(museum_city_df) == 0:
            # 如果为空，说明有问题
            return None
        address = museum_city_df['address'][0]
        city_weather_df = pd.read_csv("dlj_city_to_weather.csv")
        city_weather_df = city_weather_df.loc[city_weather_df['address'] == address]
        if len(city_weather_df) == 0:
            # 如果该城市的天晴情况没有收集到，可以返回了
            return None
        museum_weather = pd.merge(museum_city_df, city_weather_df)
        # 首先及您修改数据合并，得到每个博物馆所在地区的每天的天气情况

        museum_weather = museum_weather.loc[:,
                         ['museum_id', 'museum_name', 'date', 'address', 'weather', 'wind', 'temperature']]
        # 至此已经得到相关的天气情况了，现在开始将订单数据进行融合，为了方便merge将museum_id修改为rent_museum_id
        museum_weather.rename(columns={"museum_id": "rent_museum_id"}, inplace=True)

        museum_weather['order_count'] = museum_weather['date'].map(self.date_order_counts)
        # 添加列，判断当天是否是周末
        museum_weather["week"] = museum_weather["date"].map(self.time_to_week)
        museum_weather["is_special_day"] = museum_weather["date"].map(self.is_special_day)
        return museum_weather

    '''
        作者：周建业
        时间：2019-01-18
        描述：数据处理，核心流程函数
    '''

    def data_proc(self):
        # 获得需要处理的内容
        order_df = self.data_preproc()
        # 处理流程，判断数据
        print("有效订单数据总量:", len(order_df))
        '''预测订单量的有关因素包括，地区（这个其实可以算是无关量，因为特定博物馆订单量无论怎么变都是在一个地方的），
                                    天气：
                                    温度：
                                    风力：
                                    周末：
                                    是否是特殊节假日
        '''

        order_df.to_csv("tzzs_data2.csv")


if __name__ == '__main__':
    handle = OrderPredicts()
    handle.data_proc()
# date_order_counts()
