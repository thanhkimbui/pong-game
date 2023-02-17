from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detects collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detects collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        scoreboard.r_point()
        ball.bounce_x()

    # Detects collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        scoreboard.l_point()
        ball.bounce_x()

    # Detects when right paddle misses the ball
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()

    # Detects when left paddle misses the ball
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()

screen.exitonclick()
