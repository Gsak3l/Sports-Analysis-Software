from math import sqrt
import numpy as np
import pandas as pd
import cv2


def read_and_clean(file):
    df2 = pd.read_csv(file, sep=' ', header=None)
    df2 = df2.rename(columns={0: 'Frame', 1: 'ID', 2: 'x', 3: 'y', 4: 'w', 5: 'h'})
    df2 = df2.dropna(axis='columns')
    df2 = df2.drop([6, 7, 8, 9], axis=1)
    return df2


def calculate_distance_from_camera(df3):
    df3['CM'] = pd.DataFrame(np.random.randint(180, 181, size=(64636, 1)))

    f_mm = 30
    image_height_px = 720
    sensor_height_mm = 22

    df3['DC'] = ((f_mm * 175 * 10 * image_height_px) / (df3['h'] * sensor_height_mm)) / 1000
    df3['DC'] = df3['DC'].astype(int)

    # print(df3[df3['Frame'] == 3])

    return df3


def random_thing():
    x1, y1 = 715, 298
    x2, y2 = 741, 235

    y = abs(y2 - y1)
    y = y / 10

    x = abs(x2 - x1)
    x = x / 20

    distance = x + y
    print(distance)


def euclidean_distance_pixels(df4):
    x1, y1 = 637, 177
    x2, y2 = 1013, 204

    distance = sqrt(pow(x2 - y1, 2) + pow(y2 - y1, 2))

    df_x = df4[['x']]
    df_y = df4[['y']]

    df_distance = [abs(df_y - df_x.loc[i]) for i in range(64636)]  # works but 10gb of ram doesn't seem good...
    print(df_distance.shape)


def euclidean_distance_meters(df4):
    x2_y1 = 34
    y2_y1 = 30

    distance = sqrt(pow(x2_y1, 2) + pow(y2_y1, 2))
    print(distance)


if __name__ == '__main__':
    desired_width = 320
    pd.set_option('display.width', desired_width)
    np.set_printoptions(linewidth=desired_width)
    pd.set_option('display.max_columns', 10)

    df = read_and_clean('runs/track/exp6/Tactical View- Pixellot C Coaching.txt')
    df = calculate_distance_from_camera(df)
    euclidean_distance_pixels(df)
