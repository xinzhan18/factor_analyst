import pandas as pd


def volatility_turnover(df):
    """
    输入dataframe
    :param df:
    :return:
    """
    df["turnover_rate_f"] *= 0.01
    df["day_return"] = (df['close'] - df['close'].shift(1) )/df['close'].shift(1)

    return df

