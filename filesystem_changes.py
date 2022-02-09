import os
import glob
from datetime import datetime
import json
import cv2
import shutil

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


# CREATE FOLDER WITH NAME EXPORTED FRAMES
def create_exported_frames_folder():
    os.mkdir('Exported Frames')
    os.mkdir('Exported Frames/zoomed images')
