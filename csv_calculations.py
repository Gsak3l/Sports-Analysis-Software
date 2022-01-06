import string_manipulation as sm
import pandas as pd


# RETURNS PLAYER NAMES FROM THE GIVEN DATA FRAME
def get_player_names_from_csv(file_path, file_name):
    file_name = sm.get_file_name(file_name)
    df = pd.read_csv(f'{file_path}{file_name}.csv')
    return df['name'].tolist()
