#from turtle import *
#import random

#class Ball(Turtle):
#	def __init__(self, radius, color,speed)
#	Turtle.__init__(self)
#	self.shape("circle")
#	self.color(color)
#	self.speed(speed)

#ball1=ball(10,"green",5)
#ball2=ball(7,"blue",5)

#def check_collision(ball1,ball2):
#	b1x=ball1.xcor()
#	b1y=ball1.ycor()
#	b2x=ball2.xcor()
#	b2y=ball2.ycor()
 #   if((math.sqrt(math.pow(b1x-b2x,2)+(b1y-b2y,2)))<=ball1.shapesize()[0]+ball2.shapesize()[0])
#		ball1.color="red"
#		ball2.color="gray"









 



import turtle
import time
import random
from ball import Ball
turtle.tracer(1,0)
turtle.hideturtle()



RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2



MY_BALL= Ball(12,12,10,15,23,"blue")

NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

BALLS=[]

for i in range(NUMBER_OF_BALLS):
	x=(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
	Y=(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	dx=(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	if dx<=0
		dx=+1
	dy=(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	if dy<=0
		dy=+1
	r=random.randinit(MAXIMUM_BALL_RADIUS,MINIMUM_BALL_RADIUS)
	color=random.random(),random.random(),random.random()


	new_ball=Ball(x,y,dx,dy,radius,color)
	BALLS.append(new_ball)


def move_all_balls(self):
	for ball in BALLS:
		pass
		move()



if (ball_a.r == ball_b.r and ball_a.pos == ball_b.pos):
	return False   


def collide(ball_a,ball_b):
	 if(math.sqrt(math.pow(ball_a.x-ball_b.x))+(math.pow(ball_a.y-ball_b.y)))
	 	return True
	 else
	 	return False



def check_all_balls_collision():
	for ball_a in (BALLS):
		for ball_b in (BALLS):
			if collide(ball_a,ball_b)==True:
				
				if ball1_a.radius>ball_b.radius:
					ball_a.radius=+1
					ball_a.shapesize(ball_a.r/10)
					ball_b.x=(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
					ball_b.y=(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
					ball_b.dx=(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					if ball_b.dx<=0
						ball_b.dx=+1
					ball_b.dy=(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					if ball_b.dy<=0
						ball_b.dy=+1
					ball_b.r=random.randinit(MAXIMUM_BALL_RADIUS,MINIMUM_BALL_RADIUS)
					ball_b.color=random.random(),random.random(),random.random()
          
				else
					ball_b.r=+1
					ball_b.shapesize(ball_b.r/10)
					ball_a.x=(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
					ball_a.y=(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
					ball_a.dx=(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					if ball_a.dx<=0
						ball_b.dx=+1
					ball_a.dy=(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					if ball_a.dy<=0
						ball_a.dy=+1
					ball_a.r=random.randinit(MAXIMUM_BALL_RADIUS,MINIMUM_BALL_RADIUS)
					ball_a.color=random.random(),random.random(),random.random()
          


				

				





def check_myball_collision():
	for ball in (BALLS):
		if collide(MY_BALL,ball)==True:
			if ball.r>MY_BALL.r
				return False
			else 
					MY_BALL.r+=1
					MY_BALL.shapesize(MY_BALL.r/10)
					ball.x=(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
					ball.y=(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
					ball.dx=(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					if ball.dx<=0
						ball.dx=+1
					ball.dy=(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					if ball.dy<=0
						ball.dy=+1
					ball.r=random.randinit(MAXIMUM_BALL_RADIUS,MINIMUM_BALL_RADIUS)
					ball.color=random.random(),random.random(),random.random()
    return True      








def move_around(event)
	MY_BALL.goto(event.x - screen_width,screen_height - event.y):
	


while RUNNING==True:
	if(SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2 or SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2):
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	else























