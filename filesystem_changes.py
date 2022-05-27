import re
import os
import glob
import shutil

from datetime import datetime

import string_manipulation as sm


# CREATING A FOLDER THAT STORES SUB-FOLDER DATA
def create_root_save_directory():
    path = os.path.join('./', 'Project Saves')
    try:
        os.mkdir(path)
    except OSError as oe:
        print(oe)


# CREATING SUB-FOLDERS WITH DATE AND TIME AS A NAME
def create_sub_save_folder():
    date, time = sm.get_date_time()
    path = os.path.join('./Project Saves/', f'Date {date}')

    try:
        os.mkdir(path)
    except OSError as oe:
        print(oe)

    path = os.path.join(f'./Project Saves/Date {date}/', f'Time {time}')
    try:
        os.mkdir(path)
    except OSError as oe:
        print(oe)

    return path


# RETURNS ALL CSV LINEUPS FROM LAST CREATED FOLDER
def find_last_folder_lineups():
    all_files = os.listdir(sm.double_backslash_to_slash(find_last_created_folder()))
    lineups = []

    for file in all_files:
        if re.search(r'\blineup\b', file):
            lineups.append(file)

    return lineups


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


# RETURNING THE DOWNLOADS
def downloads_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path


# DELETE FILE
def delete_file(file_path, file_name):
    os.remove(file_path + file_name)


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
            except FileNotFoundError as fe:
                print(f)

        os.rmdir(folder_path)
    except FileNotFoundError as fe:
        print(fe)


# CREATE FOLDER FOR ZOOMED VIDEO VERSIONS
def created_zoom_video_folder():
    try:
        os.mkdir('Zoomed-in Video')
    except FileExistsError as fe:
        print(fe)


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
