import logging
from Classes.logic_handler import Logic
from Classes.map_reader import Reader

WITS_MAP_LOCATION = "../Maps/wits-testimony.csv"
BATTLEFIELD_LEGEND_PATH = "../mappings/battlefield_legend.json"

map_reader = Reader(map_location=WITS_MAP_LOCATION, map_spawn_location=(0,0))
map_logic = Logic(reader=map_reader, spawn_points=(0,0), battlefield_path=BATTLEFIELD_LEGEND_PATH)

first_player = map_logic.players[0]
location_chain = ((0,1), (0,2), (1,3), (2,4), (3,5))

can_move_to_loc = map_logic.can_move_to_location(location_chain=location_chain, player=first_player)

print(can_move_to_loc)

if can_move_to_loc:
    print(first_player.location)
    map_logic.move_to_location(player=first_player, new_location=location_chain[-1])
    print(first_player.location)
