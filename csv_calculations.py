import re
import pandas as pd
import datetime

import string_manipulation as sm
import filesystem_changes as fc


# RETURNS PLAYER NAMES FROM THE GIVEN DATA FRAME
def get_player_names_from_csv(file_path, file_name):
    file_name = sm.get_file_name(file_name)
    df = pd.read_csv(f'{file_path}{file_name}.csv')
    return sm.list_to_string(df['name'].tolist())


# ADDS PLAYER NAMES, ACTIONS ETC TO CSV
def add_to_csv(player_name, type_of_action, action, timestamp):
    timestamp = str(datetime.timedelta(seconds=int(timestamp)))
    data = {
        'Name': [player_name],
        'Action Family': [type_of_action],
        'Action': [action],
        'Timestamp': timestamp
    }
    if fc.check_if_file_exists(f'{fc.find_last_created_folder()}actions.csv'):
        df2 = pd.DataFrame(data)
        df2.to_csv(f'{fc.find_last_created_folder()}actions.csv', mode='a', index=False, header=False)
    else:
        df = pd.DataFrame(data)
        df.to_csv(f'{fc.find_last_created_folder()}actions.csv', index=False, header=True)


# CREATES A NEW CSV FILE IF IT DOESN'T ALREADY EXIST
def create_csv():
    try:
        with open(f'{fc.find_last_created_folder().actions.csv}', 'w'):
            pass
    except AssertionError:
        pass


# READ THE GIVEN CSV AND CLEAN THE USELESS DATA FROM IT FOR THIS SPECIFIC SCENARIO
def read_and_clean(file):
    df = pd.read_csv(file, sep=' ', header=None)
    df = df.drop([6, 7, 8, 9, 10], axis=1)
    df = df.dropna(axis='columns')
    df = df.rename(columns={0: 'Frame', 1: 'ID', 2: 'x', 3: 'y', 4: 'w', 5: 'h'})
    return df


# CLEANS UP THE CSV FILE AND KEEPS ONLY THE IMPORTANT FIELDS
def cleanup_csv_lineup(df):
    try:
        df = df.drop(['photoFolderIndex', 'photo', 'shortName'], axis=1)
    except KeyError:
        pass
    df['positions'] = df['positions'].apply(lambda x: re.sub(r'[^a-zA-Z, ]+', '', x))
    return df

# if __name__ == '__main__':
#     read_and_clean('player_detection/runs/track/exp73/Tactical View- Pixellot C Coaching.mp4')
