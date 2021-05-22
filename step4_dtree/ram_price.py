import pandas as pd
import os
import mglearn
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sklearn.tree import DecisionTreeRegressor #예측할거라 리그레서 사용
from sklearn.linear_model import LinearRegression

'''
가격에 대한 예측 / 램 가격 맞추기 예제
'''

class RamPrice(object):
    ram_price = pd.read_csv(os.path.join(mglearn.datasets.DATA_PATH, "ram_price.csv"))
    font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()

    def plot(self):
        rp = self.ram_price
        plt.rc('font', family=self.font_name)
        plt.semilogy(rp.date, rp.price)
        plt.xlabel("년")
        plt.ylabel("가격")
        plt.show()

    def predict(self):
        rp = self.ram_price
        data_train = rp[rp['date'] < 2000]  # 2000 기준
        data_test = rp[rp['date'] >= 2000]
        x_train = data_train['date'][:, np.newaxis]  # train data 를 1열로 만든다
        y_train = np.log(data_train['price'])
        tree = DecisionTreeRegressor().fit(x_train, y_train)
        lr = LinearRegression().fit(x_train, y_train)
        # test 는 모든 데이터(1960 ~ 2010)에 대해 적용한다
        x_all = rp['date'].values.reshape(-1, 1)  # x_all 을 1열로 만든다
        pred_tree = tree.predict(x_all)
        price_tree = np.exp(pred_tree)  # log 값 되돌리기
        pred_lr = lr.predict(x_all)
        price_lr = np.exp(pred_lr)  # log 값 되돌리기
        plt.semilogy(rp['date'], pred_tree,
                     label="TREE PREDIC", ls='-', dashes=(2, 1))
        plt.semilogy(rp['date'], pred_lr,
                     label="LINEAR REGRESSION PREDIC", ls=':')
        plt.semilogy(data_train['date'], data_train['price'], label='TRAIN DATA', alpha=0.4)
        plt.semilogy(data_test['date'], data_test['price'], label='TEST DATA')
        plt.legend(loc=1)
        plt.xlabel('year', size=15)
        plt.ylabel('price', size=15)
        plt.show()

    @staticmethod
    def main():
        rp = RamPrice()
        while 1:
            menu = int(input("0.Exit \n1.Plot \n2.Predict \n")) #프리딕트 = 예측
            if menu == 0:
                break
            elif menu == 1:
                rp.plot()
            elif menu == 2:
                rp.predict()



RamPrice.main()