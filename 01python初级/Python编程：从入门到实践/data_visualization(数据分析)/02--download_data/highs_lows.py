import csv
from matplotlib import pyplot as plt
from datetime import datetime

# filename = "sitka_weather_07-2014.csv"
# 绘制全年的最高气温和最低气温图
# filename = "sitka_weather_2014.csv"
filename = "death_valley_2014.csv"
with open(filename) as f:
    # 创建一个与该文件相关联的阅读器（reader )对象
    # 将这个阅读器对象存储在reader 中
    reader = csv.reader(f)
    # 模块csv 包含函数next() ， 调用它并将阅读器对象传递给它时，
    #  它将返回文件中的下一行。
    # reader处理文件中以逗号分隔的第一行数据， 并将每项数据都作为一个元素存储在列表中。
    # 这里只调用了next()一次, 得到文件的第一行(包括文件头)
    # 包含与天气相关的文件头， 指出了每行都包含哪些数据
    header_row = next(reader)

    # 调用了enumerate() 来获取每个元素的索引及其值
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)




    # 从文件中读取日期和每日最高气温
    # reader中将每个数据读取为字符串,并存储在列表中
    # 可能会出现缺失数据的情况,所以进行异常处理
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            # 将字符串转化为日期对象
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            #  打印错误消息后， 循环将接着处理下一行。
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)

    # 绘制折线图
    fig = plt.figure(dpi=128, figsize=(10,6))
    # alpha 指定折线颜色的透明度。 Alpha 值为0表示完全透明， 1（默认设置） 表示完全不透明。
    plt.plot(dates, highs, c="red", linewidth=1, alpha=0.5)
    plt.plot(dates, lows, c="blue", linewidth=1, alpha=0.5)

    # 给图表区域着色
    # fill_between() ，它接受一个 x 值系列和两个 y 值系列， 并填充两个 y 值系列之间的空间
    plt.fill_between(dates, highs, lows, facecolor="green", alpha=0.3)

    # 设置格式
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel(" ", fontsize=16)
    # 调用了fig.autofmt_xdate() 来绘制斜的日期标签， 以免它们彼此重叠
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=16)
    # which一共3个参数['major' ， 'minor'，'both']
    # 默认是major表示主刻度，后面分别为次刻度及主次刻度都显示。
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()