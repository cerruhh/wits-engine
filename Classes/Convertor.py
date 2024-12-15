import pandas
import numpy


class Convertor:
    def __init__(self, one_list:list, zero_list:list):
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

        mz_array = numpy.repeat(mz_array, 2, axis=0)

        return mz_array
