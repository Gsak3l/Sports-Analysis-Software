import pandas as pd
import matplotlib.pyplot as plt


def action_timestamp(csv_file):
    df = pd.read_csv(csv_file)

    action = df.Action
    timestamp = df.Timestamp
    name = df.Name

    plt.xlabel('Action')
    plt.ylabel('Timestamp')

    plt.plot(timestamp, action)
    plt.xticks(timestamp, rotation=90)

    for i, label in enumerate(name):
        plt.annotate(label, (timestamp[i], action[i]))

    plt.show()


action_timestamp('Project Saves/Date 24.02.2022/Time 10.53.44/actions.csv')
