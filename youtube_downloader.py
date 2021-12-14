import pytube
from pathlib import Path

downloads_path = str(Path.home() / "Downloads")

url = 'https://www.youtube.com/watch?v=jXjUkN-J7kE'

youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download(downloads_path)
