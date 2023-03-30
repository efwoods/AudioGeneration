from pydub import AudioSegment
from pydub.playback import play

wav_file = AudioSegment.from_file(file='output.wav', format='wav')
play(wav_file)