import csv
from pandas import read_csv, DataFrame
import logging
import tomllib


def import_settings(path: str = "../mappings/settings.toml"):
    """
    import the settings.toml file from the mappings
    :param path:
    :return:
    """
    with open(file=path, mode="rb") as settings_file:
        settings = tomllib.load(settings_file)
        return settings


class Reader:
    """
    Reads Map Files.
    map_location is the location of the map on your disk
    map_spawn is the spawn point for the player

    Generally responsible for lower level tasks to do with the map geometry
    """

    def __init__(self, map_location: str, map_spawn_location: tuple = (0, 0)):
        """
        Initalizse values map location as in the path to the .csv file
        map_spawn is the main_spawn of the map, if none is given.
        :param map_location:
        :param map_spawn_location:
        """
        self.map_location = map_location
        self.map_spawn = map_spawn_location
        self.settings = import_settings(path="../mappings/settings.toml")
        self.dataframe = read_csv(self.map_location, dtype=object)

        logging.basicConfig(level=self.settings["developer"]["loglevel"])



    def change_map(self, map_location: str):
        """
        Changes the map currently used
        :param map_location:
        :return:
        """
        self.dataframe = read_csv(map_location, dtype=object)

    def change_map_geometry(self, geometry_location: tuple, object_to_change_to: str):
        """
        Changes a piece of the map by coordinate to a given object.
        :param geometry_location:
        :param object_to_change_to:
        :return:
        """
        if len(object_to_change_to) != 1:
            logging.log(msg="Object to change to was longer than 1 charachter, likely an emoji.", level=logging.DEBUG)

        elif len(geometry_location) != 2:
            logging.error(msg="geometry location tuple lenght was not 2. exiting")
            exit(1)

        change_cell = self.dataframe.iloc[geometry_location[0] + 1,geometry_location[1] + 1]
        logging.log(level=logging.DEBUG, msg=f"Cell to be changed: {change_cell}")

        if not change_cell:
            logging.error(f"Cell to be changed does not exist. value = {change_cell}")
            exit(1)

        self.dataframe.iloc[geometry_location[0] + 1, geometry_location[1] + 1] = object_to_change_to
        logging.log(msg=f"Cell changed {change_cell} -> {object_to_change_to}", level=logging.DEBUG)

    def get_cell_from_location(self, geometry_location: tuple):
        """
        Returns a cell from coordinates.
        :param geometry_location:
        :return:
        """
        if len(geometry_location) != 2:
            logging.error(
                msg=f"Trying to get location of cell from more than 2 coordinates. value: {geometry_location}")
            exit(1)

        get_location = self.dataframe.iloc[geometry_location[0] + 1, geometry_location[1] + 1]
        if not get_location:
            logging.error(msg=f"location does not exist. value: {geometry_location}")
            exit(1)

        return self.dataframe.iloc[geometry_location[0] + 1, geometry_location[1] + 1]
