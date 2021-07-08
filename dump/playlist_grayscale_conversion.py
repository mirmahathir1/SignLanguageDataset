from dump import grayscale_conversion

from os import listdir
from os.path import isfile, join

path_of_split_videos = "../split_videos/"
path_of_grayscale_videos = "grayscale_videos/"

split_video_names = [f for f in listdir(path_of_split_videos) if isfile(join(path_of_split_videos, f))]

print(split_video_names)

for video_name in split_video_names:
    print("grayscale conversion: ",path_of_split_videos + "/" + video_name)
    grayscale_conversion.convert(path_of_split_videos, video_name, path_of_grayscale_videos)