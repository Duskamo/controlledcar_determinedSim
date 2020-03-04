import time
from pynput import keyboard
from functools import partial

class KeyboardListener:
	def __init__(self,inputQueue):
		self.listener = None
		self.inputQueue = inputQueue

		self.COMBINATION1 = {keyboard.Key.up, keyboard.Key.right}
		self.COMBINATION2 = {keyboard.Key.up, keyboard.Key.left}
		self.current = set()

	def join(self):
		# Collect events until released
		with keyboard.Listener(
			on_press=self.on_press,
			on_release=self.on_release) as listener:
		    listener.join()

	def start(self):
		# ...or, in a non-blocking fashion:
		self.listener = keyboard.Listener(
		    on_press=partial(self.on_press))
		self.listener.start()

	def on_press(self,key):
		try:
			if key in self.COMBINATION1:
				self.current.add(key)
				if all(k in self.current for k in self.COMBINATION1):
					self.inputQueue.put({'x':1,'y':1})

			if key in self.COMBINATION2:
				self.current.add(key)
				if all(k in self.current for k in self.COMBINATION2):
					self.inputQueue.put({'x':1,'y':-1})
			elif key == keyboard.Key.up:
				self.inputQueue.put({'x':1,'y':0})
			elif key == keyboard.Key.down:
				self.inputQueue.put({'x':-1,'y':0})
			"""
			elif key == keyboard.Key.left and key == keyboard.Key.up:
				self.inputQueue.put({'x':1,'y':-1})
			elif key == keyboard.Key.right and key == keyboard.Key.up:
				self.inputQueue.put({'x':1,'y':1})
			"""
		except AttributeError:
			print('special key {0} pressed'.format(key))

