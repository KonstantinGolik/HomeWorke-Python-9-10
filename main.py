# HW 9

# №1

# import pandas as pd

# df = pd.read_csv('sample_data/california_housing_train.csv')
# df.head()

# max_households_in_min_population = df[df['population'] == df['population'].min()]['households'].max()
# print(max_households_in_min_population)

# №2

# import pandas as pd

# df = pd.read_csv('sample_data/california_housing_train.csv')
# df.head()

# avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean()
# print(avg)


# HW 10


# Знакомство с языком Python (семинары)
# Урок 10. Построение графиков
# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

# ============================================================

# import pandas as pd
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})
# print(data)

# one_hot_data = pd.get_dummies(data['whoAmI'])
# data = pd.concat([data, one_hot_data], axis=1)
# data.drop(columns=['whoAmI'], inplace=True)
# print(data)