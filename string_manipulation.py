import re


# REPLACING ALL SYMBOLS WITH SPACES
# # C:\file\video\name.mp4 to random_basketball_game.mp4  to RANDOM BASKETBALL GAME
def path_to_video_title(video_file):
    file_title = re.findall('([^\/]+$)', video_file)[0]

    try:
        file_title = re.sub('[^a-zA-Z0-9\n\.]', ' ', file_title)
    except Exception as e:
        print(e.message, e.args)

    file_title = file_title[0:file_title.find('.')]

    return file_title.title()


# C:\file\video\name.mp4 to name.mp4
def path_to_video_name(video_file):
    return re.findall('([^\/]+$)', video_file)[0]


# REFORMATTING THE CALENDAR DATE, TO AN EASY TO READ DATE
def qdate_to_date(calendar_date):
    return calendar_date[calendar_date.find('(') + 1:calendar_date.find(')')]


def double_backslash_to_slash(text):
    text = text.replace('\\\\', '/')
    text = text.replace('\\', '/')
    return text


def contains_letters(text):
    if re.search('[a-zA-Z]', text):
        return True
