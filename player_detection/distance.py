from math import sqrt, hypot
import numpy as np
import pandas as pd
import cv2


def read_and_clean(file):
    df2 = pd.read_csv(file, sep=' ', header=None)
    df2 = df2.rename(columns={0: 'Frame', 1: 'ID', 2: 'x', 3: 'y', 4: 'w', 5: 'h'})
    df2 = df2.dropna(axis='columns')
    df2 = df2.drop([6, 7, 8, 9], axis=1)
    return df2


def euclidean_distance_pixels(df3):
    x2_x1 = []
    y2_y1 = []

    for i in range(df3.shape[0]):
        x2_x1.append([df3['x'].loc[i] - df3['x'].loc[j] for j in range(df3.shape[0])])
        y2_y1.append([df3['y'].loc[i] - df3['y'].loc[j] for j in range(df3.shape[0])])

    # basically x2-x1 and y2-y1
    x2_x1 = pd.DataFrame(x2_x1)
    y2_y1 = pd.DataFrame(y2_y1)

    df_player_distance_ = []
    for i in range(df3.shape[0]):
        df_player_distance_.append(
            [sqrt(pow(x2_x1.iloc[i][j], 2) + pow(y2_y1.iloc[i][j], 2)) for j in range(df3.shape[0])]
        )

    df_player_distance_ = pd.DataFrame(df_player_distance_)
    df_player_distance_ = df_player_distance_.astype(int)
    return df_player_distance_


def players_from_camera_meters(df4):
    df4['CM'] = pd.DataFrame(np.random.randint(175, 190, size=(df4.shape[0], 1)))
    df4.loc[df4['h'] > 100, 'CM'] = 5000  # goalpost6
    f_mm = 35
    image_height_px = 720
    sensor_height_mm = 44.3

    # I don't know what I am doing, I really don't
    df4.loc[df4['h'] * .8 > df4['w'], 'DC'] = \
        (f_mm * df4['CM'] * 10 * image_height_px) / ((df4['h'] + df4['w']) * sensor_height_mm)

    df4.loc[df4['h'] * .8 > df4['w'], 'DC'] = \
        (f_mm * df4['CM'] * 10 * image_height_px) / ((df4['h'] * 0.4 + df4['w'] * 0.6) * sensor_height_mm)

    df4['DC'] = df4['DC'] / 1000
    df4['DC'] = df4['DC'].astype(int)

    return df4


def euclidean_distance_meters(df5, distance_pixel):
    distance_meters = []
    for i in range(df5.shape[0]):
        # if anyone is reading this, please don't judge me, I have no idea what I am doing
        distance_meters.append(
            [(df5['DC'].loc[i] + df5['DC'].loc[j]) * distance_pixel.iloc[i][j] / (df5['x'].loc[i] + df5['x'].loc[j])
             for j in range(df5.shape[0])]
        )

    distance_meters = pd.DataFrame(distance_meters)
    distance_meters = distance_meters
    distance_meters += distance_meters.mean() / 3
    return distance_meters


def calculate_offense_defense(df_offense):
    possession_changed = []
    df_center = df_offense[(df_offense['h'] > 200)]
    df_center = df_center.drop(['ID', 'y', 'w', 'h'], axis=1)

    # df_offense.loc[(df_offense['ID'] == 1) & (df_offense['x'] < 800), 'D/O'] = 'DEFENCE'
    # print(df_offense.loc[(df_offense['ID'] == 1) & (df_offense['x'] > 800)])

    df_center.loc[df_center['x'] < 350, 'D/O'] = 'DEFENSE'
    df_center.loc[df_center['x'] > 800, 'D/O'] = 'OFFENSE'
    df_center['D/O'] = df_center['D/O'].replace(np.nan, 'JUST PLAYING')

    # print(df_center[df_center['D/O'] == 'OFFENSE'])
    # print(df_center[df_center['D/O'] == 'DEFENCE'])
    # print(df_center[df_center['D/O'] == 'JUST PLAYING'])

    for i in range(df_center.shape[0] - 1):
        if df_center.iloc[i]['D/O'] != df_center.iloc[i + 1]['D/O']:
            print('CHANGE', i)
            print(df_center.iloc[i]['D/O'], i)
            possession_changed.append(i)

    print(possession_changed)
    return possession_changed


def manager(df, frame):
    df = read_and_clean(df)
    calculate_offense_defense(df)
    df = df[df['Frame'] == frame]
    df = df.reset_index(drop=True)
    df_ds_px = euclidean_distance_pixels(df)  # distance between players pixels
    df = players_from_camera_meters(df)
    df_ds_m = euclidean_distance_meters(df, df_ds_px)  # distance between players meters


if __name__ == '__main__':
    desired_width = 320
    pd.set_option('display.width', desired_width)
    np.set_printoptions(linewidth=desired_width)
    pd.set_option('display.max_columns', 23)
    manager('runs/track/exp18/Tactical View- Pixellot C Coaching.txt', 46)
