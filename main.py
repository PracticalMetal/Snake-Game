from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# creating a screen object and changing the background colour
screen=Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# checking for collision of the snake and the food
    if snake.head.distance(food) < 10:
        food.refresh()
        score.successful_score()



    


screen.exitonclick()