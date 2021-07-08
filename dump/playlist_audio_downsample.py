import audio_downsample

from os import listdir
from os.path import isfile, join

import config

src_directory = "split_audios/"
dst_directory = "downsampled_audios/"

split_audio_names = [f for f in listdir(src_directory) if isfile(join(src_directory, f))]

print(split_audio_names)

for audio_name in split_audio_names:
    print("downsampling audio: ",src_directory + "/" + audio_name)
    audio_downsample.downsample(src_directory,audio_name,dst_directory,config.audio_sample_rate,config.split_duration)

