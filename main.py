# import logging
import numpy

from Classes.logic_handler import Logic
from Classes.map_reader import Reader
from Classes.Convertor import Convertor
from Classes.Turns import Turns
import os

print(f"PWD: {os.getcwd()}")

WITS_MAP_LOCATION = "Maps/wits-testimony.csv"
BATTLEFIELD_LEGEND_PATH = "mappings/battlefield_legend.json"

choose_map = input("Do you want to load a save or a new Map? (Map/Save) ")

if choose_map.lower() == "map":
    sel_map = input("Please Input the map files full name. (/Maps) ")
    if sel_map:
        WITS_MAP_LOCATION = f"Maps/{sel_map}"
elif choose_map.lower() == "saves":
    sel_save = input("Please Input a save files name. (/Saves) ")
    if sel_save:
        WITS_MAP_LOCATION = f"Saves/{sel_save}"

map_reader = Reader(map_location=WITS_MAP_LOCATION, map_spawn_location=(0, 0))
map_logic = Logic(reader=map_reader, spawn_points=(0, 0), battlefield_path=BATTLEFIELD_LEGEND_PATH)


convertor = Convertor(one_list=map_logic.player_can_pass_array, zero_list=[""])
turns = Turns(logic=map_logic, convertor=convertor)

while True:
    # Infinity Turns
    turns.turn_new()




# if can_move_to_loc:
#     print(first_player.location)
#     map_logic.move_to_location(player=first_player, new_location=location_chain[-1])
#     print(first_player.location)
#     map_logic.reader.save_match()
