from turtle import Turtle
import random


#	def__init__(self,size)
#		Turtle.__init__(slef)
#		self.shapesize(size)
#		self.shape("square")

#	def random_color():
#		r = random.randint(0, 256)
#		g = random.randint(0, 256)
#		b = random.randint(0, 256)
#		self.color(r, g, b)


#EXTRAAAAAAA
#############################

class Hexagon(Turtle):
	def__init__(self,size):
		Turtle.__init__(self)
		self.begin_poly()
		for i in range(6):
			self.forward(size)
			self.left(360/6)
		self.end_poly()
		turtle.register_shape("hexagon", self.get_poly())
		self.shape("hexagon")
		self.shapesize(size)

hexagon = Hexagon(10)

turtle.mainloop()


