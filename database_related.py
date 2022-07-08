import uuid
import json
import glob
import os

import pymongo
import pandas as pd

import filesystem_changes as fc
# import string_manipulation as sm


def details_to_db():
    details_path = f'{fc.find_last_created_folder()}game details.json'
    # details_path = sm.double_backslash_to_slash(details_path) # windows path thing

    with open(details_path) as f:
        details_ = json.load(f)
    details_['Game ID'] = game_id
    details.insert_one(details_)


def actions_to_db():
    df = pd.read_csv(f'{fc.find_last_created_folder()}actions.csv')
    df['Game ID'] = game_id
    df = df[['Game ID', 'Name', 'Action Family', 'Action', 'Timestamp']]
    actions.insert_many(df.to_dict('records'))


def lineup_to_db():
    all_lineups = glob.glob(os.path.join(fc.find_last_created_folder(), '*lineup*'))
    for single_lineup in all_lineups:
        lineup_id = str(uuid.uuid4())

        df = pd.read_csv(single_lineup)

        df.rename(columns={'id': 'Player ID'}, inplace=True)
        df.rename(columns={'name': 'Name'}, inplace=True)
        df.rename(columns={'rating': 'Rating'}, inplace=True)
        df.rename(columns={'positions': 'Positions'}, inplace=True)

        df['Game ID'] = game_id
        df['Lineup ID'] = lineup_id
        df = df[['Game ID', 'Lineup ID', 'Player ID', 'Name', 'Rating', 'Positions']]

        lineup.insert_many(df.to_dict('records'))


def everything_to_db():
    details_to_db()
    actions_to_db()
    lineup_to_db()


game_id = str(uuid.uuid4())

client = pymongo.MongoClient()
database = client['football-db']
actions = database['player-actions']
lineup = database['lineup']
details = database['details']
