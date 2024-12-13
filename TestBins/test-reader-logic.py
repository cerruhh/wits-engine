import logging
from Classes.logic_handler import Logic
from Classes.map_reader import Reader

WITS_MAP_LOCATION = "../Maps/wits-testimony.csv"
BATTLEFIELD_LEGEND_PATH = "../mappings/battlefield_legend.json"

map_reader = Reader(map_location=WITS_MAP_LOCATION, map_spawn_location=(0,0))
map_logic = Logic(reader=map_reader, spawn_points=(0,0), battlefield_path=BATTLEFIELD_LEGEND_PATH)



