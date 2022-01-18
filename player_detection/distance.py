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
    # works but 10gb of ram doesn't seem good
    x2_x1 = []
    y2_y1 = []
    # FIXME for loop doesn't work for all frames
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
    df4['CM'] = pd.DataFrame(np.random.randint(180, 181, size=(df4.shape[0], 1)))
    df4.loc[df4['w'] > 60, 'CM'] = (732 + 244) / 2  # goalpost6
    f_mm = 35
    image_height_px = 720
    sensor_height_mm = 44.3

    # cm * 10 to get the mm
    df4['DC'] = (f_mm * df4['CM'] * 10 * image_height_px) / (df4['h'] * sensor_height_mm)
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
    distance_meters = distance_meters / 1000
    distance_meters += distance_meters.mean() / 2
    return distance_meters


def manager(df, frame):
    df = read_and_clean(df)
    print(df)
    df = df[df['Frame'] == frame]
    df = df.reset_index(drop=True)
    df_player_distance_px = euclidean_distance_pixels(df)
    df = players_from_camera_meters(df)
    df_player_distance_meters = euclidean_distance_meters(df, df_player_distance_px)
    print(df)
    print(df_player_distance_meters.iloc[0][11])


if __name__ == '__main__':
    desired_width = 320
    pd.set_option('display.width', desired_width)
    np.set_printoptions(linewidth=desired_width)
    pd.set_option('display.max_columns', 23)
    manager('runs/track/exp8/Tactical View- Pixellot C Coaching.txt', 271)
