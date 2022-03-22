import os
import glob
import json
import cv2
import shutil
import pandas as pd

from datetime import datetime

import string_manipulation as sm


# CREATING A FOLDER THAT STORES SUB-FOLDER DATA
def create_root_save_directory():
    path = os.path.join('./', 'Project Saves')
    try:
        os.mkdir(path)
    except OSError as e:
        print(e)


# CREATING SUB-FOLDERS WITH DATE AND TIME AS A NAME
def create_sub_save_folder():
    date, time = get_date_time()
    path = os.path.join('./Project Saves/', f'Date {date}')

    try:
        os.mkdir(path)
    except OSError as e:
        print(e)

    path = os.path.join(f'./Project Saves/Date {date}/', f'Time {time}')
    try:
        os.mkdir(path)
    except OSError as e:
        print(e)

    return path


# CHECKING IF THE GIVEN PATH IS A VALID FILE
def check_if_file_exists(file):
    return os.path.isfile(file)


# RETURNS THE PATH FOR THE FOLDER THAT WAS CREATED LAST INSIDE A GIVEN DIRECTORY
def find_last_created_folder():
    last_date_path = max(glob.glob(os.path.join('./Project Saves/', '*/')), key=os.path.getmtime)
    last_time_path = max(glob.glob(os.path.join(last_date_path, '*/')), key=os.path.getmtime)
    return last_time_path


# RETURNS LAST CREATED WEIGHTS FOLDER FOR THE YOLO-V5 WEIGHTS
def find_yolo_weight_folder():
    os.chdir('./player_detection')
    weights_folder = max(glob.glob(os.path.join('yolov5/runs/train/exp55', '*/*.pt')), key=os.path.getmtime)
    os.chdir('..')
    return weights_folder


# GETTING THE CURRENT DATE AND TIME
def get_date_time():
    now = datetime.now()  # current date and time
    date = now.strftime("%d.%m.%Y")
    time = now.strftime("%H.%M.%S")
    return date, time


# RETURNING THE DOWNLOADS
def downloads_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path


# DELETE FILE
def delete_file(file_path, file_name):
    os.remove(file_path + file_name)


# FIND VIDEO LENGTH SECONDS
def find_video_sec_length():
    duration = 1
    path = ''

    try:
        f = open(sm.double_backslash_to_slash(find_last_created_folder()) + 'game details.json')
        path = json.load(f)
        path = path['Video Path']
        f.close()
    except FileNotFoundError as fl:
        print(fl)

    if path != '':
        cap = cv2.VideoCapture(path)
        fps = cap.get(cv2.CAP_PROP_FPS)  # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps

    return duration


# DELETE ALL FILES FROM FOLDER AND THEN THE FOLDER ITSELF
def delete_files_and_folder(folder_path):
    try:
        for file_name in os.listdir(folder_path):
            file = os.path.join(folder_path, file_name)
            try:
                if os.path.isfile(file) or os.path.islink(file):
                    os.unlink(file)
                elif os.path.isdir(file):
                    shutil.rmtree(file)
            except FileNotFoundError as f:
                print(f)

        os.rmdir(folder_path)
    except FileNotFoundError as f:
        print(f)


# CREATE FOLDER FOR ZOOMED VIDEO VERSIONS
def created_zoom_video_folder():
    try:
        os.mkdir('Zoomed-in Video')
    except FileExistsError as f:
        print(f)


# CREATE FOLDER WITH NAME EXPORTED FRAMES
def create_exported_frames_folder():
    os.mkdir('Exported Frames')
    os.mkdir('Exported Frames/zoomed images')


# FIND LAST CREATED RUNS FOLDER AND GET THE VIDEO FROM THERE
def find_last_detection_video():
    chdir_to_content_root()
    relative_path = max(glob.glob(os.path.join('./player_detection/runs/track/exp*', '*mp4')), key=os.path.getmtime)
    return relative_path


# FIND LAST CREATED RUNS FOLDER AND GET THE TXT FILE FROM THERE
def find_last_detection_text_file():
    chdir_to_content_root()
    relative_path = max(glob.glob(os.path.join('./player_detection/runs/track/exp*', '*txt')), key=os.path.getmtime)
    return relative_path


# CHANGE DIRECTORY TO CONTENT ROOT
def chdir_to_content_root():
    relative_cwd = sm.get_after_last_slash(sm.double_backslash_to_slash(os.getcwd()))
    while relative_cwd != 'SportsAnalysisSoftware':
        os.chdir('..')
        relative_cwd = sm.get_after_last_slash(sm.double_backslash_to_slash(os.getcwd()))


# if __name__ == '__main__':
#     df = pd.read_csv(find_last_detection_text_file(), sep=' ', header=None)
#     df = df.drop([6, 7, 8, 9, 10], axis=1)
#     df = df.dropna(axis='columns')
#     df = df.rename(columns={0: 'Frame', 1: 'ID', 2: 'x', 3: 'y', 4: 'w', 5: 'h'})
#     print(df)
