#https://stackoverflow.com/questions/54710982/using-pytube-to-download-playlist-from-youtube
#https://github.com/pytube/pytube

from pytube import Playlist

### https://www.youtube.com/playlist?list=PLhUp81I0jET71gMTWy50cpAYHrWnVnYlA
p = Playlist('https://www.youtube.com/playlist?list=PLwXQLZ3FdTVEITn849NlfI9BGY-hk1wkq')
print('Number of videos in playlist: %s' % len(p.video_urls))
print(f'Downloading: {p.title}')
for video in p.videos:
    print(video)
    video.streams.first().download()
