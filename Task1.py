# Задание 44. В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?


import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('sample_data/california_housing_train.csv')
