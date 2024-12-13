import logging
import csv
from pandas import read_csv
from Classes.get_battle_field_json import get_battle_field
import Classes.player


def get_list_of_players(path: str = "../mappings/players.csv", spawn_location: tuple = (0, 0)):
    players = []
    with open(file=path, mode='r') as file:
        # Create a DictReader object
        reader = csv.DictReader(file)

        # Convert the reader to a list of dictionaries
        dict_list = list(reader)

    for player in dict_list:
        new_player = Classes.player.Player(spawn=spawn_location, data=player)
        players.append(new_player)
    return players


class Logic:
    def __init__(self, reader, spawn_points: tuple, battlefield_path: str):
        self.reader = reader
        self.player_spawn_points = spawn_points
        self.battlefield_legend = get_battle_field(battlefield_path)
        self.player_can_land_array = self.battlefield_legend["main"]["cannot_end"]
        self.player_can_pass_array = self.battlefield_legend["main"]["unpassable"]
        self.settings = self.reader.settings

        self.players = get_list_of_players(spawn_location=self.player_spawn_points[0])

    def can_move_to_location(self, location_chain: tuple):
        """
        This function Checks if the player can move to a specified location.
        :param location_chain:
        :return:
        """
        if len(location_chain) > self.settings["map"]["amount_of_cells_per_turn"]:
            logging.error(msg=f"location chain too long (longer than 5). Value: {location_chain}")
            return False

        end_point = location_chain[-1]
        if end_point in self.player_can_land_array or end_point in self.player_can_land_array:
            logging.error(msg="cannot land on mapping 'cannot_end' charachter")
            return False

        logging.log(level=logging.DEBUG, msg="Last Point of movement chain check passed.")
        logging.log(level=logging.DEBUG, msg=f"lenght of location chain: {len(location_chain)}")
        for location_tuple in location_chain:
            returned_location = self.reader.get_cell_from_location(location_tuple)
            if not returned_location:
                logging.error(msg=f"returned location does not exist. value: {returned_location}")
                return False

            if returned_location in self.battlefield_legend["main"]["unpassable"]:
                logging.error(msg=f"cannot go through mapping 'unpassable'. Value: {returned_location}")
                return False
