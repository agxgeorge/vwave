import numpy

from pyechonest import config
config.ECHO_NEST_API_KEY="2URAQSUTOO6R543X6"

"""Reverse a song by playing its beats forward starting from the end of the song"""
import echonest.remix.audio as audio

# Easy around wrapper mp3 decoding and Echo Nest analysis
audio_file = audio.LocalAudioFile("song1.mp3")

# You can manipulate the beats in a song as a native python list
beats = audio_file.analysis.beats
print beats
print audio_file.numChannels

beats.reverse()

# And render the list as a new audio file!
#audio.getpieces(audio_file, beats).encode("NeverGonnaTellItBackwardsByBeat.mp3")