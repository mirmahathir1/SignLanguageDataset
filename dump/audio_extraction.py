import moviepy.editor as mp
from os.path import isfile


# plot wav file scipy https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html

def extract(src_directory, video_name, dst_directory):

    file_name_without_ext = video_name.split(".")[0]

    if isfile(dst_directory + file_name_without_ext + ".wav"):
        print("DUPLICATE: ", dst_directory + file_name_without_ext + ".wav")
        return

    clip = mp.VideoFileClip(src_directory + video_name)

    # Insert Local Audio File Path
    clip.audio.write_audiofile(dst_directory + file_name_without_ext + ".wav", codec='pcm_s16le')




# extract("split_videos/", "Do not wreck this now Van-Tam pleads 🔴 @BBC News live - BBC_0.mp4", "split_audios/")
