from turtle import *
import random

class Ball(Turtle):
	def __init__(self, radius, color,speed)
	Turtle.__init__(self)
	self.shape("circle")
	self.shapesize(radius)
	self.color(color)
	self.speed(speed)

ball1=ball(10,"green",5)
ball2=ball(7,"blue",5)

def check_collision(ball1,ball2):
	b1x=ball1.xcor()
	b1y=ball1.ycor()
	b2x=ball2.xcor()
	b2y=ball2.ycor()
    if((math.sqrt(math.pow(b1x-b2x,2)+(b1y-b2y,2)))<=ball1.shapesize()[0]+ball2.shapesize()[0])
		ball1.color="red"
		ball2.color="gray"
