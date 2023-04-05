import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2

chat_id = 298754188 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    
    x2 = np.array([xi**2 for xi in x])
    x2_mean = x2.mean()
    
    chi2_rv = chi2(df = 2 * n)
    
    left = chi2_rv.ppf(1 - alpha / 2)
    right = chi2_rv.ppf(alpha / 2)
    
    return np.sqrt(n * x2_mean / (left * 9)), np.sqrt(n * x2_mean / (right * 9))
