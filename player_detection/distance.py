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
    df3['Player Height in CM'] = pd.DataFrame(np.random.randint(160, 200, size=(64636, 1)))

    f_mm = 20
    image_height_px = 720
    sensor_height_mm = 25

    df3['Distance from Camera'] = ((f_mm * df3['Player Height in CM'] * 10 * image_height_px) /
                                   (df3['h'] * sensor_height_mm)) / 1000
    df3['Distance from Camera'] = df3['Distance from Camera'].astype(int)

    print(df3[df3['Frame'] == 3])


if __name__ == '__main__':
    desired_width = 320
    pd.set_option('display.width', desired_width)
    np.set_printoptions(linewidth=desired_width)
    pd.set_option('display.max_columns', 10)

    df = read_and_clean('runs/track/exp6/Tactical View- Pixellot C Coaching.txt')
    calculate_distance_from_camera(df)
