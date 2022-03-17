import os
import sys

import string_manipulation as sm
import filesystem_changes as fc


# RETURNS DEFAULT SYSTEM PYTHON VERSION
def get_python_version():
    python_ver = sys.version
    python_ver = sm.keep_till_second_dot(python_ver)
    return python_ver


# GET YOLO
def get_yolo_mode():
    y_mode = fc.find_yolo_weight_folder()
    y_mode = sm.double_backslash_to_slash(y_mode)
    # y_mode = sm.get_text_after_slash(y_mode)
    return y_mode


# TRAIN USING THE STANDARD WEIGHTS
def track_players_given_the_weights(video_path):
    python_version = get_python_version()
    yolo_mode = get_yolo_mode()

    os.chdir('./player_detection')
    command = f'python track.py --yolo_mode {yolo_mode} --source "{video_path}" --classes 0 1 --save-vid --save-txt'
    os.system(command)
