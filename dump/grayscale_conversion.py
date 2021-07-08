# importing the module
import cv2
from os.path import isfile, join
from moviepy.video.fx.all import blackwhite
from moviepy.editor import *

def convert(path_of_split_videos, name_of_video, path_of_grayscale_videos):
    # path_of_split_videos = "split_videos/"
    # name_of_video = "Do not wreck this now Van-Tam pleads 🔴 @BBC News live - BBC_0.mp4"
    # path_of_grayscale_videos = "grayscale_videos/"

    # file_without_ext = name_of_video.split(".")[0]

    if isfile(path_of_grayscale_videos + name_of_video):
        print("DUPLICATE: ",path_of_grayscale_videos + name_of_video + '.avi already exists')
        return

    clip = VideoFileClip(path_of_split_videos + name_of_video)
    clip = blackwhite(clip)
    clip.write_videofile(path_of_grayscale_videos + name_of_video)

    # source = cv2.VideoCapture(path_of_split_videos + name_of_video)
    # out = cv2.VideoWriter(path_of_grayscale_videos + file_without_ext + '.avi',
    #                       cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
    #                       30, (512, 432), isColor=False)
    # while True:
    #     ret, frame = source.read()
    #     if ret:
    #         # converting to gray-scale
    #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #         out.write(gray)
    #     else:
    #         break
    # out.release()
    # source.release()


# convert("split_videos/", "Do not wreck this now Van-Tam pleads 🔴 @BBC News live - BBC_0.mp4", "grayscale_videos/")
