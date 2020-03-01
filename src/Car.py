from graphics import *
from math import sin, cos, radians

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


	# **** HERE, PUT IN NEW CLASS AND BLAH BLAH BLAH
	def rotate_point(point, angle, center_point=(0, 0)):
		"""Rotates a point around center_point(origin by default)
		Angle is in degrees.
		Rotation is counter-clockwise
		"""
		angle_rad = radians(angle % 360)
		# Shift the point so that center_point becomes the origin
		new_point = (point[0] - center_point[0], point[1] - center_point[1])
		new_point = (new_point[0] * cos(angle_rad) - new_point[1] * sin(angle_rad),
			 new_point[0] * sin(angle_rad) + new_point[1] * cos(angle_rad))
		# Reverse the shifting we have done
		new_point = (new_point[0] + center_point[0], new_point[1] + center_point[1])
		return new_point

	def rotate_polygon(polygon, angle, center_point=(0, 0)):
		"""Rotates the given polygon which consists of corners represented as (x,y)
		around center_point (origin by default)
		Rotation is counter-clockwise
		Angle is in degrees
		"""
		rotated_polygon = []
		for corner in polygon:
			rotated_corner = rotate_point(corner, angle, center_point)
			rotated_polygon.append(rotated_corner)
		return rotated_polygon
