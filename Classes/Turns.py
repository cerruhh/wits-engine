import logging
import Classes.logic_handler
import Classes.Convertor
import Classes.astar
from random import randint


class Turns:
    def __init__(self, logic:Classes.logic_handler.Logic, convertor:Classes.Convertor.Convertor):
        self.logic = logic
        self.turn = 0
        self.players = logic.players
        self.convertor = convertor

    def turn_new(self):
        print(f"Current Turn: {self.turn}")
        amount_of_cells_to_move = self.logic.settings["map"]["amount_of_cells_per_turn"]
        for player in self.players:
            for _i in range(amount_of_cells_to_move):
                print(f"The current player: {player.name} ({player.username})")
                print(f"You current location is: {player.location}")
                where_to_move = input("Where would you like to move? (eg. 2,3) ")
                move_split = where_to_move.split(sep=",")
                if len(move_split) != 2:
                    logging.error(msg="move split longer than 2, exiting")
                logging.log(level=logging.DEBUG, msg="move location valid")

                new_cv = self.convertor.convert_df_to_astar(df=self.logic.reader.dataframe)
                astar_example = Classes.astar.example(maze=new_cv, print_maze=False, start=(int(move_split[0]), int(move_split[1])),
                                                      end=(0, 4))
                final_path = self.convertor.convert_astar_to_xy(tuples_list=astar_example)

                logging.log(msg=f"Final path: {final_path}", level=logging.DEBUG)
                if not final_path:
                    print("Try again.")
                    exit()

                if self.logic.can_move_to_location(location_chain=final_path, player=player):
                    self.logic.move_to_location(player=player, new_location=final_path[-1])


    def roll_the_dice(self):
        dice_sides = self.logic.settings["map"]["dice_sides"]
        return randint(a=0, b=dice_sides)
