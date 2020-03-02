
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
		carBodyPoints = [(self.car.carBody.getP1().getX(),self.car.carBody.getP1().getY()),(self.car.carBody.getP2().getX(),self.car.carBody.getP2().getY()), (self.car.carBody.getP1().getX()+50,self.car.carBody.getP1().getY()),(self.car.carBody.getP1().getX(),self.car.carBody.getP1().getY()+50)]
		print(carBodyPoints)

		print(self.car.rotate_polygon(carBodyPoints,90))
		
		"""
		time.sleep(5)
		for i in range(len(joystickInput)):
			self.car.move(joystickInput[i]['x']*carSpeed,joystickInput[i]['y']*carSpeed)
			time.sleep(0.05)
		"""
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
