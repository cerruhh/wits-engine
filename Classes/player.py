import logging
# def get_player_csv(path: str = "../mappings/players.csv"):
#     with open(file=path, mode="r") as file:
#         return read_csv(path)


def get_data_list_from_init(items: str) -> list:
    """
    makes a list from items that the player owns, and turns it into an array.
    :param items:
    :return:
    """
    new_dict = []
    for item in items.split(sep=","):
        item_split = item.split(sep="|")
        appendable = {"item": item_split[0], "weight": int(item_split[1])}
        new_dict.append(appendable)
    return new_dict


def calculate_weight(items: list) -> int:
    """
    calculates the weight of a player by adding all items weight values togheter
    :param items:
    :return:
    """
    total_weight = 0
    for item in items:
        total_weight += item["weight"]
    return total_weight


class Player:
    def __init__(self, spawn: tuple, data: dict):
        """
        Initalize all values that logic needs to calculate rounds of wits
        :param spawn:
        :param data:
        """
        self.spawn = spawn
        self.data = data

        self.username = data["Username"]
        self.name = data["Name"]
        self.items = get_data_list_from_init(items=data["Items"])
        self.username = data["Username"]
        self.icon = data["Icon"]
        self.location = (int(data["Location"].split(sep=",")[0]), int(data["Location"].split(sep=",")[1]))
        self.health = data["Health"]
        self.max_health = data["Max Health"]
        #       print(self.items)
        self.weight = calculate_weight(items=self.items)

    def can_move_to_location(self, new_location: tuple) -> bool:
        """
        Calculates if the player can move to a given location of a chain.
        Returns true if the new location is touching the player.
        :param new_location:
        :return:
        """

        dx = abs(new_location[0] - self.location[0])
        dy = abs(new_location[1] - self.location[1])

        if dx == 0 and dy == 0:
            logging.error("Moving to same location")
            return False

        if dx > 1 or dy > 1:
            return False

        # All checks passed
        self.location = new_location
        return True

    def move_to_new_location(self, new_location: tuple):
        pass
