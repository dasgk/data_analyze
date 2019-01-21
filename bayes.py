from sklearn.naive_bayes import MultinomialNB


class Bayes():
    '''
        多项式朴素贝叶斯算法,is_special_day 是否是特殊节假日    week 是否是周末   天气如何量化成一个因素？？
        思考：风向，暂时不考虑，关于天气和温度，想下应该怎么量化
              温度暂时不考虑，大家都知道怎么穿衣服，只看天气状况
    '''

    def bayes_formutiple(self, X, y, Test):
        clf = MultinomialNB(alpha=0.50)
        clf.fit(X, y)
        result = clf.predict(Test)
        print(result)
