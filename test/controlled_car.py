#A simple graphics example constructs a face from basic shapes.


from graphics import *


def main():
	win = GraphWin('App-Controlled Car', 800, 600) 
	
	# Set Borders
	c = Rectangle(Point(50,50), Point(750,550))
	c.setWidth(5)
	c.draw(win)

	# Set Maze
	l1 = Line(Point(50,200), Point(550,200))
	l1.setWidth(5)
	l1.draw(win)

	l2 = Line(Point(250,350), Point(750,350))
	l2.setWidth(5)
	l2.draw(win)
	
	goalLine = Rectangle(Point(550,350), Point(750,550))
	goalLine.setWidth(3)
	goalLine.setFill("red")
	goalLine.draw(win)

	goalText = Text(Point(650,450),"GOAL")
	goalText.setSize(35)
	goalText.draw(win)

	# Set Car
	frontLeftWheel = Circle(Point(150,100),10)
	frontLeftWheel.setWidth(1)
	frontLeftWheel.setFill('grey')
	frontLeftWheel.draw(win)

	frontRightWheel = Circle(Point(150,150),10)
	frontRightWheel.setWidth(1)
	frontRightWheel.setFill('grey')
	frontRightWheel.draw(win)

	backLeftWheel = Circle(Point(110,100),10)
	backLeftWheel.setWidth(1)
	backLeftWheel.setFill('grey')
	backLeftWheel.draw(win)

	backRightWheel = Circle(Point(110,150),10)
	backRightWheel.setWidth(1)
	backRightWheel.setFill('grey')
	backRightWheel.draw(win)

	carBody = Rectangle(Point(100,100), Point(150,150))
	carBody.setWidth(0)
	carBody.setFill('blue')
	carBody.draw(win)

	carSensors = Circle(Point(150,125),25)
	carSensors.setWidth(0)
	carSensors.setFill('blue')
	carSensors.draw(win)

	# Pause and Close
	win.getMouse() 
	win.close()  

main()
