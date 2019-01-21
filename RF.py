from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


class RF():
    def __init__(self):

        # 对参数 n 进行寻参，这里的参数范围是根据实际情况定义的
        self.n_estimators_options = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
        self.best_n_estimators = 0
        self.best_acc = 0

    def train(self, X, y, TEST):

        # 处理标签
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        #  https://blog.csdn.net/jeryjeryjery/article/details/78882661
        # 寻参
        for n_estimators_size in self.n_estimators_options:
            alg = RandomForestClassifier(n_jobs=-1, n_estimators=n_estimators_size)
            alg.fit(X_train, y_train)
            predict = alg.predict(X_test)
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
