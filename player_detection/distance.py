import pandas as pd


def read_n_clean(file):
    df = pd.read_csv(file, sep=' ', header=None)
    df = df.rename(columns={0: 'Frame', 1: 'ID', 2: 'x', 3: 'y', 4: 'w', 5: 'h'})
    df = df.dropna(axis='columns')
    df = df.drop([6, 7, 8, 9], axis=1)
    print(df)


if __name__ == '__main__':
    read_n_clean('runs/track/exp6/Tactical View- Pixellot C Coaching.txt')
