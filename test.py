import pandas as pd

df_actions = pd.read_csv('Project Saves/Date 29.01.2022/Time 11.30.30/actions.csv')
print(df_actions['Name'].tolist())
