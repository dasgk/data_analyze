from order_proc import OrderPredicts
from algorithm import Algorithm
from bayes import Bayes

'''
    进行数据处理
'''
order_proc = OrderPredicts()
path = order_proc.data_proc()
'''
    采用算法进行处理
'''
if path!="":
    handle_algorithm = Bayes(path)
    handle_algorithm.bayes_formutiple()
