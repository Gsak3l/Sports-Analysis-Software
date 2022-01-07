import pandas as pd

import string_manipulation as sm
import filesystem_changes as fc


# RETURNS PLAYER NAMES FROM THE GIVEN DATA FRAME
def get_player_names_from_csv(file_path, file_name):
    file_name = sm.get_file_name(file_name)
    df = pd.read_csv(f'{file_path}{file_name}.csv')
    return sm.list_to_string(df['name'].tolist())


def add_to_csv(player_name, type_of_action, action):
    # create_csv()
    data = {
        'Name': [player_name],
        'Action Family': [type_of_action],
        'Action': [action]
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
