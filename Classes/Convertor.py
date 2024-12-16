import pandas
import numpy


class Convertor:
    def __init__(self, one_list: list, zero_list: list):
        self.onelist = one_list
        self.zerolist = zero_list

    def convert_df_to_astar(self, df: pandas.DataFrame):
        df = df.fillna("")
        for i in self.onelist:
            df = df.replace(i, value=1)

        for i in self.zerolist:
            df = df.replace(i, value=0)

        df = df.fillna(0)
        mz_array = df.to_numpy()

        #       mz_array = [[element * 2 for element in row] for row in mz_array]

        mz_array = numpy.repeat(mz_array, 2, axis=0)

        return mz_array

    def convert_astar_to_xy(self, tuples_list: list = None):
        """
        Swaps a tuple
        :param tuples_list:
        :return:
        """
        swapped_tuples_list = [(y, x) for x, y in tuples_list]
        return swapped_tuples_list
