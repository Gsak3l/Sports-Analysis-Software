import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import string_manipulation as sm


# ALL ACTIONS THAT TOOK PLACE DURING THE ENTIRE GAME
def all_game_all_player_actions(csv_file):
    df = pd.read_csv(csv_file)

    action = df.Action
    timestamp = df.Timestamp
    name = df.Name

    plt.title('All actions during the entire game')
    plt.xlabel('Action')
    plt.ylabel('Timestamp')

    plt.plot(timestamp, action, 'o')
    plt.xticks(timestamp, rotation=90)

    for i, label in enumerate(name):
        plt.annotate(label, (timestamp[i], action[i]), rotation=45)

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

# all_game_action_family('Project Saves/Date 24.02.2022/Time 10.53.44/actions.csv', 'Passing Game')
# all_game_specific_action('Project Saves/Date 24.02.2022/Time 10.53.44/actions.csv', 'Long Pass')
# all_game_single_player_actions('Project Saves/Date 02.03.2022/Time 09.23.44/actions.csv', '1')
# all_game_all_player_actions('Project Saves/Date 08.05.2022/Time 17.08.31/actions.csv')
