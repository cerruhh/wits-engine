import logging
from Classes.get_battle_field_json import get_battle_field


class Logic:
    def __init__(self, reader, spawn_points: tuple, battlefield_path: str):
        self.reader = reader
        self.player_spawn_points = spawn_points
        self.battlefield_legend = get_battle_field(battlefield_path)
        self.player_can_land_array = self.battlefield_legend["main"]["cannot_end"]
        self.player_can_pass_array = self.battlefield_legend["main"]["unpassable"]

    def can_move_to_location(self, location_chain: tuple):
        """
        This function Checks if the player can move to a specified location.
        :param location_chain:
        :return:
        """
        if len(location_chain) > 5:
            logging.error(msg=f"location chain too long (longer than 5). Value: {location_chain}")
            return False

        end_point = location_chain[-1]
        if end_point in self.player_can_land_array or end_point in self.player_can_land_array:
            logging.error(msg="cannot land on mapping 'cannot_end' charachter")
            return False

        logging.log(level=5, msg="Last Point of movement chain check passed.")
        logging.log(level=5, msg=f"lenght of location chain: {location_chain}")
        for location_tuple in location_chain:
            returned_location = self.reader.get_cell_from_location(location_tuple)
            if not returned_location:
                logging.error(msg=f"returned location does not exist. value: {returned_location}")
                return False

            if returned_location in self.battlefield_legend["main"]["unpassable"]:
                logging.error(msg=f"cannot go through mapping 'unpassable'. Value: {returned_location}")
                return False
