from scipy.io import wavfile
import numpy as np
from os.path import isfile, join
from os import listdir

path_of_split_videos = "../split_audios/"
split_video_names = [f for f in listdir(path_of_split_videos) if isfile(join(path_of_split_videos, f))]

buf = np.empty((5, 5292882), np.dtype('uint8'))

audio_count = 0
for file_name in split_video_names:
    samplerate, data = wavfile.read(path_of_split_videos+ file_name)
    length = data.shape[0] / samplerate
    time = np.linspace(0., length, data.shape[0])

    buf[audio_count] = data[:, 1]
    audio_count = audio_count + 1

# with open('binary_data/Y.npy', 'wb') as f:
#     np.save(f, buf)
