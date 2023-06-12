# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd

data = pd.read_csv('sample_data/california_housing_train.csv')

res = data[data['population'] == data['population'].min()]['households'].max()

print(f"Минимальное значение population - {data['population'].min()}")
print(f'Максимальная households в зоне минимального значения population - {res}')

