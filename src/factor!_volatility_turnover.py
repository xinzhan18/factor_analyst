from utils.pre_factors_utils import *
import pandas as pd

sz_001 = pd.read_csv("../data/raw/000001.SH.csv")

df = volatility_turnover(sz_001)

print(df)
