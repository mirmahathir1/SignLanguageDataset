from pytube import YouTube
import sys

# print(sys.argv)
yt = YouTube(sys.argv[1])

resolutions = ["1080p", "720p", "480p", "360p", "240p", "144p"]
print(yt.streams)
for resolution in resolutions:
    filtered_stream = yt.streams.filter(res=resolution, type="video")
    if len(filtered_stream) != 0:
        print("Download: start ", yt.title)
        filtered_stream.first().download()
        print("Download: end ", yt.title)
        break

abrs = ["160kbps", "128kbps", "70kbps", "50kbps"]
for abr in abrs:
    filtered_stream = yt.streams.filter(abr=abr, type="audio")
    if len(filtered_stream) != 0:
        print("Download: start ", yt.title)
        filtered_stream.first().download()
        print("Download: end ", yt.title)
        break
