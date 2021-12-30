import os
import glob
from datetime import datetime


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
