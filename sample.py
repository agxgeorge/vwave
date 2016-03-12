# Our Project, yay! 

import wave

print ("Hello World")

def main():
	waveObject = wave.open('test_mono_8000Hz_16bit_PCM.wav', 'r')
	width = waveObject.getsamplewidth()
	print (width)
	
main()


