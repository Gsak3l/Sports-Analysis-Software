import json
import convert_text as ct


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

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(x_json, f, ensure_ascii=False, indent=4)
