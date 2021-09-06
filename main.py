from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

UPDATED_TIME = 0

turtle = Turtle()
screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

paddle_r = Paddle(350)
paddle_l = Paddle(-350)

screen.onkey(key="Up", fun=paddle_r.move_up)
screen.onkey(key="Down", fun=paddle_r.move_down)

screen.onkey(key="w", fun=paddle_l.move_up)
screen.onkey(key="s", fun=paddle_l.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1-UPDATED_TIME)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        if UPDATED_TIME < 0.09:
            UPDATED_TIME += 0.001

    # Detect collision with the left paddle
    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if UPDATED_TIME < 0.09:
            UPDATED_TIME += 0.001

    # Detect when the ball goes out of bound in the right side
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()

    # Detect when the ball goes out of bound in the left side
    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()

screen.exitonclick()
