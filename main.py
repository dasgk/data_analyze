from order_proc import OrderPredicts
import pandas as pd
from RF import RF

'''
    进行数据处理
'''
order_proc = OrderPredicts()
path = order_proc.data_proc()
'''
    采用算法进行处理
'''
if path != "":
    data_df = pd.read_csv("tzzs_data2.csv")
    X_data_df = data_df.loc[:, ['week', 'is_special_day', 'weather_quantization', 'temperature']]
    X = X_data_df.values
    y = data_df.loc[:, 'order_count']
    print('RF result:')
    handle_algorithm = RF()
    handle_algorithm.train(X, y)
