import json


def get_battle_field(path: str) -> dict:
    """
    turns a path from the battlefield json to a dict
    :param path:
    :return:
    """
    with open(file=path, mode="r") as file:
        return json.load(file)
