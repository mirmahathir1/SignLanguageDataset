import librosa
import soundfile as sf
from os.path import isfile
import config

def downsample(src_directory, audio_name, dest_directory, audio_sampling_rate,audio_duration):
    if isfile(dest_directory + audio_name):
        print("DUPLICATE: " + dest_directory + audio_name + " already created.")
        return

    print("downsampling audio file name: "+dest_directory + audio_name)
    y, s = librosa.load(src_directory + audio_name,
                        audio_sampling_rate, mono=True)

    # rounding the length of audio
    y = y[:s*audio_duration]
    print("audio shape: ",y.shape)
    print("sampling rate: ", s)
    sf.write(dest_directory + audio_name, y, s, 'PCM_24')

# downsample("split_audios/", "Do not wreck this now Van-Tam pleads 🔴 @BBC News live - BBC_0.wav", "downsampled_audios/",
#            config.audio_sample_rate,config.split_duration)
