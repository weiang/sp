# -*- coding: utf-8 -*-
import numpy as np
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
PCM_OUTPUT_FILENAME = "output.pcm"


def wave2pcm(wave_file, pcm_file):
    with open(wave_file, 'rb') as fd:
        fd.seek(0)
        fd.read(44)
        data = np.fromfile(fd, dtype=np.int16)
        data.tofile(pcm_file)



def main():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK)

    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    wave2pcm(WAVE_OUTPUT_FILENAME, PCM_OUTPUT_FILENAME)


if __name__ == '__main__':
    main()



