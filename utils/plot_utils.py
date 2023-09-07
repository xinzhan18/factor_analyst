import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_two_yaxis(df,date_name,data1,data2,title):
    # 创建时间数据
    time = pd.to_datetime(df[date_name])

    # 创建图形和轴对象
    fig, ax1 = plt.subplots(figsize=(15, 6))
    # 绘制第一条线并设置为左侧y轴
    ax1.set_xlabel('datetime')
    ax1.set_ylabel(data1)  # 针对左侧y轴设置标签颜色
    ax1.plot(time, df[data1], color='tab:red',label=data1)
    ax1.legend(loc='upper right')

    # 创建右侧y轴对象
    ax2 = ax1.twinx()  # 共享横坐标轴
    # 绘制第二条线并设置为右侧y轴
    ax2.set_ylabel(data2)  # 针对右侧y轴设置标签颜色
    ax2.plot(time, df[data2], color='tab:blue',label=data2)
    # 添加标题
    ax2.legend(loc='upper left')
    plt.title(title)
    # 显示图形
    plt.show()