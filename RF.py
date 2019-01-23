from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class RF():
    def __init__(self):

        # 对参数 n 进行寻参，这里的参数范围是根据实际情况定义的
        self.n_estimators_options = [7, 14, 21, 28, 35]
        self.best_n_estimators = 0
        self.best_acc = 0

    def train(self, X, y):
        # X 样本数量是 112
        #  https://blog.csdn.net/jeryjeryjery/article/details/78882661
        #  https://www.jianshu.com/p/dbf21ed8be88
        # 最小叶子结点的参数取值
        sample_leaf_options = list(range(1, 100, 1))
        # 重置索引
        real_result = list(y[100:])

        result = []
        for leaf_size in sample_leaf_options:
            for n_estimators_size in self.n_estimators_options:
                if n_estimators_size <= 0:
                    continue
                # n_jobs=-1 用于设定算法使用的cpu核数，-1表示的是使用和cpu核数相同
                # 在利用最大投票数或平均值来预测之前，你想要建立子树的数量。
                # 较多的子树可以让模型有更好的性能，但同时让你的代码变慢。 你应该选择尽可能高的值，只要你的处理器能够承受的住，因为这使你的预测更好更稳定
                # print(n_estimators_size)
                alg = RandomForestClassifier(n_jobs=-1, n_estimators=n_estimators_size, min_samples_leaf=leaf_size)
                alg.fit(X[:100], y[:100])
                predict = alg.predict(X[100:])
                #  mean求平均值,判断y_test和predict数组中每个值进行比较，对应位置的元素相同则为1，不等则为0，新数组和的平均值就是mean()
                acc = 0
                predict = predict.tolist()
                for i in range(0, len(real_result)):
                    acc += abs(real_result[i] - predict[i])
                result.append((leaf_size, n_estimators_size, acc, predict))
                print('[leaf_size,n_estimators, acc]:', leaf_size, n_estimators_size, acc)
        best_fit = (min(result, key=lambda x: x[2]))
        print(best_fit)
        print(real_result)
        print(best_fit[3])
        plt.plot(real_result,label='real',color='yellow')
        plt.plot(best_fit[3], label='predict', color='red')
        plt.legend()  # 显示图例

        plt.show()


