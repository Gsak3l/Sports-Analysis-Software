import filesystem_changes
import pytube


# SAVING YOUTUBE VIDEO TO DOWNLOADS
def save_video_to_downloads(url):
    youtube = pytube.YouTube(url)
    youtube_video_title = youtube.title

    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download(filesystem_changes.downloads_path())

    return filesystem_changes.downloads_path() + '/' + youtube_video_title + '.mp4'
