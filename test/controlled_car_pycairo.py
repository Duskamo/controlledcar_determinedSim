#!/usr/bin/python

'''
ZetCode PyCairo tutorial 

This code example draws another
three shapes in PyCairo.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: April 2016
'''

from gi.repository import Gtk
import cairo
import math

class cv(object):
    
	points = ( 
		( 0, 85 ), 
		( 75, 75 ), 
		( 100, 10 ), 
		( 125, 75 ), 
		( 200, 85 ),
		( 150, 125 ), 
		( 160, 190 ),
		( 100, 150 ), 
		( 40, 190 ),
		( 50, 125 ),
		( 0, 85 )
	)


class Example(Gtk.Window):

	def __init__(self):
		super(Example, self).__init__()
		
		self.init_ui()
	
	
	def init_ui(self):    
		darea = Gtk.DrawingArea()
		darea.connect("draw", self.on_draw)
		self.add(darea)

		self.set_title("Controlled Car")
		self.resize(800, 600)
		self.set_position(Gtk.WindowPosition.CENTER)
		self.connect("delete-event", Gtk.main_quit)
		self.show_all()
	
    
	def on_draw(self, wid, cr):
		cr.set_source_rgb(0, 0, 0)
		cr.set_line_width(2)

		# ************** Borders **************
		cr.rectangle(20, 20, 120, 80)
		cr.fill()
		"""
		# Top Border
		cr.move_to(50, 50)
		cr.line_to(750, 50)
		cr.stroke()

		# Bottom Border
		cr.move_to(50, 550)
		cr.line_to(750, 550)
		cr.stroke()

		# Left Border
		cr.move_to(50, 50)
		cr.line_to(50, 550)
		cr.stroke()

		# Right Border
		cr.move_to(750, 50)
		cr.line_to(750, 550)
		cr.stroke()
		"""

def main():
    
	app = Example()
	Gtk.main()
	
	
if __name__ == "__main__":    
	main()
