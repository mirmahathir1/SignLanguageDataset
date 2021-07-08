import audio_extraction

from os import listdir
from os.path import isfile, join

path_of_split_videos = "split_videos/"
path_of_split_audios = "split_audios/"

split_video_names = [f for f in listdir(path_of_split_videos) if isfile(join(path_of_split_videos, f))]

print(split_video_names)

for video_name in split_video_names:
    print("extracting audio: ",path_of_split_videos + "/" + video_name)
    audio_extraction.extract(path_of_split_videos,video_name,path_of_split_audios)
