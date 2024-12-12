import csv
from pandas import read_csv, DataFrame
import logging


class Reader:
    """
    Reads Map Files.
    map_location is the location of the map on your disk
    map_spawn is the spawn point for the player
    """

    def __init__(self, map_location: str, map_spawn_location: tuple):
        self.map_location = map_location
        self.map_spawn = map_spawn_location

        self.dataframe = read_csv(self.map_location)

    def change_map(self, map_location: str):
        self.dataframe = read_csv(map_location)

    def change_map_geometry(self, geometry_location: tuple, object_to_change_to: str):
        if len(object_to_change_to) != 1:
            logging.error(msg="Object to change to was longer than 1 charachter")
            exit(1)
        elif len(geometry_location) != 2:
            logging.error(msg="geometry location tuple lenght was not 2. exiting")
            exit(1)

        change_cell = self.dataframe.iloc[geometry_location[0]][geometry_location[1]]
        logging.log(level=1, msg=f"Cell to be changed: {change_cell}")

        if not change_cell:
            logging.error(f"Cell to be changed does not exist. value = {change_cell}")
            exit(1)

        self.dataframe.iloc[geometry_location] = object_to_change_to
        logging.log(msg=f"Cell changed {change_cell} -> {object_to_change_to}", level=1)

    def get_cell_from_location(self, geometry_location:tuple):
        if len(geometry_location) != 2:
            logging.error(msg=f"Trying to get location of cell from more than 2 coordinates. value: {geometry_location}")
            exit(1)

        get_location = self.dataframe.iloc[geometry_location]
        if not get_location:
            logging.error(msg=f"location does not exist. value: {geometry_location}")
            exit(1)
