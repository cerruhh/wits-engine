import logging
import Classes.logic_handler
import Classes.Convertor
import Classes.astar
from random import randint


class Turns:
    def __init__(self, logic: Classes.logic_handler.Logic, convertor: Classes.Convertor.Convertor):
        self.logic = logic
        self.turn = 0
        self.players = logic.players
        self.convertor = convertor

    def turn_new(self):
        print(f"Current Turn: {self.turn}")
        self.turn += 1
        amount_of_cells_to_move = self.logic.settings["map"]["amount_of_cells_per_turn"]
        for player in self.players:
            print(f"The current player: {player.name} ({player.username})")
            print(f"You current location is: {player.location}")
            while True:
                where_to_move = input("Where would you like to move? (eg. 2,3) ")
                move_split = where_to_move.split(sep=",")
                if len(move_split) != 2:
                    logging.error(msg="move split longer than 2, exiting")
                    logging.log(level=logging.DEBUG, msg="move location valid")

                desired_location = (int(move_split[0]), int(move_split[1]))
                logging.log(msg=f"desired location: {desired_location}", level=logging.DEBUG)
                new_cv = self.convertor.convert_df_to_astar(df=self.logic.reader.dataframe)
                astar_example = Classes.astar.example(maze=new_cv, print_maze=False,
                                                      start=player.location,
                                                      end=desired_location)
                final_path = self.convertor.convert_astar_to_xy(tuples_list=astar_example)

                logging.log(msg=f"Final path: {final_path}", level=logging.DEBUG)
                if not final_path:
                    print("Try again.")
                    break
                cell_at_desired_location = self.logic.reader.get_cell_from_location(geometry_location=desired_location)
                if self.logic.can_move_to_location(location_chain=final_path, player=player, desired_location=self.logic.reader.get_cell_from_location(desired_location)):
                    logging.log(msg=f"cell_at_desired_loc: {cell_at_desired_location}",level=logging.DEBUG)
                    self.logic.move_to_location(player=player, new_location=desired_location)
                    print(f"You have successfully moved to location {desired_location}")
                    break
                else:
                    logging.log(msg=f"cell_at_desired_loc: {self.logic.reader.get_cell_from_location(geometry_location=desired_location)}", level=logging.DEBUG)
                    print(f"Cannot move to wanted location, try again!")
                    print(f"Cell at wanted location: {cell_at_desired_location}")
                    continue

    def roll_the_dice(self):
        dice_sides = self.logic.settings["map"]["dice_sides"]
        return randint(a=0, b=dice_sides)
