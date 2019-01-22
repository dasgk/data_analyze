from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


class RF():
    def __init__(self):

        # 对参数 n 进行寻参，这里的参数范围是根据实际情况定义的
        self.n_estimators_options = [40, 50, 60, 70, 80]
        self.best_n_estimators = 0
        self.best_acc = 0

    def train(self, X, y, TEST):

        # 将样本划分为训练子集和测试子集
        # 如果是浮点数，在0-1之间，表示样本占比；如果是整数的话就是样本的数量
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        #  https://blog.csdn.net/jeryjeryjery/article/details/78882661
        # 寻参
        for n_estimators_size in self.n_estimators_options:
            # n_jobs=-1 用于设定算法使用的cpu核数，-1表示的是使用和cpu核数相同
            # 在利用最大投票数或平均值来预测之前，你想要建立子树的数量。
            # 较多的子树可以让模型有更好的性能，但同时让你的代码变慢。 你应该选择尽可能高的值，只要你的处理器能够承受的住，因为这使你的预测更好更稳定
            alg = RandomForestClassifier(n_jobs=-1, n_estimators=n_estimators_size)
            alg.fit(X_train, y_train)
            predict = alg.predict(X_test)
            #  mean求平均值,判断y_test和predict数组中每个值进行比较，对应位置的元素相同则为1，不等则为0，新数组和的平均值就是mean()
            acc = (y_test == predict).mean()
            # 更新最优参数和 acc
            if acc >= self.best_acc:
                self.best_acc = acc
                self.best_n_estimators = n_estimators_size
            print('[n_estimators, acc]:', n_estimators_size, acc)

        # 用最优参数进行训练
        rf = RandomForestClassifier(n_jobs=-1, n_estimators=self.best_n_estimators)
        rf.fit(X, y)

        # 预测标签
        predict = rf.predict(TEST)
        # 预测概率
        # predict_prob = rf.predict_prob(TEST)

        # 转换为预测标签为真实标签
        print(predict)
