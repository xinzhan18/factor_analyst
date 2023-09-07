from utils.pre_factors_utils import *
import pandas as pd
from utils.plot_utils import *

sz_001 = pd.read_csv("../data/raw/000001.SH.csv")

df = volatility_turnover(sz_001)


plot_two_yaxis(df,'date','close','rolling_volatility',title='close_250_volatility')
plot_two_yaxis(df,'date','close','rolling_turnover_rate',title='close_250_turnover')

plot_two_yaxis(df,'date','close','bull_bear_factor',title='close_bull_bear_factor')

