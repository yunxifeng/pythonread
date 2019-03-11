import matplotlib.pyplot as plt

# s是绘制图形所使用的点的尺寸
# plt.scatter(2, 4, s=200)

# x_values = [1,2,3,4,5]
# y_values = [2, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=50)

x_values = list(range(1,1001))
y_values = [x ** 2 for x in x_values]
# matplotlib允许你给散点图中的各个点指定颜色,默认为蓝色点和黑色轮廓
# 删除数据点的轮廓-->edgecolors="none"
# 修改数据点的颜色-->c="color_name"或者rgb格式c = (*,*,*)-->好像不太行..
# plt.scatter(x_values, y_values, edgecolors="None", c="red", s=1)

# 颜色映射
# 此处将参数c设置成了一个 y 值列表， 并使用参数cmap 告诉pyplot 使用哪个颜色映射。
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors="None", s=1)


# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=14)
# 设置坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# plt.show()
# 自动保存
# 第一个参数: 以什么文件名保存
# 第二个参数: 指定将图表多余的空白区域裁剪掉。如要保留,可以省略
plt.savefig("squares_plot.png", bbox_inches="tight")