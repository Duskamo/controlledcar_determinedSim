
import time
from KeyboardListener import *
from JoystickListener import *
from queue import Queue
from graphics import *
from GameStatus import *
from Maze import *
from Car import *
from data import *

class main():
	def __init__(self):
		self.initialize()

	def initialize(self):
		# Setup Background, game objects, and initial states
		win = GraphWin('App-Controlled Car', 800, 600)

		self.maze = Maze(win)
		self.maze.draw()

		self.car = Car(win)
		self.car.draw()

		self.isRunning = True

		# Setup Queues, Listeners, and off threads
		self.inputQueue = Queue(maxsize=0)

		#keyboardListener = KeyboardListener(self.inputQueue)
		#keyboardListener.start()

		joystickListener = JoystickListener("Web Joystick Listener", self.inputQueue)
		joystickListener.start()

		# Setup Game Loop
		self.run()

		# Pause and Close
		win.getMouse() 
		win.close() 

	def run(self):	
		# Game Loop
		while self.isRunning:
			# Process Events - Process inputs and other things
			self.processEvents()

			# Update - Update all objects that needs updating, ex position changes, physics 
			#self.car.update(joystickInput)

			# Draw - Render things on screen
			self.car.move(self.inputQueue.get()['x']*carSpeed,self.inputQueue.get()['y']*carSpeed)

			# Pause thread for framerate
			time.sleep(0.017)

	def processEvents(self):
		# Check if game is complete or not
		if self.car.carBody.getCenter().getX() > 580 and self.car.carBody.getCenter().getY() > 380:
				self.isRunning = False


if __name__ == "__main__":
	main = main()
