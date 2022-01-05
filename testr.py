import re
import numpy as np
import pandas as pd


def pandas_things():
    desired_width = 320
    pd.set_option('display.width', desired_width)
    np.set_printoptions(linewidth=desired_width)
    pd.set_option('display.max_columns', 10)

    df = pd.read_csv('Project Saves/Date 05.01.2022/Time 11.15.50/lineup 11.16.28.csv')
    df2 = df.drop(['photoFolderIndex', 'photo', 'shortName'], axis=1)

    df2['positions'] = df2['positions'].apply(lambda x: re.sub(r'[^a-zA-Z, ]+', '', x))
    print(df2)


pandas_things()
