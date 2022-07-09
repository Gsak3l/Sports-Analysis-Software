import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import database_related as dr
import string_manipulation as sm


# ALL ACTIONS THAT TOOK PLACE DURING THE ENTIRE GAME
def all_game_all_player_actions(csv_file=None, game_id=None):
    if csv_file is not None:
        # using the csv file
        df = pd.read_csv(csv_file)

        name = df.Name
        action = df.Action
        timestamp = df.Timestamp

        plt.title('All actions during the entire game')
        plt.xlabel('Action')
        plt.ylabel('Timestamp')

        plt.plot(timestamp, action, 'o')
        plt.xticks(timestamp, rotation=90)

        for i, label in enumerate(name):
            plt.annotate(label, (timestamp[i], action[i]), rotation=75)

        plt.show()

    else:
        # using the database
        name, _, action, timestamp = dr.return_actions(game_id)

        plt.title('All actions during the entire game')
        plt.xlabel('Action')
        plt.ylabel('Timestamp')

        plt.plot(timestamp, action, 'o')
        plt.xticks(timestamp, rotation=90)

        for i in range(len(name)):
            plt.annotate(name[i], (timestamp[i], action[i]), rotation=75)

        plt.show()


# ALL ACTIONS A SPECIFIC PLAYER DID DURING THE GAME
def all_game_single_player_actions(csv_file, name):
    df = pd.read_csv(csv_file)
    df = df[df['Name'] == sm.string_to_int_or_pass(name)]

    action_count = df.Action.value_counts()
    action_names = df['Action'].drop_duplicates()

    plt.title(f'{name} actions during the entire game')
    plt.pie(action_count, labels=action_names, autopct=lambda p: f'{p * sum(action_count) / 100 :.0f}')
    plt.axis('equal')
    plt.show()


# SPECIFIED ACTION AND COUNTER PER PLAYER
def all_game_specific_action(csv_file, action):
    df = pd.read_csv(csv_file)
    df = df[df['Action'] == action]

    player_count = df.Name.value_counts()
    player_names = df['Name'].drop_duplicates()

    plt.title(f'{action} per player')
    plt.bar(player_names, player_count)
    plt.xticks(np.arange(len(player_count)))
    plt.show()


def all_game_action_family(csv_file, family):
    df = pd.read_csv(csv_file)
    df = df[df['Action Family'] == family]

    action_count = df.Action.value_counts()
    action_names = df['Action'].drop_duplicates()

    plt.title(family)
    plt.pie(action_count, labels=action_names, autopct=lambda p: f'{p * sum(action_count) / 100 :.0f}')
    plt.axis('equal')
    plt.show()

# all_game_action_family('Project Saves/Date 27.05.2022/Time 09.44.02/actions.csv', 'Offensive Game')
# all_game_specific_action('Project Saves/Date 27.05.2022/Time 09.44.02/actions.csv', 'Tackle')
# all_game_single_player_actions('Project Saves/Date 27.05.2022/Time 09.44.02/actions.csv', '1')
# file_all_game_all_player_actions(None, 'cde3c012-eda0-40ec-b09f-b83791e774b2')
