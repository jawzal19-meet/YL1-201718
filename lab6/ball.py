from turtle import Turtle
import turtle
import time
import random
import math
#from ball import Ball


turtle.tracer(1,0)
turtle.hideturtle()



class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.r=r

		self.penup()
		self.goto(x,y)

		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)
		self.setposition(x,y)


	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		new_x=current_x + self.dx
		current_y=self.ycor()
		new_y=current_y + self.dy
		right_side_ball=new_x + self.r
		left_side_ball=new_x -self.r
		upper_side_ball=new_y + self.r
		down_side_ball=new_y -self.r
	
		self.goto(new_x,new_y)
		if right_side_ball>screen_width:
			self.dx= -self.dx
		elif left_side_ball<-screen_width:
			self.dx= -self.dx
		elif upper_side_ball>screen_height:
			self.dy= -self.dy
		elif down_side_ball<-screen_height:
			self.dy= -self.dy
		




RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

MY_BALL= Ball(12,12,2,2,23,"blue")

NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

BALLS=[]

for i in range(NUMBER_OF_BALLS):
	x=random.randint(int(-SCREEN_WIDTH)+MAXIMUM_BALL_RADIUS,int(SCREEN_WIDTH)-MAXIMUM_BALL_RADIUS)
	y=random.randint(int(-SCREEN_HEIGHT)+MAXIMUM_BALL_RADIUS,int(SCREEN_HEIGHT)-MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	while dx==0 and dy==0:
		dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
		dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

	r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(),random.random(),random.random())
	new_ball=Ball(x,y,dx,dy,r,color)
	BALLS.append(new_ball)

def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
	if ball_b == ball_a:
		return False
	distance=math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
	if(distance + 10 < ball_a.r + ball_b.r):
	 	return True
	else:
	 	return False   


def check_all_balls_collision():
	for ball_a in (BALLS):
		for ball_b in (BALLS):
			if collide(ball_a,ball_b):
				
				if ball_a.r>ball_b.r:
					ball_a.r+=1
					ball_a.shapesize(ball_a.r/10)
					ball_b.x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
					ball_b.y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
					ball_b.goto(ball_b.x,ball_b.y)
					ball_b.dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					if ball_b.dx<=0:
						ball_b.dx=+1
					ball_b.dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					if ball_b.dy<=0:
						ball_b.dy=+1
					ball_b.r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
					ball_b.color=random.random(),random.random(),random.random()
          
				else:
					ball_b.r=+1
					ball_b.shapesize(ball_b.r/10)
					ball_a.x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
					ball_a.y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
					ball_a.dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					ball_a.goto(ball_a.x,ball_a.y)
					if ball_a.dx<=0:
						ball_b.dx=+1
					ball_a.dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					if ball_a.dy<=0:
						ball_a.dy=+1
					ball_a.r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
					ball_a.color=random.random(),random.random(),random.random()
          

def check_myball_collision():
	for ball in (BALLS):
		if collide(MY_BALL,ball)==True:
			if ball.r>MY_BALL.r:
				return False
			else:
					MY_BALL.r+=1
					MY_BALL.shapesize(MY_BALL.r/10)
					ball.x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
					ball.y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
					ball.dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					ball.dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					ball.goto(ball.x,ball.y)
					if ball.dx<=0:
						ball.dx=+1
					ball.dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					if ball.dy<=0:
						ball.dy=+1
					ball.r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
					ball.color=random.random(),random.random(),random.random()
    		return True      


def move_around(event):
	MY_BALL.goto(event.x - SCREEN_WIDTH,SCREEN_HEIGHT - event.y)

turtle.getcanvas().bind("<Motion>", move_around)
turtle.listen()


while RUNNING:
	if(SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2): #or #SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2):
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
	if(SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2):
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2


	move_all_balls()
	check_all_balls_collision()
	RUNNING= check_myball_collision()
	turtle.getscreen().update()
	time.sleep(SLEEP)


turtle.mainloop()