import logging
import csv
from pandas import read_csv
from Classes.get_battle_field_json import get_battle_field
import Classes.player
import Classes.map_reader


def get_list_of_players(path: str = "mappings/players.csv", spawn_location: tuple = (0, 0)) -> list:
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
    def __init__(self, reader: Classes.map_reader.Reader, spawn_points: tuple, battlefield_path: str) -> None:
        self.reader = reader
        self.player_spawn_points = spawn_points
        self.battlefield_legend = get_battle_field(battlefield_path)
        self.player_can_land_array = self.battlefield_legend["main"]["cannot_end"]
        self.settings = self.reader.settings

        self.players = get_list_of_players(spawn_location=self.player_spawn_points[0])
        self.player_can_pass_array = self.battlefield_legend["main"]["unpassable"]
        for i in self.players:
            self.player_can_pass_array.append(i.icon)

    def can_move_to_location(self, location_chain: tuple, player: Classes.player.Player, desired_location: str) -> bool:
        """
        This function Checks if the player can move to a specified location.
        :param desired_location:
        :param player:
        :param location_chain:
        :return:
        """

        if len(location_chain) > self.settings["map"]["amount_of_cells_per_turn"]:
            logging.error(msg=f"location chain too long (longer than 5). Value: {location_chain}")
            return False

        if desired_location in self.player_can_land_array or desired_location in self.player_can_land_array:
            logging.error(msg="cannot land on mapping 'cannot_end' charachter")
            return False

        logging.log(level=logging.DEBUG, msg="Last Point of movement chain check passed.")
        logging.log(level=logging.DEBUG, msg=f"lenght of location chain: {len(location_chain)}")
        for location_tuple in location_chain:
            returned_location = self.reader.get_cell_from_location(location_tuple)
            if not returned_location:
                logging.error(msg=f"returned location does not exist. value: {returned_location}")
                return False

            if returned_location in self.player_can_pass_array:
                logging.error(msg=f"cannot go through mapping 'unpassable'. Value: {returned_location}")
                return False

            if player.can_move_to_location(new_location=location_tuple):
                return True

    def move_to_location(self, new_location: tuple, player: Classes.player.Player) -> bool:
        if not player or not new_location:
            logging.error(msg="Player Or new_location are undefined.")
            return False

        if len(new_location) != 2:
            logging.error("new location tuple is more than 2 coordinates.")

        self.reader.change_map_geometry(geometry_location=player.location, object_to_change_to="")
        logging.log(level=logging.DEBUG, msg="Set Players Old location to ''.")
        self.reader.change_map_geometry(geometry_location=new_location, object_to_change_to=player.icon)
        logging.log(level=logging.DEBUG, msg=f"Set Players New location to players desired icon: {player.icon}")
        player.location = new_location

        if self.reader.get_cell_from_location(geometry_location=new_location) != player.icon:
            logging.warning(msg="New location does not contain the players icon!")

        return True
