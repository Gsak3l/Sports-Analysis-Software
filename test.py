import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Project Saves/Date 24.02.2022/Time 10.09.20/actions.csv')

action = df.Action
timestamp = df.Timestamp
name = df.Name

plt.plot(action, timestamp, 'bo')
plt.show()
