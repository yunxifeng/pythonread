import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = "Populations of Countries in North America"
# 人口最少的国家颜色最浅， 人口最多的国家颜色最深
wm.add("North America", {"ca": 34126000, "us": 309349000, "mx": 113423000})
wm.render_to_file("na_population.svg")