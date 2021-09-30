from turtle import Turtle
import random

# inheriting from the turtle class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # the following method stretches the shape by the given number, by default its 20 x 20 pixels
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("yellow")
        # to avoid animation
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        x_cor=random.randrange(-280,280,20)
        y_cor=random.randrange(-280,280,20)
        self.goto(x_cor,y_cor)