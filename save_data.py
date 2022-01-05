import os
import json
import pandas as pd

import string_manipulation as sm
import filesystem_changes as fc


# CHECKING IF THE GIVEN PATH IS A VALID FILE
def check_if_file_exists(video_file):
    return os.path.isfile(video_file)


# SAVING THE EMBED LOCAL VIDEO DATA TO A JSON FILE
def save_pre_local_video_data(calendar_date, sport, season, competition, details, video_file):
    x_json = {
        'Title': sm.path_to_video_title(video_file),
        'Date': sm.qdate_to_date(str(calendar_date)),
        'Sport': sport,
        'Season': season,
        'Competition': competition,
        'Other Details': details,
        'Video Title': sm.path_to_video_name(video_file),
        'Video Path': video_file
    }
    save_readable_json(x_json)


# SAVING THE EMBED CLOUD VIDEO DATA TO A JSON FILE
def save_pre_cloud_video_data(calendar_date, sport, season, competition, details, video_file):
    x_json = {
        'Title': sm.path_to_video_title(video_file),
        'Date': sm.qdate_to_date(str(calendar_date)),
        'Sport': sport,
        'Season': season,
        'Competition': competition,
        'Other Details': details,
        'Video Title': sm.path_to_video_name(video_file),
        'Video Path': video_file
    }
    save_readable_json(x_json)


# APPLYING EMBEDS ON THE JSON FILE TO MAKE IT MORE VISIBLE AND SAVING IT
def save_readable_json(x_json):
    # getting the last created folder
    path = fc.find_last_created_folder()
    # saving to a json file
    with open(f'{path}/game details.json', 'w') as f:
        json.dump(x_json, f, ensure_ascii=False, indent=4)
    f.close()


# CONVERTING A ONE-LINE JSON INTO VISIBLE JSON
def fix_one_line_json(file_path, file_name):
    file_path = sm.double_backslash_to_slash(file_path)
    with open(file_path + file_name) as f:
        x_json = json.load(f)
    with open(file_path + file_name, 'w') as f:
        json.dump(x_json, f, ensure_ascii=False, indent=4)
    f.close()


# JSON DATA CLEANING (KEEPING THINGS THAT ARE USEFUL)
def json_data_cleanup(file_path, file_name):
    with open(file_path + file_name) as f:
        x_json = json.load(f)

    for element in x_json:
        element.pop('club', None)

    _, time_ = fc.get_date_time()
    new_name = 'lineup ' + time_ + '.json'
    with open(file_path + new_name, 'w') as f:
        json.dump(x_json, f, ensure_ascii=False, indent=4)
    f.close()

    fc.delete_file(file_path, file_name)

    file_name = 'lineup ' + time_ + '.json'
    fix_one_line_json(file_path, file_name)
    json_to_csv(file_path, file_name)

    fc.delete_file(file_path, file_name)


# JSON TO CSV
def json_to_csv(file_path, file_name):
    df = pd.read_json(file_path + '/' + file_name)
    file_name = sm.get_file_name(file_name)
    df.to_csv(f'{file_path}{file_name}.csv', index=None, encoding='utf8')


# json_to_csv('Project Saves/Date 01.01.2022/Time 19.33.14', 'lineup 19.34.50.json')
