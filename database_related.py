import uuid
import json
import glob
import os

import pymongo
import pandas as pd

import filesystem_changes as fc


# ADDS GAME DETAILS TO THE DATABASE
def details_to_db():
    details_path = f'{fc.find_last_created_folder()}game details.json'

    with open(details_path) as f:
        details_ = json.load(f)
    details_['Game ID'] = game_id
    details.insert_one(details_)


# ADDS ACTIONS TO THE DATABASE
def actions_to_db():
    df = pd.read_csv(f'{fc.find_last_created_folder()}actions.csv')
    df['Game ID'] = game_id
    df = df[['Game ID', 'Name', 'Action Family', 'Action', 'Timestamp']]
    actions.insert_many(df.to_dict('records'))


# ADDS LINEUPS TO THE DATABASE
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


# RETURNS INFO ABOUT A SPECIFIC GAME GIVEN THE GAME ID
def return_all_actions(game_id_):
    acts = []
    for act in actions.find({'Game ID': game_id_}):
        acts.append(act)

    return acts


# RETURN ACTIONS A GIVEN PLAYER DID, ON A SPECIFIC GAME
def return_player_actions(game_id_, player_name_):
    player_actions = []
    for act in actions.find({'Game ID': game_id_, 'Name': player_name_}):
        player_actions.append(act)

    return player_actions


# RETURN ALL PLAYERS THAT DID A SPECIFIC ACTION
def return_specific_action(game_id_, action_):
    game_actions = []
    for act in actions.find({'Game ID': game_id_, 'Action': action_}):
        game_actions.append(act)

    return game_actions


# RETURN ALL ACTIONS THAT BELONG TO A GIVEN ACTION FAMILY, E.G. DEFENSE
def return_family_action(game_id_, family):
    action_family = []
    for act in actions.find({'Game ID': game_id_, 'Action Family': family}):
        action_family.append(act)

    return action_family


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
