from turtle import Screen, Turtle
import turtle
import time

screen=Screen()

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        initial_pos=0
        for i in range(3):
            new_turtle=Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            # new_turtle.shapesize(0.75,0.75)
            # new_turtle.turtlesize(stretch_wid=-1, stretch_len=-1)
            new_turtle.setx(initial_pos)
            initial_pos-=20
            self.segments.append(new_turtle)

    def move(self):
           
        # 0 is not included in this for loop
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor() 
            new_y=self.segments[seg_num-1].ycor()
                

            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].fd(20)
        
        


    def left(self):
        if self.segments[0].heading()==90:
            self.segments[0].left(90)  
        elif self.segments[0].heading()==270:
            self.segments[0].right(90)
            

        
    def right(self):
        if self.segments[0].heading()==90:
            self.segments[0].right(90)  
        elif self.segments[0].heading()==270:
            self.segments[0].left(90)

    def up(self):
        if self.segments[0].heading()==180:
            self.segments[0].right(90) 
        elif self.segments[0].heading()==0:
            self.segments[0].left(90)

    def down(self):
        if self.segments[0].heading()==180:
            self.segments[0].left(90) 
        elif self.segments[0].heading()==0:
            self.segments[0].right(90)  
