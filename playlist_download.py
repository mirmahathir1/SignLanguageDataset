# include library
from pytube import Playlist, YouTube
from os import path

# CONTROLLER VARIABLES
playlist_link = 'https://www.youtube.com/playlist?list=PL5A4nPQbUF8Ck7csEOg98U0-bA970noXS'
playlist = Playlist(playlist_link)

resolutions = ["720p"]
# resolutions = ["720p", "720p50", "480p", "360p", "240p", "144p"]
number_of_videos_to_be_downloaded = len(playlist.video_urls)
# number_of_videos_to_be_downloaded = 50
path_to_raw_video_download = "./raw_videos"
# enable_download = False
enable_download = True

# CODE EXECUTION START
print("Total number of videos in playlist: ", len(playlist.video_urls))
# total_length_audio_in_bytes = 0
print("_" * 40)


def write_completed_url(new_url):
    logfile = open('completed_urls.txt', 'r')
    loglist = logfile.readlines()
    logfile.close()
    found = False
    for line in loglist:
        if new_url in line:
            print("Video Found")
            found = True
    if not found:
        logfile = open('completed_urls.txt', 'a')
        logfile.write(new_url + "\n")
        logfile.close()


def check_is_downloaded(url):
    logfile = open('completed_urls.txt', 'r')
    loglist = logfile.readlines()
    logfile.close()
    found = False
    for line in loglist:
        if url in line:
            found = True
    return found


for video_url in playlist.video_urls[:number_of_videos_to_be_downloaded]:
    print("_" * 40)
    yt = YouTube(video_url)
    print("Processing url: ", video_url)

    if check_is_downloaded(video_url):
        print("skipping download")
        continue

    # print("Title: ",yt.title)
    # print("video length in minutes: ", yt.length / 60)
    # downloadable_video_found = False

    downloadable_video_found = False
    for resolution in resolutions:
        filtered_stream = None

        attempt = 0
        while True:
            try:
                filtered_stream = yt.streams.filter(res=resolution)
                print("Stream found")
                # stream_found_urls.write(video_url + "\n")
                break
            except:
                print("ERROR in reading stream. Retrying...", end=" ")
                attempt = attempt + 1
                if attempt == 10:
                    break
        if attempt == 10:
            break

        if len(filtered_stream) != 0:
            print("video stream: ", filtered_stream.first())
            print("video file size in MB: ", filtered_stream.first().filesize / (1024 * 1024))
            if enable_download:
                print("Download: video start ", yt.title)

                filtered_stream.first().download(output_path=path_to_raw_video_download)

                print("Download: video end ", yt.title)
                write_completed_url(video_url)
            downloadable_video_found = True
            break

    if not downloadable_video_found:
        print("ERROR: FOUND VIDEO WITH NON MATCHING RESOLUTION")
