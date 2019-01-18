from order_proc import OrderPredicts
from algorithm import Algorithm

'''
    进行数据处理
'''
order_proc = OrderPredicts()
path = order_proc.data_proc()
'''
    采用算法进行处理
'''
handle_algorithm = Algorithm(path)
handle_algorithm.bayes_formutiple()
