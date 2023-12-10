"""Задача №63. Решение в группах
1. Изобразите отношение households к population с помощью точечного графика 
2. Визуализировать longitude по отношения к median_house_value, используя линейный график 
3. Представить гистограмму по housing_median_age 
4. Изобразить гистограмму по median_house_value с оттенком housing_median_age
"""

# from pandas import read_csv
# #import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# df = read_csv('california_housing_train.csv')
#1. Изобразите отношение households к population с помощью точечного графика 
#sns.scatterplot(data=df, x='households', y='population')
#2. Визуализировать longitude по отношения к median_house_value, используя линейный график 
#sns.relplot(data=df, x='longitude', y='median_house_value', kind='line')
#3. Представить гистограмму по housing_median_age 
#sns.histplot(data=df, x='housing_median_age')
#4. Изобразить гистограмму по median_house_value с оттенком housing_median_age
#sns.histplot(data=df, x='median_house_value', hue='housing_median_age')

#plt.show()
"""
Задача №65. Решение в группах Написать EDA для датасета про пингвинов Необходимо:
 ● Использовать 2-3 точечных графика
 ● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
 ● Использовать PairGrid с типом графика на ваш выбор 
 ● Изобразить Heatmap
 ● Использовать 2-3 гистограммы
"""

# from seaborn import load_dataset, scatterplot, PairGrid, displot
# from matplotlib.pyplot import show 

# data = load_dataset("penguins");
# x_vars=["body_mass_g", "bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
# y_vars=['sex']

# ● Использовать 2-3 точечных графика
#scatterplot(data=data, x='flipper_length_mm', y='body_mass_g')
# ● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
#scatterplot(data=data, x='flipper_length_mm', y='body_mass_g', hue='sex', size='island', style='island')
# ● Использовать PairGrid с типом графика на ваш выбор 
#g = PairGrid(data=data, x_vars=x_vars, y_vars=y_vars, hue='species')
# g = PairGrid(data=data, hue='species')
# g.map(scatterplot)
# ● Изобразить Heatmap
#displot(data=data, x='bill_length_mm', y='bill_depth_mm', hue='species')
# ● Использовать 2-3 гистограммы
#data['bill_depth_mm'].hist(bins=5)
#show()

"""
Задача №67. Решение в группах "
1. Создать новый столбец в таблице с пингвинами, который будет отвечать  за показатель длины клюва пингвина. 
high - длинный(от 42)
middle - средний(от 35 до 42) 
low - маленький(до 35)
"""
#-----------------------------------

