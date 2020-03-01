from graphics import *

class Car:
	def __init__(self,win):
		self.win = win
	
		self.initialize()

	def initialize(self):
		self.frontLeftWheel = Circle(Point(150,100),10)
		self.frontLeftWheel.setWidth(1)
		self.frontLeftWheel.setFill('grey')

		self.frontRightWheel = Circle(Point(150,150),10)
		self.frontRightWheel.setWidth(1)
		self.frontRightWheel.setFill('grey')

		self.backLeftWheel = Circle(Point(110,100),10)
		self.backLeftWheel.setWidth(1)
		self.backLeftWheel.setFill('grey')	

		self.backRightWheel = Circle(Point(110,150),10)
		self.backRightWheel.setWidth(1)
		self.backRightWheel.setFill('grey')	

		self.carBody = Rectangle(Point(100,100), Point(150,150))
		self.carBody.setWidth(0)
		self.carBody.setFill('blue')	

		self.carSensors = Circle(Point(150,125),25)
		self.carSensors.setWidth(0)
		self.carSensors.setFill('blue')


	def draw(self):
		self.frontLeftWheel.draw(self.win)
		self.frontRightWheel.draw(self.win)
		self.backLeftWheel.draw(self.win)
		self.backRightWheel.draw(self.win)
		self.carBody.draw(self.win)
		self.carSensors.draw(self.win)

	def move(self,dx,dy):
		self.frontLeftWheel.move(dx,dy)
		self.frontRightWheel.move(dx,dy)
		self.backLeftWheel.move(dx,dy)
		self.backRightWheel.move(dx,dy)
		self.carBody.move(dx,dy)
		self.carSensors.move(dx,dy)
