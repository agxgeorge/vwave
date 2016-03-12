# Our Project, yay! 

import wave

key = "2URAQSUTOO6R543X6"

print ("Hello World")

def main():
	waveObject = wave.open('test_mono_8000Hz_16bit_PCM.wav', 'r')
	width = waveObject.getsampwidth()
	print (width)
	
main()


