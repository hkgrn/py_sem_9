# Задание 44. В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?


import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'WhoAmI': lst})

print('Исходные данные:')
print(data.head(n=len(data)))
print()

data.loc[data["WhoAmI"] == 'human', 'humans'] = '1'
data.loc[data["WhoAmI"] == 'robot', 'robots'] = '1'
data.loc[data["WhoAmI"] == 'robot', 'humans'] = '0'
data.loc[data["WhoAmI"] == 'human', 'robots'] = '0'

print('ONE HOT вид:')
print(data.head(n=len(data)))
