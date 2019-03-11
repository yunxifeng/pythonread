from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据国家的指定, 返回pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # 如果没有找到指定国家,则返回None
    return None

# print(get_country_code("Andorra"))
# print(get_country_code("United Arab Emirates"))
# print(get_country_code("Afghanistan"))
