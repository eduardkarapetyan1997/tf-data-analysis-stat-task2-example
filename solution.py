import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2

chat_id = 298754188 # Ваш chat ID, не меняйте название переменной

#def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
#     alpha = 1 - p
#     loc = x.mean()
#     scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
#     return loc - scale * norm.ppf(1 - alpha / 2), \
#            loc - scale * norm.ppf(alpha / 2)

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    df = n - 1
    x_bar = np.mean(x)
    s_squared = np.var(x, ddof=1)
    alpha = 1 - p
    chi2_left = chi2.ppf(alpha / 2, df)
    chi2_right = chi2.ppf(1 - alpha / 2, df)
    left = np.sqrt(df * s_squared / chi2_right)
    right = np.sqrt(df * s_squared / chi2_left)
    return x_bar - left, x_bar + right
