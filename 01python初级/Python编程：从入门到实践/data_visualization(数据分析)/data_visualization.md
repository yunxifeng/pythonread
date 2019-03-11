# 数据可视化(Data Visualization)
- matplotlib画廊: [http://matplotlib.org/ ]
## 生成数据
- [折线图]-->mpl_squares.py
    - 函数plot(): 二维线画图函数
    - 函数show(): 打开matplotlib查看器,并显示绘制的图形
    - 注: - plot: 制图
          - square: 平方
          - label: 标签
          - axis: 轴,轴线 
          - param: 参数
          - tick mark: 刻度线
- [散点图]-->scatter_squares.py
    - 函数scatter(): 向它传递一对x和y坐标,它将在指定位置绘制一个点
    - 函数axis([*,*,*,*]): 指定了每个坐标轴的取值范围.函数axis()要求提供四个值: x和y坐标轴的最小值和最大值。
    - 颜色映射(colormap): 是一系列颜色,它们从起始颜色渐变到结束颜色。 
                          在可视化中,颜色映射用于突出数据的规律.
                          [要了解pyplot 中所有的颜色映射， 请访问http://matplotlib.org/ ， 
                          单击Examples， 向下滚动到Color Examples， 再单击colormaps_reference。]
    - 自动保存图表: 要让程序自动将图表保存到文件中，可将对plt.show()的调用替换为对plt.savefig()的调用
    - 注: - scatter: 分散, 使散开
- 随机漫步-->random_walk.py, rw_visual.py
    - 随机漫步是这样行走得到的路径：每次行走都完全是随机的，没有明确的方向，结果是由一系列随机决策决定的。
    - 注: - random: 随机的  
- 使用Pygal模拟掷骰子
    - 安装pygal包
    - pygal画廊: [http://www.pygal.org/] ，单击Documentation，再单击Chart types。 
    - 注: - die: 骰子
          - dice: 骰子
          - visual: 视觉的
          - roll: 滚动
          - frequency: 频率
          - histogram: 直方图 柱状图 柱形统计图
    - [直方图]-->die.py, die_visual.py, dice_visual.py, different_dice.py
## 下载数据
- CSV文件格式
    - 要在文本文件中存储数据，最简单的方式是将数据作为一系列以逗号分隔的值(CSV)写入文件。 
    - csv模块包含在python标准库中
    - 案例1-->highs_lows.py
- JSON格式
    - world_population.py, countries.py, country_codes.py, americas.py, an_populations.py
## 使用API
- Web应用编程接口(API): 自动请求网站的特定信息,再对这些信息进行可视化.
- Web API是网站的一部分，用于与使用非常具体的URL请求特定信息的程序交互。这种请求称为API调用。 
  请求的数据将以易于处理的格式（如JSON或CSV）返回。 
- 在本章中，我们将编写一个程序，它自动下载GitHub上星级最高的Python项目的信息,并对这些信息进行可视化。
- 案例: 
    - [https://api.github.com/search/repositories?q=language:python&sort=stars] 
        - 这个调用返回GitHub当前托管了多少个Python项目， 还有有关最受欢迎的Python仓库的信息。
        - 第一部分(https://api.github.com/)将请求发送到GitHub网站中响应API调用的部分；
        - 接下来的一部分(search/repositories)让API搜索GitHub上的所有仓库。
        - 后面的问号指出我们要传递一个实参。q表示查询，而等号让我们能够开始指定查询(q=)。
          通过使用language:python,我们指出只想获取主要语言为Python的仓库的信息。
          最后一部分(&sort=stars)指定将项目按其获得的星级进行排序。
    - 监视API的速率限制
        - [https://api.github.com/rate_limit]
        - 
                "search": {
                  "limit": 10,          # 极限为每分钟10个请求， 
                  "remaining": 10,      # 而在当前这一分钟内， 我们还可执行8个请求
                  "reset": 1546838030   # reset值指的是配额将重置的Unix时间或新纪元时间 （1970年1月1日午夜后多少秒）
                                        # 用完配额后， 你将收到一条简单的响应， 由此知道已到达API极限。 
                                        # 到达极限后， 你必须等待配额重置。
                },
- 案例:
    - 返回Hacker News上当前热门文章的ID,再查看每篇排名靠前的文章
    - hn_submissions.py












    
