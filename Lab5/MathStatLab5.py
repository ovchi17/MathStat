import pandas as pd
import numpy as np
from scipy.stats import f

data = pd.read_csv('sex_bmi_smokers.csv')

smokers_bmi = data['bmi'][data['smoker'] == 'yes']
non_smokers_bmi = data['bmi'][data['smoker'] == 'no']

# Рассчитать средние значения для каждой группы
smokers_mean = np.mean(smokers_bmi)
non_smokers_mean = np.mean(non_smokers_bmi)

# Рассчитать среднее значение для всех данных
total_mean = np.mean(np.concatenate([smokers_bmi, non_smokers_bmi]))

# Рассчитать суммы квадратов внутри групп (SSW)
ssw_smokers = np.sum((smokers_bmi - smokers_mean) ** 2)
ssw_non_smokers = np.sum((non_smokers_bmi - non_smokers_mean) ** 2)
ssw = ssw_smokers + ssw_non_smokers

# Рассчитать суммы квадратов между группами (SSB)
ssb = len(smokers_bmi) * (smokers_mean - total_mean) ** 2 + len(non_smokers_bmi) * (non_smokers_mean - total_mean) ** 2

# Рассчитать средние квадраты внутри групп (MSW) и между группами (MSB)
df_between = 1  # степени свободы между группами
df_within = len(smokers_bmi) + len(non_smokers_bmi) - 2  # степени свободы внутри групп
msb = ssb / df_between
msw = ssw / df_within

# Рассчитать значение F
f_val = msb / msw

# Найти значение p
p_val = 1 - f.cdf(f_val, df_between, df_within)

# Интерпретировать результаты
print('F-value:', f_val)
print('p-value:', p_val)