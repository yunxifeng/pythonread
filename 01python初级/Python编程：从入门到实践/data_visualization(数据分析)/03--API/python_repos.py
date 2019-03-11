import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print(type(r))
# 状态码为200, 表示请求成功
print("Status Code :", r.status_code)


# 将API响应存储在在一个变量中
# 这个API返回JSON格式的信息， 因此我们使用方法json() 将这些信息转换为一个Python字典
response_dict = r.json()
print("Total repositories: ", response_dict["total_count"])

# 探索有关仓库的信息
repo_dicts = response_dict["items"]

# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict["name"])
#     stars.append(repo_dict["stargazers_count"])


# 添加工具提示
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])

    plot_dict = {
        "value": repo_dict["stargazers_count"],
        "label": str(repo_dict["description"]),
        "xlink": repo_dict["html_url"]
    }
    plot_dicts.append(plot_dict)




# 可视化
my_style = LS("#333366", base_style=LCS)

# 定制图表样式
# config: 英文释义: 配置
my_config = pygal.Config()
# 让标签绕x 轴旋转45度（x_label_rotation=45 ）
my_config.x_label_rotation = 45
# 隐藏了图例（show_legend=False ）
my_config.show_legend = False
# 图表标题,副标签,主标签的字体大小
# 副标签是 x 轴上的项目名以及 y 轴上的大部分数字, 主标签是 y 轴上为5000整数倍的刻度
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# truncate_label 将较长的项目名缩短为15个字符（如果你将鼠标指向屏幕上被截短的项目名， 将显示完整的项目名）
my_config.truncate_label = 15
# 隐藏图表中的水平线
my_config.show_y_guides = False
# 自定义宽度
# my_config.width = 1000

chart = pygal.Bar(my_config, my_style=my_style)
chart.title = "Most-Stars Python Projects on Github"

chart.x_labels = names
chart.add(" ", plot_dicts)

chart.render_to_file("python_repos3.svg")




# print(type(repo_dicts))
# print("Repositories returned: ", len(repo_dicts))
#
# # 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
#
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print('\nName:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Description:', repo_dict['description'])



# 处理结果
# print(response_dict.keys())