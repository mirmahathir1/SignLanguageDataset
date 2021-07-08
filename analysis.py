from scipy.io import wavfile
import numpy as np
wav_name = "downsampled_audios/Do not wreck this now Van-Tam pleads 🔴 @BBC News live - BBC_0.wav"
samplerate, data = wavfile.read(wav_name)
print(samplerate)
print(data.shape)
print(data)
print(data.dtype)

max_data = np.max(data)
data = data/max_data
data = data*1000
data = data.astype(np.int32)

print(data)
data = data/1000
data = data* max_data
data = data.astype(np.int32)
print(data)
#
wavfile.write('sample_video/sample.wav',samplerate,data)