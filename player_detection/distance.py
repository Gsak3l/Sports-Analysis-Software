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


def euclidean_distance_pixels(df_3):
    # works but 10gb of ram doesn't seem good
    x2_x1 = []
    y2_y1 = []
    for i in range(df_3.shape[0]):
        x2_x1.append([df_3['x'].loc[i] - df_3['x'].loc[j] for j in range(df_3.shape[0])])
        y2_y1.append([df_3['y'].loc[i] - df_3['y'].loc[j] for j in range(df_3.shape[0])])

    # basically x2-x1 and y2-y1
    x2_x1 = pd.DataFrame(x2_x1)
    y2_y1 = pd.DataFrame(y2_y1)

    df_player_distance_ = []
    for i in range(df_3.shape[0]):
        df_player_distance_.append(
            [sqrt(pow(x2_x1.iloc[i][j], 2) + pow(y2_y1.iloc[i][j], 2)) for j in range(df_3.shape[0])])

    df_player_distance_ = pd.DataFrame(df_player_distance_)
    return df_player_distance_


def players_from_camera_meters(df4):
    df4['CM'] = pd.DataFrame(np.random.randint(175, 185, size=(df4.shape[0], 1)))
    df4.loc[df4['w'] > 60, 'CM'] = (732 + 244) / 2  # goalpost6
    f_mm = 30
    image_height_px = 720
    sensor_height_mm = 22

    df4['DC'] = ((f_mm * df4['CM'] * 10 * image_height_px) / (df4['h'] * sensor_height_mm))
    df4['DC'] = df4['DC'].astype(int)

    return df4


def pixels_to_meters(df5, df_distance_px):
    known_pixel_distance = df_distance_px.iloc[1][16]
    known_meters = 9.15
    df_meters = df_distance_px / 5
    print(df_meters.iloc[1][8])
    print(df5)


def manager(df, frame):
    df = read_and_clean(df)
    df = df[df['Frame'] == frame]
    df_player_distance = euclidean_distance_pixels(df)
    df = players_from_camera_meters(df)
    pixels_to_meters(df, df_player_distance)


if __name__ == '__main__':
    desired_width = 320
    pd.set_option('display.width', desired_width)
    np.set_printoptions(linewidth=desired_width)
    pd.set_option('display.max_columns', 20)
    manager('runs/track/exp6/Tactical View- Pixellot C Coaching.txt', 3)
