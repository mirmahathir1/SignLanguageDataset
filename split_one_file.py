from moviepy.editor import *
from moviepy.video.fx.all import blackwhite, resize
from os.path import isfile, join
import config


def split(src_directory, video_file, dst_directory, segment_length):

    file_name_without_ext = video_file.split(".")[0]

    clip = VideoFileClip(src_directory + video_file)

    print(clip.fps)
    print(clip.w, " ", clip.h)

    original_video = VideoFileClip(src_directory + video_file)
    duration = original_video.duration
    clip_start = 0

    num = 0

    while clip_start < duration:
        clip_end = clip_start + segment_length
        if clip_end > duration:
            break

        print("generating: ", dst_directory + file_name_without_ext + "_" + str(num) + ".mp4")

        if not isfile(dst_directory + file_name_without_ext + "_" + str(num) + ".mp4"):
            clip = VideoFileClip(src_directory + video_file).subclip(clip_start, clip_end)
            # clip = blackwhite(clip)
            # clip = clip.resize(dimension)
            # clip = clip.set_fps(fps)

            clip.write_videofile(dst_directory + file_name_without_ext + "_" + str(num) + ".mp4",
                                 audio_codec='aac')

        else:
            print("DUPLICATE: skipping ", dst_directory + file_name_without_ext + "_" + str(num) + ".mp4")

        clip_start = clip_end
        num += 1


# split("cropped_videos/", "Do not wreck this now Van-Tam pleads 🔴 @BBC News live - BBC.mp4", "split_videos/",
#       config.split_duration)
