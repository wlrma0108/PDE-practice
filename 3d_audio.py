import numpy as np
import librosa
import soundfile as sf
import numpy as np
import soundfile as sf


input_audio, fs = sf.read('/content/london-money-170064.mp3')


v = np.arange(-100, 101)
x = v / 200 + 0.5
x_full = np.tile(np.concatenate((x, x[::-1])), int(np.ceil(len(input_audio) / (2*len(x)))))
x_full = x_full[:len(input_audio)]

left_linear = (1 - x_full) * input_audio
right_linear = x_full * input_audio
stereo_linear = np.stack([left_linear, right_linear], axis=1)


left_sine = np.sin((1 - x_full) * (np.pi/2)) * input_audio
right_sine = np.sin(x_full * (np.pi/2)) * input_audio
stereo_sine = np.stack([left_sine, right_sine], axis=1)

sf.write('output_linear.wav', stereo_linear, fs)
sf.write('output_sine.wav', stereo_sine, fs)

print("변환 완료: 'output_linear.wav', 'output_sine.wav'")




