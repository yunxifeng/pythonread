import json
import pygal_maps_world.maps
# pygal通常使用较暗的颜色主题
# LightColorizedStyle加亮地图的颜色
#不能直接控制使用的颜色， Pygal将选择默认的基色。 要设置颜色， 可使用RotateStyle ， 并将LightColorizedStyle 作为基本样式。
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code
# 将数据加载到一个列表中
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家2010年的人口数量
# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        # Pygal中的地图制作工具要求数据为特定的格式：用两个国别码表示国家,以及用数字表示人口数量。
        country_name = pop_dict["Country Name"]
        #Python不能直接将包含小数点的字符串'1127437398.85751' 转换为整数（这个小数值可能是人
        # 口数据缺失时通过插值得到的）
        population = int(float(pop_dict["Value"]))

        code = get_country_code(country_name)
        if code:

            cc_populations[code] = population

# 根据人口数量分组着色
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop


# 十六进制的RGB颜色
wm_style = RS("#336699", base_style=LCS)

wm = pygal_maps_world.maps.World(wm_style=wm_style)
wm.title = "World Population in 2010, by Country"
wm.add("2010--0-10m", cc_pops_1)
wm.add("2010--10m-1bn", cc_pops_2)
wm.add("2010-->1bn", cc_pops_3)

wm.render_to_file("world_population3.svg")