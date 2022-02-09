import pandas as pd
import datetime

import string_manipulation as sm
import filesystem_changes as fc


# RETURNS PLAYER NAMES FROM THE GIVEN DATA FRAME
def get_player_names_from_csv(file_path, file_name):
    file_name = sm.get_file_name(file_name)
    df = pd.read_csv(f'{file_path}{file_name}.csv')
    return sm.list_to_string(df['name'].tolist())


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
    df2 = pd.read_csv(file, sep=' ', header=None)
    df2 = df2.rename(columns={0: 'Frame', 1: 'ID', 2: 'x', 3: 'y', 4: 'w', 5: 'h'})
    df2 = df2.dropna(axis='columns')
    df2 = df2.drop([6, 7, 8, 9], axis=1)
    return df2
