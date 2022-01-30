import os

import pandas as pd

import filesystem_changes as fc
import string_manipulation as sm
import re


def find_last_folder_lineups():
    all_files = os.listdir('Project Saves/Date 30.01.2022/Time 10.41.39')
    lineups = []

    for file in all_files:
        if re.search(r'\blineup\b', file):
            lineups.append('Project Saves/Date 30.01.2022/Time 10.41.39/' + file)

    return lineups


new_lineups = find_last_folder_lineups()

start = end = 0

for csv in new_lineups:
    df_csv = pd.read_csv(csv)
    end += df_csv.shape[0]
    for i in range(start, end):
        print(end - start)
    start += df_csv.shape[0]



