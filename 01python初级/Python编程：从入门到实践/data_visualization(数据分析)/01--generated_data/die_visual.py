from die import Die
import pygal

# 创建一个骰子
die = Die()
# 掷骰子, 并储存结果
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 可视化frequencies
# 创建条形图实例,储存在hist中
hist = pygal.Bar()

hist.title = "Results of rolling a die 1000 times"
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 向hist传递要给添加的值指定的标签，还有一个列表，其中包含将出现在图表中的值
hist.add("D6", frequencies)
# 将这个图表渲染为一个SVG文件， 这种文件的扩展名必须为.svg。
# 最简单的方式是使用Web浏览器查看svg文件
hist.render_to_file("die_visual.svg")
# Pygal让这个图表具有交互性： 如果你将鼠标指向该图表中的任何条形， 将看到与之相关联的数据