
import time
from graphics import *
from Maze import *
from Car import *

class main():
	def __init__(self):
		self.initialize()

	def initialize(self):
		# Setup Background and game objects
		win = GraphWin('App-Controlled Car', 800, 600)

		self.maze = Maze(win)
		self.maze.draw()

		self.car = Car(win)
		self.car.draw()

		# Setup Game Loop
		self.run()

		# Pause and Close
		win.getMouse() 
		win.close() 

	def run(self):
		time.sleep(5)
		for i in range(40):
			self.car.move(5,0)
			time.sleep(0.05)

		"""
		isRunning = True

		while isRunning:
			""
			# Process Events - Process inputs and other things

			# Update - Update all objects that needs updating, ex position changes, physics 

			# Draw - Render things on screen

			# Pause thread for framerate
			time.sleep(0.017)
		"""


if __name__ == "__main__":
	main = main()
