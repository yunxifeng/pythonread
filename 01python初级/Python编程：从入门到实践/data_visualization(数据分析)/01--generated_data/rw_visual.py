import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk的实例, 并将其包含的点都绘制出来
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 调整绘图窗口的大小
    # 函数figure() 用于指定图表的宽度、 高度、 分辨率和背景色。
    # figsize= Tuple, 单位: 英寸
    plt.figure(dpi=128, figsize=(10, 6))

    # 绘制
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, edgecolors="None", c=point_numbers, cmap=plt.cm.Blues, s=1)

    # 突出起点和重点
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", s=100, edgecolors="none")

    plt.title("Random Walk", fontsize=24)
    # plt.xlabel("x_values", fontsize=12)
    # plt.ylabel("y_values", fontsize=12)
    # plt.tick_params(labelsize=12)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)


    plt.show()


    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break