from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=280)
        self.write(arg=f"My Score: {self.score}", align="center",font=("Arial", 12, "bold"))

    def successful_score(self):
        self.score+=1
        self.clear()
        self.write(arg=f"My Score: {self.score}", align="center", font=("Arial", 12, "bold"))
