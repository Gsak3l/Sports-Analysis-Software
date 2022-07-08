import json
import pickle
import glob
import os

import pandas as pd

import filesystem_changes as fc
import string_manipulation as sm


# create the export pickle file
def make_pickle():
    details = f'{fc.find_last_created_folder()}game details.json'
    lineups = glob.glob(os.path.join(fc.find_last_created_folder(), '*lineup*'))
    actions = f'{fc.find_last_created_folder()}actions.csv'

    with open(details) as f:
        details = json.load(f)
    f.close()

    with open(f'{fc.downloads_path()}/fileExport.sports', 'wb') as fp:
        pickle.dump(details, fp)
        for lineup in lineups:
            df = pd.read_csv(lineup)
            pickle.dump(df.to_dict('records'), fp)
        df = pd.read_csv(actions)
        pickle.dump(df.to_dict('records'), fp)

    fp.close()


# this will at some point allow to import pickle files to the program
def read_pickle():
    lines = []
    with (open(f'{fc.downloads_path()}/fileExport.sports', 'rb')) as openfile:
        while True:
            try:
                lines.append(pickle.load(openfile))
            except EOFError:
                break

    details = []
    actions = []
    lineups = []

    # keeping only details
    for det in lines[0]:
        details.append(lines[0][det])
    lines.pop(0)

    # keeping only names, family actions,actions, timestamps
    for act in lines[2]:
        a_list = []
        for a in act:
            a_list.append([a, act[a]])
        actions.append(a_list)
    lines.pop(2)

    actions2 = []
    for act in actions:
        [actions2.append(act[i][1]) for i in range(4)]
    actions = actions2

    # we'll see
    for line in lines:
        for l1 in line:
            l3 = []
            for l2 in l1:
                l3.append(l1[l2])
            lineups.append(l3)
    #
    return details, lineups, actions


read_pickle()
