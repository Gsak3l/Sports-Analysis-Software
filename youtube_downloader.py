from pathlib import Path
import pytube
import os


# Saving the youtube video, might add on progress bar in the future I guess...
def save_video_to_downloads(url):
    youtube = pytube.YouTube(url)
    youtube_video_title = youtube.title

    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download(file_path())

    return file_path() + '/' + youtube_video_title + '.mp4'


# # On complete seems to work just fine
# def on_complete(yt_title):
#     path = file_path() + '\\' + yt_title + '.mp4'
#     if os.path.exists(path):
#         return False
#
#
# def on_progress(yt_title):
#     i = 0
#     while not on_complete(yt_title):
#         time.sleep(1)
#         print(str(i) + "%")
#         i = i + 0.1
#     i = 100
#     print(str(i) + "%")


# Downloading the file and saving it to the Downloads
def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path


save_video_to_downloads('https://www.youtube.com/watch?v=Wof0xPUmW38')
