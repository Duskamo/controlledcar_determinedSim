
from graphics import *

class Maze:
	def __init__(self,win):
		self.win = win
	
		self.initialize()

	def initialize(self):
		# Set Borders
		self.c = Rectangle(Point(50,50), Point(750,550))
		self.c.setWidth(5)

		# Set Maze
		self.l1 = Line(Point(50,200), Point(550,200))
		self.l1.setWidth(5)

		self.l2 = Line(Point(250,350), Point(750,350))
		self.l2.setWidth(5)

		self.goalField = Rectangle(Point(550,350), Point(750,550))
		self.goalField.setWidth(3)
		self.goalField.setFill("red")

		self.goalText = Text(Point(650,450),"GOAL")
		self.goalText.setSize(35)


	def draw(self):
		self.c.draw(self.win) 
		self.l1.draw(self.win)
		self.l2.draw(self.win)
		self.goalField.draw(self.win)
		self.goalText.draw(self.win)




 


