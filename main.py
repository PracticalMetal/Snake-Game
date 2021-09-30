from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# creating a screen object and changing the background colour
screen=Screen()
screen.setup(height=630, width=630)
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
    snake.move()
    game_is_on=snake.check_collision()
    if game_is_on==False:
        break
    screen.update()
    time.sleep(0.1)
    

# checking for collision of the snake and the food
    if snake.head.distance(food) < 10:
        food.refresh()
        score.successful_score()
        snake.add_snake()
        



    


screen.exitonclick()