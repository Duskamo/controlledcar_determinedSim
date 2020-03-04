
import threading
import time

class GameStatus(threading.Thread):
	def __init__(self,name,car,isRunning):
		super(GameStatus, self).__init__()
		self.name = name
		self.car = car
		self.isRunning = isRunning


	def run(self):
		""
		while True:
			if self.car.carBody.getCenter().getX() > 580 and self.car.carBody.getCenter().getY() > 380:
				print(self.car.carBody.getCenter())
				self.isRunning = False

			time.sleep(1)
