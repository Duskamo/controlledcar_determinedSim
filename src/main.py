
import time
from graphics import *
from Maze import *
from Car import *
from data import *

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
		# with game loop
		
		isRunning = True
		i = 0

		while isRunning:
			""
			# Process Events - Process inputs and other things
			joystickInput = joystickInputs[i]

			# Update - Update all objects that needs updating, ex position changes, physics 
			self.car.update(joystickInput)
			i += 1

			# Draw - Render things on screen
			self.car.move(joystickInput['x']*carSpeed,joystickInput['y']*carSpeed)

			# Pause thread for framerate
			time.sleep(0.017)
		


if __name__ == "__main__":
	main = main()
