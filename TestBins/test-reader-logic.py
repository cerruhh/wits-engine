# import logging
import numpy

from Classes.logic_handler import Logic
from Classes.map_reader import Reader
from Classes.Convertor import Convertor
import os
print(f"PWD: {os.getcwd()}")
import Classes.astar

WITS_MAP_LOCATION = "../Maps/wits-testimony.csv"
BATTLEFIELD_LEGEND_PATH = "../mappings/battlefield_legend.json"

choose_map = input("Do you want to load a save or a new Map? (Map/Save)")

if choose_map.lower() == "map":
    sel_map = input("Please Input the map files full name. (/Maps) ")
    if sel_map:
        WITS_MAP_LOCATION = f"../Maps/{sel_map}"
elif choose_map.lower() == "saves":
    sel_save = input("Please Input a save files name. (/Saves) ")
    if sel_save:
        WITS_MAP_LOCATION = f"../Saves/{sel_save}"


map_reader = Reader(map_location=WITS_MAP_LOCATION, map_spawn_location=(0,0))
map_logic = Logic(reader=map_reader, spawn_points=(0,0), battlefield_path=BATTLEFIELD_LEGEND_PATH)

first_player = map_logic.players[0]
location_chain = ((0,1), (0,2), (1,3), (2,4), (3,5))

can_move_to_loc = map_logic.can_move_to_location(location_chain=location_chain, player=first_player)


convertor = Convertor(one_list=map_logic.player_can_pass_array, zero_list=[""])
new_cv =convertor.convert_df_to_astar(df=map_logic.reader.dataframe)
print(new_cv)
astar_example = Classes.astar.example(maze=new_cv, print_maze=True, start=first_player.location, end=(0,4))
print(astar_example)

if can_move_to_loc:
    print(first_player.location)
    map_logic.move_to_location(player=first_player, new_location=location_chain[-1])
    print(first_player.location)
    map_logic.reader.save_match()
