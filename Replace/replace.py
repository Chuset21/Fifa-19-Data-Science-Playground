import pandas as pd


class Replace:
    _REPLACE_DICT = {'[kK]': '*1e3', '[mM]': '*1e6', '[bB]': '*1e9'}

    @staticmethod
    def convert_to_int(x):
        return x.replace(Replace._REPLACE_DICT, regex=True).map(pd.eval).astype(int)

    @staticmethod
    def remove_euro_symbol(df, key_name):
        return df[key_name].replace(r'[€,]', '', regex=True)

    @staticmethod
    def convert_to_int_and_remove_euro_symbol(df, key_name):
        return Replace.convert_to_int(Replace.remove_euro_symbol(df, key_name))
