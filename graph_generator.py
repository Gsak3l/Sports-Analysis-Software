import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import filesystem_changes


# ALL ACTIONS THAT TOOK PLACE DURING THE ENTIRE GAME
def all_game_all_player_actions(csv_file):
    df = pd.read_csv(csv_file)

    action = df.Action
    timestamp = df.Timestamp
    name = df.Name

    plt.title('All actions during the entire game')
    plt.xlabel('Action')
    plt.ylabel('Timestamp')

    plt.plot(timestamp, action)
    plt.xticks(timestamp, rotation=90)

    for i, label in enumerate(name):
        plt.annotate(label, (timestamp[i], action[i]))

    plt.show()


# ALL ACTIONS A SPECIFIC PLAYER DID DURING THE GAME
def all_game_single_player_actions(csv_file, name):
    df = pd.read_csv(csv_file)
    df = df[df['Name'] == name]

    action_count = df.Action.value_counts()
    action_names = df['Action'].drop_duplicates()

    plt.title(f'{name} actions during the entire game')
    plt.pie(action_count, labels=action_names, autopct=lambda p: f'{p * sum(action_count) / 100 :.0f}')
    plt.axis('equal')
    plt.show()


def all_game_specific_action(csv_file, action):
    df = pd.read_csv(csv_file)
    df = df[df['Action'] == action]

    player_count = df.Name.value_counts()
    player_names = df['Name'].drop_duplicates()

    plt.bar(player_names, player_count)
    plt.xticks(np.arange(len(player_count)))
    plt.show()

    # plt.title(f'{action} actions during the entire game')
    # plt.pie(player_count, labels=player_names, autopct=lambda p: f'{p * sum(player_count) / 100 :.0f}')
    # plt.axis('equal')
    # plt.show()


all_game_specific_action('Project Saves/Date 24.02.2022/Time 10.53.44/actions.csv', 'Long Pass')
# all_game_single_player_actions(filesystem_changes.find_last_created_folder() + 'actions.csv', 'Arjen Robben')
# all_game_all_player_actions(filesystem_changes.find_last_created_folder() + 'actions.csv')