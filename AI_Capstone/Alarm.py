import pyaudio
import wave
import time

def play_audio(enabled=True):
    # your audio here
    wf = wave.open('Clock-chimes-sounds.wav', 'rb')

    # instantiate PyAudio
    p = pyaudio.PyAudio()

    # define callback
    def callback(in_data, frame_count, time_info, status):
        if enabled:
            data = wf.readframes(frame_count)
            return (data, pyaudio.paContinue)
        else:
            return (b'', pyaudio.paComplete)

    # open stream using callback
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream
    stream.start_stream()

    while stream.is_active() and enabled:
        time.sleep(0.1)

    # stop stream
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio
    p.terminate()
