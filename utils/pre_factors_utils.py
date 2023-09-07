import pandas as pd


def volatility_turnover(df, volatility_n=250,turnover_n=250):
    '''

    :param df:
    :param volatility_n: 求N日收益率的标准差为波动率
    :return:
    '''
    # 数据预处理
    df["turnover_rate_f"] *= 0.01

    # 计算收益率
    df['day_return'] = df['close'].pct_change()

    # 计算N日波动率 — 即为收益率N日的标准差
    df["rolling_volatility"] = df['day_return'].rolling(volatility_n).std()

    # 换手率
    df["rolling_turnover_rate"] = df.get("turnover_rate_f").rolling(turnover_n).mean()

    # 牛熊指标构建
    df['bull_bear_factor'] = df['rolling_volatility'] / df['rolling_turnover_rate']
    return df

