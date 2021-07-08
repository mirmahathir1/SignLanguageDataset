import cv2
import numpy as np
from os.path import isfile, join
from os import listdir

video_name = "split_videos/Do not wreck this now Van-Tam pleads 🔴 @BBC News live - BBC_0.mp4"
cap = cv2.VideoCapture(video_name)
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

path_of_split_videos = "../split_videos/"
split_video_names = [f for f in listdir(path_of_split_videos) if isfile(join(path_of_split_videos, f))]

split_video_names.sort()

print("number of videos: ", len(split_video_names))

buf = np.empty((5, frameCount, frameHeight, frameWidth), np.dtype('uint8'))

video_count = 0
for video in split_video_names[:5]:
    print("processing video: ",video)
    fc = 0
    ret = True
    cap = cv2.VideoCapture(path_of_split_videos + video)
    while fc < frameCount and ret:
        ret, buffer = cap.read()
        buf[video_count][fc] = buffer[:,:,0]
        fc += 1

    cap.release()
    video_count = video_count + 1

print(buf.shape)


with open('binary_data/X.npy', 'wb') as f:
    np.save(f, buf)
