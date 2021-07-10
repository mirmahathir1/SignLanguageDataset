import split_one_file

from os import listdir
from os.path import isfile, join
import config

path_of_cropped_videos = "cropped_videos/"
path_of_split_videos = "split_videos/"

cropped_video_names = [f for f in listdir(path_of_cropped_videos) if isfile(join(path_of_cropped_videos, f))]

print(cropped_video_names)

for video_name in cropped_video_names:
    print("splitting: ", path_of_cropped_videos + "/" + video_name)
    split_one_file.split(path_of_cropped_videos, video_name, path_of_split_videos, config.split_duration,
                         config.video_fps, config.video_dimension)
