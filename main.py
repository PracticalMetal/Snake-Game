from turtle import Turtle, Screen
import turtle
import time
from snake import Snake

# creating a screen object and changing the background colour
screen=Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake=Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

snake.move()


screen.exitonclick()