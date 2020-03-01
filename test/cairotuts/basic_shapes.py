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

        self.set_title("Basic shapes")
        self.resize(460, 240)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        
    
    def on_draw(self, wid, cr):

        cr.set_source_rgb(0.6, 0.6, 0.6)

        cr.rectangle(20, 20, 120, 80)
        cr.rectangle(180, 20, 80, 80)
        cr.fill()

        cr.arc(330, 60, 40, 0, 2*math.pi)
        cr.fill()

        cr.arc(90, 160, 40, math.pi/4, math.pi)
        cr.fill()

        cr.translate(220, 180)
        cr.scale(1, 0.7)
        cr.arc(0, 0, 50, 0, 2*math.pi)
        cr.fill()
        
    
def main():
    
    app = Example()
    Gtk.main()
        
        
if __name__ == "__main__":    
    main()
