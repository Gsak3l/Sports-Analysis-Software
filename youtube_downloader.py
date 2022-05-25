import pytube

import filesystem_changes as fc


# SAVING YOUTUBE VIDEO TO DOWNLOADS
def save_video_to_downloads(url):
    youtube = pytube.YouTube(url)
    youtube_video_title = youtube.title

    video = youtube.streams.get_highest_resolution()
    video.download(fc.downloads_path())

    return fc.downloads_path() + '/' + youtube_video_title + '.mp4'


if __name__ == '__main__':
    save_video_to_downloads('https://www.youtube.com/watch?v=JM3a7olLxmE')
