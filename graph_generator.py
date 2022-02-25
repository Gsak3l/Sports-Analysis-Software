import pandas as pd
import matplotlib.pyplot as plt


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


def all_game_single_player_actions(csv_file, name):
    df = pd.read_csv(csv_file)
    df = df[df['Name'] == name]

    action_count = df.Action.value_counts()
    action_names = df['Action'].drop_duplicates()

    plt.title(f'{name} actions during the entire game')
    plt.pie(action_count, labels=action_names, autopct=lambda p: f'{p * sum(action_count) / 100 :.0f}')
    # plt.pie(action_count, labels=action_names, autopct=lambda p: f'{p:.2f}%, {p * sum(action_count) / 100 :.0f} items')
    plt.axis('equal')
    plt.show()


all_game_single_player_actions('Project Saves/Date 24.02.2022/Time 10.53.44/actions.csv', 'Arjen Robben')
# all_game_all_player_actions('Project Saves/Date 24.02.2022/Time 10.53.44/actions.csv')
