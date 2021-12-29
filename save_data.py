import os.path
import json
import time

import string_manipulation
import string_manipulation as ct
import filesystem_changes


# checking if the given path is a valid path
def check_if_file_exists(video_file):
    return os.path.isfile(video_file)


# SAVING THE EMBED LOCAL VIDEO DATA TO A JSON FILE
def save_pre_local_video_data(calendar_date, sport, season, competition, details, video_file):
    x_json = {
        'Title': ct.path_to_video_title(video_file),
        'Date': ct.qdate_to_date(str(calendar_date)),
        'Sport': sport,
        'Season': season,
        'Competition': competition,
        'Other Details': details,
        'Video Title': ct.path_to_video_name(video_file),
        'Video Path': video_file
    }
    save_readable_json(x_json)


# SAVING THE EMBED CLOUD VIDEO DATA TO A JSON FILE
def save_pre_cloud_video_data(calendar_date, sport, season, competition, details, video_file):
    x_json = {
        'Title': ct.path_to_video_title(video_file),
        'Date': ct.qdate_to_date(str(calendar_date)),
        'Sport': sport,
        'Season': season,
        'Competition': competition,
        'Other Details': details,
        'Video Title': ct.path_to_video_name(video_file),
        'Video Path': video_file
    }
    save_readable_json(x_json)


# APPLYING EMBEDS ON THE JSON FILE TO MAKE IT MORE VISIBLE AND SAVING IT
def save_readable_json(x_json):
    # getting the last created folder
    path = filesystem_changes.find_last_created_folder()
    # saving to a json file
    with open(f'{path}/game_details.json', 'w', encoding='utf-8') as f:
        json.dump(x_json, f, ensure_ascii=False, indent=4)
    f.close()


# CONVERTING A ONE-LINE JSON INTO VISIBLE JSON
def fix_one_line_json(file_path):
    file_path = string_manipulation.double_backslash_to_slash(file_path)
    print(file_path)
    with open(file_path) as f:
        x_json = json.load(f)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(x_json, f, ensure_ascii=False, indent=4)
    f.close()

