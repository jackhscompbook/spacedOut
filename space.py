	
from pynput import keyboard
import pyautogui

def onPress(key):
	if key == keyboard.Key.esc:
		return False
	else:
		try:
			print(key.name)
		except:
			print(key.char)
			if key.char != '7':
				pyautogui.write(' ')


listener = keyboard.Listener(on_press=onPress)
listener.start() 
listener.join()
