import logging
import Classes.logic_handler
from random import randint


class Turns:
    def __init__(self, logic:Classes.logic_handler.Logic):
        self.logic = logic
        self.turn = 0
        self.players = logic.players

    def turn_new(self):
        print(f"Current Turn: {self.turn}")
        amount_of_cells_to_move = self.logic.settings["map"]["amount_of_cells_per_turn"]
        for player in self.players:
            for _i in range(__stop=amount_of_cells_to_move):
                print(f"You current location is: {player.location}")
                where_to_move = input("Where would you like to move? (eg. 2,3) ")
                move_split = where_to_move.split(sep=",")
                if len(move_split) != 2:
                    logging.error(msg="move split longer than 2, exiting")
                logging.log(level=logging.DEBUG, msg="move location valid")

#               if self.logic.can_move_to_location(location_chain=)


    def roll_the_dice(self):
        dice_sides = self.logic.settings["map"]["dice_sides"]
        return randint(a=0, b=dice_sides)
