from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.x_position = x_position
        self.penup()
        self.shape("square")
        self.fillcolor("white")
        self.goto(x_position, 0)
        self.shapesize(5, 1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.x_position, new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.x_position, new_y)
