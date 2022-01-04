import os
import json

import string_manipulation
import string_manipulation as ct
import filesystem_changes


# CHECKING IF THE GIVEN PATH IS A VALID FILE
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
    with open(f'{path}/game details.json', 'w', encoding='utf-8') as f:
        json.dump(x_json, f, ensure_ascii=False, indent=4)
    f.close()


# CONVERTING A ONE-LINE JSON INTO VISIBLE JSON
def fix_one_line_json(folder_path, file_name):
    folder_path = string_manipulation.double_backslash_to_slash(folder_path)
    with open(folder_path + file_name) as f:
        x_json = json.load(f)
    with open(folder_path + file_name, 'w', encoding='utf-8') as f:
        json.dump(x_json, f, ensure_ascii=False, indent=4)
    f.close()


# JSON DATA CLEANING (KEEPING THINGS THAT ARE USEFUL)
def json_data_cleanup(folder_path, file_name):
    with open(folder_path + file_name) as f:
        x_json = json.load(f)

    for element in x_json:
        element.pop('club', None)

    _, time_ = filesystem_changes.get_date_time()
    new_name = 'lineup ' + time_ + '.json'
    with open(folder_path + new_name, 'w', encoding='utf-8') as f:
        json.dump(x_json, f, ensure_ascii=False, indent=4)
    f.close()

    os.remove(folder_path + file_name)
    fix_one_line_json(folder_path, 'lineup ' + time_ + '.json')
