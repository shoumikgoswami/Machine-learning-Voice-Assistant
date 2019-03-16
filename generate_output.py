import pyttsx3
from bot import get_mode

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)


def gen_output(mode, text):
	if mode == 'TEXT':
		print(text)
	elif mode == 'VOICE':
		engine.say(text)
		print(text)
		engine.runAndWait()
	else:
		print('Error, Set mode of interaction')
		get_mode()