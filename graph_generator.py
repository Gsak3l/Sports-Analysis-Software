import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import database_related as dr
import string_manipulation as sm


# ALL ACTIONS THAT TOOK PLACE DURING THE ENTIRE GAME
def all_game_all_player_actions(csv_file, game_id):
    if csv_file is not None:
        # using the csv file
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(dr.return_all_actions(game_id))

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


# ALL ACTIONS A SPECIFIC PLAYER DID DURING THE GAME
def all_game_single_player_actions(csv_file, game_id, name):
    if csv_file is not None:
        # using the csv file
        df = pd.read_csv(csv_file)
    else:
        # using the database
        df = pd.DataFrame(list(dr.return_player_actions(game_id, name)))

    # creating the plot
    df = df[df['Name'] == sm.string_to_int_or_pass(name)]

    action_count = df.Action.value_counts()
    action_names = df['Action'].drop_duplicates()

    plt.title(f'{name} actions during the entire game')
    plt.pie(action_count, labels=action_names, autopct=lambda p: f'{p * sum(action_count) / 100 :.0f}')
    plt.axis('equal')
    plt.show()


# SPECIFIED ACTION AND COUNTER PER PLAYER
def all_game_specific_action(csv_file, game_id, action):
    if csv_file is not None:
        # using csv file
        df = pd.read_csv(csv_file)
    else:
        # using the database
        df = pd.DataFrame(list(dr.return_specific_action(game_id, action)))

    df = df[df['Action'] == action]

    player_count = df.Name.value_counts()
    player_names = df['Name'].drop_duplicates()

    plt.title(f'{action} per player')
    plt.bar(player_names, player_count)
    plt.xticks(np.arange(len(player_count)))
    plt.show()


def all_game_action_family(csv_file, game_id, family):
    if csv_file is not None:
        # using csv file
        df = pd.read_csv(csv_file)
    else:
        # using database
        df = pd.DataFrame(list(dr.return_family_action(game_id, family)))

    df = df[df['Action Family'] == family]

    action_count = df.Action.value_counts()
    action_names = df['Action'].drop_duplicates()

    plt.title(family)
    plt.pie(action_count, labels=action_names, autopct=lambda p: f'{p * sum(action_count) / 100 :.0f}')
    plt.axis('equal')
    plt.show()

# all_game_action_family(None, 'cde3c012-eda0-40ec-b09f-b83791e774b2', 'Defensive Game')
# all_game_specific_action(None, 'cde3c012-eda0-40ec-b09f-b83791e774b2', 'Tackle in Defensive Zone')
# all_game_single_player_actions('Robert Lewandowski', None, 'cde3c012-eda0-40ec-b09f-b83791e774b2')
# all_game_all_player_actions(None, 'cde3c012-eda0-40ec-b09f-b83791e774b2')
