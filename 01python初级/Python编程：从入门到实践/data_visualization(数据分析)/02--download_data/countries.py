from pygal_maps_world.i18n import COUNTRIES

# 打印国别码
for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])