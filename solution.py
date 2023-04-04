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
    s2 = np.var(x, ddof=1)
    alpha = 1 - p / 2
    left = (n - 1) * s2 / chi2.ppf(alpha, n - 1)
    right = (n - 1) * s2 / chi2.ppf(1 - alpha, n - 1)
    return np.sqrt(left), np.sqrt(right)
