from pytube import YouTube
yt = YouTube('https://youtu.be/f0UPSNGiHxw')
yt.streams.filter(progressive=True)
yt.streams.filter(adaptive=True)
yt.streams.filter(only_audio=True)
yt.streams.filter(file_extension='mp4')
stream = yt.streams.get_by_itag(22)
stream.download()